# encoding: utf-8
"""
resume.py is a pre-processor for Markdown resumes, targeting the pandoc
document processor.

Pandoc extended Markdown supports embedded HTML (like all compliant Markdown
parser) and a subset of LaTeX, but when outputting LaTeX any unrecognized
LaTeX commands will simply be passed through.

This means you can keep your resume in pure markdown and define pre-processing
functions that do different things with different parts of the input depending
on the target output format.

Currently, the main feature is extraction of contact details.  They are
expected to begin on the fourth line, following the header and a blank line,
and extend until the next blank line.  Lines with bullets (•) will be split
into separate lines.

    Michael White
    =============

    72 Bower St. #1 • Medford, MA, 02155
    617-899-1621

You can then define a function for an output format like this:

    def tex(lines, contact_lines, *args):
        '''
        Returns the pre-processed Markdown output suitable for tex processing,
        as a string.

        lines -- a list of lines, without the contact lines
        contact_lines -- the extracted contact lines
        args -- any extra command-line arguments
        '''

And finally run it like this:

    python resume.py tex < resume.md

"""
import hashlib
import sys
import re


GRAVATAR = "http://www.gravatar.com/avatar/{hash}?s=200"


class Processor(object):
    handlers = {}

    def register(self, fn):
        self.handlers[fn.__name__] = fn
        return fn

    def process(self, format, lines, contact_lines, *args):
        try:
            handler = self.handlers[format]
        except KeyError:
            raise Exception("Unknown format: %s" % format)

        return handler(lines, contact_lines, *args)

processor = Processor()


@processor.register
def tex(lines, contact_lines, *args):
    def sub(pattern, repl, string, **kwargs):
        """Replacement for re.sub that doesn't replace pattern it's inside the
        first latex command argument brackets.  Kind of a hack."""

        flags = kwargs.pop('flags', 0) | re.X | re.M

        num_groups = re.compile(pattern, flags).groups
        pattern = r"""
            (^|}{)   # beginning of line or second argument
            ([^{}\n\r]*) # disallow { and }
            %s
            ([^{}\n\r]*)
        """ % pattern

        repl = re.sub(r"\\(\d)",
                      lambda m: r"\%d" % (int(m.group(1)) + 2), repl)

        return re.sub(pattern, r"\1\2%s\%d" % (repl, num_groups + 3), string,
                      flags=flags, **kwargs)

    # pandoc doesn't seem to support markdown inside latex blocks, so we're
    # just going to hardcode the two most common link formats for now so people
    # can put links in their contact info
    def replace_links(line):
        if '!' in line:
            return re.sub(r"!\[([^\]]+)\]\(([^\)]+)\)", r"\includegraphics[height=2cm]{\2}", line)

        line = re.sub(r"<([^:]+@[^:]+?)>", r"\href{mailto:\1}{\1}", line)
        line = re.sub(r"<(http.+?)>", r"\url{\1}", line)
        return re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r"\href{\2}{\1}", line)

    contact_lines = "\n\n".join(map(replace_links, contact_lines))

    # replacements to apply to the text in contact_lines, because it won't be
    # processed by pandoc
    replace = {
        '~': r"\\textasciitilde{}"
    }
    escape = ['#']

    for search in replace:
        contact_lines = sub(search, replace[search], contact_lines)

    for c in escape:
        contact_lines = sub(r'([^\\])\%s' % c, r'\1\%s' % c, contact_lines)

    lines.insert(0, "\\begin{nospace}\\begin{flushright}\n\\vspace{-2em}" +
                    contact_lines +
                    "\n\\end{flushright}\\end{nospace}\n")

    return "".join(lines)


@processor.register
def html(lines, contact_lines, *args):
    untex = ['LaTeX']

    for word in untex:
        # yuck
        replace = lambda l: l.replace(r"\%s" % word, word)
        lines = list(map(replace, lines))
        contact_lines = list(map(replace, contact_lines))

    gravatar = None
    for line in contact_lines:
        if '!' in line:
            # If gravatar given, ignore the one from gravatar.com
            break
        if '@' in line and '--no-gravatar' not in args:
            gravatar = GRAVATAR.format(
                hash=hashlib.md5(line.lower().strip('<>')).hexdigest())
            break
    if gravatar is not None:
        contact_lines.insert(0, "<img src='{}' />".format(gravatar))

    lines.insert(0, "<div id='container'><div id='contact'>%s</div>\n" %
                 ("<p>" + "</p><p>".join(contact_lines) + "</p>"))
    lines.insert(1, "<div>")
    lines.append("</div>")

    return "".join(lines)


def main():
    try:
        format = sys.argv[1]
    except IndexError:
        raise Exception("No format specified")

    if '-h' in sys.argv or '--help' in sys.argv:
        sys.stderr.write(
            "Usage: python resume.py tex|html [--no-gravatar] < INPUT.md\n")
        raise SystemExit

    lines = sys.stdin.readlines()

    contact_lines = []
    for line in lines[3:]:
        lines.remove(line)
        parts = [x.strip() for x in line.split("•")]
        if parts == ['']:
            break

        contact_lines.extend(parts)

    print(processor.process(format, lines, contact_lines, *sys.argv[1:]))

if __name__ == '__main__':
    main()

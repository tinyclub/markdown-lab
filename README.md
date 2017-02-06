
# Markdown Lab

This lab aims to easier the building of the markdown environment for slides, books, resume and articles.

## Download

    $ git clone https://github.com/tinyclub/markdown-lab.git
    $ cd markdown-lab/

## Installation

To install the necessary tools, try `tools/install-local-lab.sh` for local
machine and `tools/install-docker-lab.sh` for virtual machine.

For docker machine, need to open it with `tools/run-docker-lab-daemon.sh` and
login `http://localhost:6080/vnc.html` in with `ubuntu` password.

## Slides

    $ cd slides/
    $ make

To tune the theme and colortheme, based on `slides/doc/`, please configure
`latex_theme` and `latex_colortheme` in Makefile.

To specify the fonts, please open `templates/zh_template.tex` and configure the
`\set*font` commands with the fonts you want in the result of `fc-list`.

## Resume

    $ cd resume/
    $ make

If no gravatar.jpg specified, a gravatar will be added automatically if the
email address is there. To disable this feature, do:

    $ GRAVATAR_OPTION=--no-gravatar make

To specify the fonts, please open `templates/header.tex` and configure the
`\set*font` commands with the fonts you want in the result of `fc-list`.

## Article

    $ cd article/
    $ make

To specify the fonts, please open `templates/header.tex` and configure the
`\set*font` commands with the fonts you want in the result of `fc-list`.

## Book

    $ git submodule update --init book
    $ cd book/
    $ make

To specify the fonts, please open `book.jason` and configure the
`fontFamily` with the fonts you want in the result of `fc-list`.

## References

* [Markdown 基本语法](http://wowubuntu.com/markdown/)
* [Pandoc's Markdown 语法](http://johnmacfarlane.net/pandoc/demo/example9/pandocs-markdown.html)

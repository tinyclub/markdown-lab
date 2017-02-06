
# Markdown Lab

This lab aims to easier the building of the markdown environment for slides, books, resume and articles.

![Markdown Lab Demo](images/markdown-lab-demo.jpg)

## Download

    $ git clone https://github.com/tinyclub/cloud-lab.git
    $ cd cloud-lab/ && tools/docker/choose markdown-lab

## Installation

    $ tools/docker/build # Build ourselves
    or
    $ tools/docker/pull # Pull from docker hub

    $ tools/docker/uid
    $ tools/docker/identify
    $ tools/docker/run

Login the VNC page with the password printed in the console.

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


# Markdown Lab

This lab aims to easier the building of the markdown environment for slides, books, resume and articles.

![Markdown Lab Demo](images/markdown-lab-demo.jpg)

## Prepare

Please install docker at first:

* Linux and Mac OSX: [Docker CE](https://store.docker.com/search?type=edition&offering=community)
* Windows: [Docker Toolbox](https://www.docker.com/docker-toolbox)

Notes:

In order to run docker without password, please make sure your user is added in the docker group:

    $ sudo usermod -aG docker $USER

In order to speedup docker images downloading, please configure a local docker mirror in `/etc/default/docker`, for example:

    $ grep registry-mirror /etc/default/docker
    DOCKER_OPTS="$DOCKER_OPTS --registry-mirror=https://docker.mirrors.ustc.edu.cn"
    $ service docker restart

In order to avoid network ip address conflict, please try following changes and restart docker:

    $ grep bip /etc/default/docker
    DOCKER_OPTS="$DOCKER_OPTS --bip=10.66.0.10/16"
    $ service docker restart

If the above changes not work, try something as following:

    $ grep dockerd /lib/systemd/system/docker.service
    ExecStart=/usr/bin/dockerd -H fd:// --bip=10.66.0.10/16 --registry-mirror=https://docker.mirrors.ustc.edu.cn
    $ service docker restart

## Choose a working directory

If installed via Docker Toolbox, please enter into the `/mnt/sda1` directory of the `default` system on Virtualbox, otherwise, after poweroff, the data will be lost for the default `/root` directory is only mounted in DRAM.

    $ cd /mnt/sda1

For Linux or Mac OSX, please simply choose one directory in `~/Downloads` or `~/Documents`.

    $ cd ~/Documents

## Download

    $ git clone https://github.com/tinyclub/cloud-lab.git
    $ cd cloud-lab/ && tools/docker/choose markdown-lab

## Installation

    $ tools/docker/build # Build ourselves
    or
    $ tools/docker/pull # Pull from docker hub

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
    $ gitbook install
    $ make

To specify the fonts, please open `book.jason` and configure the
`fontFamily` with the fonts you want in the result of `fc-list`.

## References

* [Markdown 基本语法](http://wowubuntu.com/markdown/)
* [Pandoc's Markdown 语法](http://johnmacfarlane.net/pandoc/demo/example9/pandocs-markdown.html)

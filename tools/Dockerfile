# https://github.com/fcwu/docker-ubuntu-vnc-desktop
FROM dorowu/ubuntu-desktop-lxde-vnc
MAINTAINER Falcon wuzhangjin@gmail.com

RUN sed -i -e "s/archive.ubuntu.com/cn.archive.ubuntu.com/g" /etc/apt/sources.list

RUN apt-get -y update

RUN apt-get install -y vim git ca-certificates
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-xetex texlive-latex-recommended texlive-latex-extra
RUN apt-get install -y texlive-fonts-recommended texlive-fonts-extra
RUN apt-get install -y latex-cjk-common latex-cjk-chinese
RUN apt-get install -y latex-cjk-chinese-arphic-bkai00mp latex-cjk-chinese-arphic-bsmi00lp
RUN apt-get install -y latex-cjk-chinese-arphic-gbsn00lp latex-cjk-chinese-arphic-gkai00mp
RUN apt-get install -y latex-beamer
RUN apt-get install -y fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp fonts-arphic-gkai00mp
RUN apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei #ttf-mscorefonts-installer

WORKDIR /markdown-lab/

EXPOSE 22

ENTRYPOINT ["/startup.sh"]

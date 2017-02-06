# https://github.com/fcwu/docker-ubuntu-vnc-desktop
FROM dorowu/ubuntu-desktop-lxde-vnc
MAINTAINER Falcon wuzhangjin@gmail.com

RUN sed -i -e "s/archive.ubuntu.com/cn.archive.ubuntu.com/g" /etc/apt/sources.list

RUN apt-get -y update

RUN apt-get install -y vim git ca-certificates

# For Slides, Resume and Article
RUN apt-get install -y pandoc

RUN apt-get install -y texlive-xetex texlive-latex-recommended texlive-latex-extra
RUN apt-get install -y texlive-fonts-recommended texlive-fonts-extra
RUN apt-get install -y latex-cjk-common latex-cjk-chinese
RUN apt-get install -y latex-cjk-chinese-arphic-bkai00mp latex-cjk-chinese-arphic-bsmi00lp
RUN apt-get install -y latex-cjk-chinese-arphic-gbsn00lp latex-cjk-chinese-arphic-gkai00mp
RUN apt-get install -y latex-beamer

RUN apt-get install -y fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp fonts-arphic-gkai00mp
RUN apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei #ttf-mscorefonts-installer

# For gitbook

RUN apt-get install -y nodejs npm
RUN apt-get -y update
RUN apt-get install -y calibre

RUN npm config set registry https://registry.npm.taobao.org
RUN npm install gitbook-cli -g
RUN rm /usr/local/bin/gitbook
RUN sh -c 'echo "nodejs /usr/local/lib/node_modules/gitbook-cli/bin/gitbook.js \$@" > /usr/local/bin/gitbook'
RUN chmod +x /usr/local/bin/gitbook

RUN npm install gitbook-plugin-duoshuo -g
RUN npm install gitbook-plugin-disqus -g
RUN npm install gitbook-plugin-google_code_prettify -g
RUN npm install gitbook-plugin-collapsible-menu -g
RUN npm install gitbook-plugin-maxiang -g
RUN npm install gitbook-plugin-multipart -g

# RUN gitbook fetch latest

# Allow ubuntu user use sudo without password
ADD sudoers.d/ubuntu /etc/sudoers.d/
RUN chmod 440 /etc/sudoers.d/ubuntu

# Add shortcuts on Desktop
ADD lab.desktop /
ADD startup.sh /

# Add lab-name
ADD lab-name /
ADD lab-uid /

# Tune the screen size
ADD supervisord.conf /etc/supervisor/conf.d/

WORKDIR /markdown-lab/

EXPOSE 22

ENTRYPOINT ["/startup.sh"]

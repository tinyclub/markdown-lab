#!/bin/bash

mkdir -p /var/run/sshd

# create an ubuntu user
# PASS=`pwgen -c -n -1 10`
PASS=ubuntu
# echo "Username: ubuntu Password: $PASS"
id -u ubuntu &>/dev/null || useradd --create-home --shell /bin/bash --user-group --groups adm,sudo ubuntu

sudo -u ubuntu mkdir /home/ubuntu/Desktop/
sudo cp /markdown-lab.desktop /home/ubuntu/Desktop/
sudo chown ubuntu:ubuntu /home/ubuntu/Desktop/markdown-lab.desktop

echo "ubuntu:$PASS" | chpasswd
sudo -u ubuntu -i bash -c "mkdir -p /home/ubuntu/.config/pcmanfm/LXDE/ \
    && cp /usr/share/doro-lxde-wallpapers/desktop-items-0.conf /home/ubuntu/.config/pcmanfm/LXDE/"

cd /web && ./run.py > /var/log/web.log 2>&1 &
nginx -c /etc/nginx/nginx.conf
exec /usr/bin/supervisord -n

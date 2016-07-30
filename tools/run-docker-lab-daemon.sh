#!/bin/bash
#
# start the lab via docker with the shared source in $PWD/
#

TOP_DIR=$(dirname `readlink -f $0`)

IMAGE=$(< ${TOP_DIR}/lab-name)

local_lab_dir=`dirname ${TOP_DIR}`
remote_lab_dir=/`basename ${IMAGE}`/

browser=chromium-browser
port=6080
url=http://localhost:$port/vnc.html
pwd=ubuntu

# nfsd.ko must be inserted to enable nfs kernel server
sudo modprobe nfsd

CONTAINER_ID=$(docker run --privileged \
                --cap-add sys_admin --cap-add net_admin \
                --device=/dev/net/tun \
                -d -p $port:$port \
                -v $local_lab_dir:$remote_lab_dir \
                $IMAGE)

docker logs $CONTAINER_ID | sed -n 1p

which $browser 2>&1>/dev/null \
    && ($browser $url 2>&1>/dev/null &) \
    && echo "please login with password: $pwd" && exit 0

echo "Usage: Please open $url with password: $pwd"

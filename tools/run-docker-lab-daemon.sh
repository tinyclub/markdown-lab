#!/bin/bash
#
# start the lab via docker with the shared source in $PWD/
#

TOP_DIR=$(dirname `readlink -f $0`)

IMAGE=$(< ${TOP_DIR}/lab-name)

local_lab_dir=`dirname ${TOP_DIR}`
remote_lab_dir=/`basename ${IMAGE}`/

browser=chromium-browser
remote_port=6080

while :;
do
    retry=0
    local_port=$((RANDOM/500+6080))
    echo "new vnc port: $local_port"

    # Make sure it is unique
    ports=`docker ps -a | grep -v PORTS | cut -d':' -f2 | cut -d'-' -f1 | grep "[0-9]*" | tr '\n' ' '`
    echo "old vnc ports: $ports"

    for port in $ports
    do
	if [ $local_port -eq $port ]; then
		retry=1
		break
	fi
    done

    [ $retry -eq 0 ] && break
    echo "Retry $retry times to generate a random and unique port"
done

url=http://localhost:$local_port/vnc.html
pwd=ubuntu

# nfsd.ko must be inserted to enable nfs kernel server
sudo modprobe nfsd

CONTAINER_ID=$(docker run --privileged \
                --cap-add sys_admin --cap-add net_admin \
                --device=/dev/net/tun \
                -d -p $local_port:$remote_port \
                -v $local_lab_dir:$remote_lab_dir \
                $IMAGE)

echo "Wait for lab launching..."
sleep 5

docker logs $CONTAINER_ID 2>/dev/null | grep Password

pwd=`docker logs $CONTAINER_ID 2>/dev/null | grep Password | sed -e "s/.* VNC-Password: \(.*\)$/\1/g"`

echo $local_port > $TOP_DIR/.lab_local_port
echo $pwd > $TOP_DIR/.lab_login_pwd

$TOP_DIR/open-docker-lab.sh

# open the web lab via a browser

TOP_DIR=$(dirname `readlink -f $0`)

browser=chromium-browser
local_port=6080
[ -f $TOP_DIR/.lab_local_port ] && local_port=$(< $TOP_DIR/.lab_local_port)
url=http://localhost:$local_port/vnc.html
pwd=ubuntu

which $browser 2>&1>/dev/null \
    && ($browser $url 2>&1>/dev/null &) \
    && echo "Please login $url with password: $pwd" && exit 0

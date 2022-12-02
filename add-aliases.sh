#!/usr/bin/env bash

# This script adds aliases to the ~/.bashrc file

bashrc=`cat -e ~/.bashrc`

if [ ${bashrc: -1} != '$' ]; then
    echo '' >> ~/.bashrc
fi
echo '' >> ~/.bashrc

echo '# kubuntu-scripts' >> ~/.bashrc
echo 'alias pd="protonvpn-disconnect"' >> ~/.bashrc
echo 'alias pf="protonvpn-fastest"' >> ~/.bashrc
echo 'alias pr="protonvpn-russia"' >> ~/.bashrc
echo 'alias t="time-theme"' >> ~/.bashrc
echo 'alias td="time-theme --dark"' >> ~/.bashrc
echo 'alias tl="time-theme --light"' >> ~/.bashrc
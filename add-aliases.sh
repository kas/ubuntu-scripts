#!/usr/bin/env bash

# This script adds aliases to the ~/.bashrc file

bashrc=`cat -e ~/.bashrc`
if [ ${bashrc: -1} != '$' ]; then
    echo '' >> ~/.bashrc
fi
echo '' >> ~/.bashrc

echo '# kubuntu-scripts' >> ~/.bashrc
echo 'alias pd="protonvpn-cli ks --off && protonvpn-cli d && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pdk="protonvpn-cli ks --permanent && protonvpn-cli d && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pf="protonvpn-cli ns --ads-malware && protonvpn-cli ks --permanent && protonvpn-cli c -f && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pst="protonvpn-cli s"' >> ~/.bashrc
echo 'alias t="~/repos/kubuntu-scripts/time-theme/time-theme.py"' >> ~/.bashrc
echo 'alias td="~/repos/kubuntu-scripts/time-theme/time-theme.py --day"' >> ~/.bashrc
echo 'alias tn="~/repos/kubuntu-scripts/time-theme/time-theme.py --night"' >> ~/.bashrc
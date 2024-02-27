#!/usr/bin/env bash

# This script adds aliases to the ~/.bashrc file

bashrc=`cat -e ~/.bashrc`
if [ ${bashrc: -1} != '$' ]; then
    echo '' >> ~/.bashrc
fi
echo '' >> ~/.bashrc

echo '# ubuntu-scripts' >> ~/.bashrc
echo 'alias ab="sudo auto-cpufreq --force=reset"' >> ~/.bashrc
echo 'alias ap="sudo auto-cpufreq --force=powersave"' >> ~/.bashrc
echo 'alias as="auto-cpufreq --stats"' >> ~/.bashrc
echo 'alias pd="protonvpn-cli ks --off && protonvpn-cli d && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pdk="protonvpn-cli ks --permanent && protonvpn-cli d && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pf="protonvpn-cli ns --ads-malware && protonvpn-cli ks --permanent && protonvpn-cli c -f && protonvpn-cli s"' >> ~/.bashrc
echo 'alias pst="protonvpn-cli s"' >> ~/.bashrc
echo 'alias psw="protonvpn-cli ns --ads-malware && protonvpn-cli ks --permanent && protonvpn-cli c --cc CH && protonvpn-cli s"' >> ~/.bashrc
echo 'alias t="~/repos/kubuntu-scripts/time-theme/time-theme.py"' >> ~/.bashrc
echo 'alias td="~/repos/kubuntu-scripts/time-theme/time-theme.py --day"' >> ~/.bashrc
echo 'alias tn="~/repos/kubuntu-scripts/time-theme/time-theme.py --night"' >> ~/.bashrc

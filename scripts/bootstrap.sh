#!/usr/bin/env bash

set -euo pipefail

# Set up sudo
sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=sudo' /etc/sudoers;
echo 'vagrant ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/vagrant
chmod 600 /etc/sudoers.d/vagrant

# Change permissions of the google credential json file
chmod 755 /var/buildkite-artifact-uploader.json 

# Install pip
apt-get install -y python-pip
pip install pip --upgrade

# Install virtualenv
pip install virtualenv
#!/usr/bin/env bash

set -euo pipefail

# Set up ssh
mkdir -p /home/vagrant/.ssh
touch /home/vagrant/.ssh/authorized_keys

# Install public keys
wget --no-check-certificate "https://github.com/mitchellh/vagrant/raw/master/keys/vagrant.pub" -O /home/vagrant/.ssh/authorized_keys
chmod 700 /home/vagrant/.ssh
chmod 600 /home/vagrant/.ssh/authorized_keys
chown -R vagrant:vagrant /home/vagrant/.ssh
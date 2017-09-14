#!/usr/bin/env bash

set -euo pipefail

# Install extra package for Trusty
apt-get update
apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual


# Install docker using the repository
apt-get install -y apt-transport-https ca-certificates curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable"

apt-get update
apt-get install -y docker-ce

# Add vagrant to docker group
usermod -aG docker $USER
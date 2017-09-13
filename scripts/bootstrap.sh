#!/usr/bin/env bash

set -euo pipefail

echo 'learningequality ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/learningequality
chmod 600 /etc/sudoers.d/learningequality

# Install pip
apt-get install -y python-pip
pip install pip --upgrade
#!/usr/bin/env bash

set -euo pipefail

apt-get install -y linux-headers-$(uname -r) build-essential dkms

VERSION="`cat /home/vagrant/.vbox_version`"
mkdir -p /tmp/vbox
mount -o loop /home/vagrant/VBoxGuestAdditions_$VERSION.iso /tmp/vbox

sh /tmp/vbox/VBoxLinuxAdditions.run || echo "VBoxLinuxAdditions.run exited $? and is suppressed." \
    "For more read https://www.virtualbox.org/ticket/12479";
umount /tmp/vbox
rm -rf /tmp/vbox
rm -f /home/vagrant/*.iso

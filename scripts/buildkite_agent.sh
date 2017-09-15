#!/usr/bin/env bash

set -euo pipefail

sh -c 'echo deb https://apt.buildkite.com/buildkite-agent stable main > \
    /etc/apt/sources.list.d/buildkite-agent.list'
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys \
    32A37959C2FA5C3C99EFBC32A79206696452D198

apt-get update && apt-get install -y buildkite-agent

sed -i "s/xxx/$1/g" /etc/buildkite-agent/buildkite-agent.cfg
# Test for now
sed -i "s/^#.meta-data=.*/meta-data=\"queue=agenttesting\"/" /etc/buildkite-agent/buildkite-agent.cfg

# Add buildkite-agent to docker group
usermod -aG docker buildkite-agent

service buildkite-agent start
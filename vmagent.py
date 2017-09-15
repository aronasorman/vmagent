#!/usr/bin/env python

import os
import argparse
import subprocess
from time import sleep
from jinja2 import Environment, FileSystemLoader


box_path = 'output/packer_virtualbox-iso_virtualbox.box'
google_credential = 'credentials/google_credential.json'
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def create_vagrantbox(token, memory):
    agent_token = 'agent_token={}'.format(token)
    agent_memory = 'memory={}'.format(memory)
    
    subprocess.call(['packer', 'build', '-var', agent_token, '-var', 
        agent_memory, 'build.json'])
    while not os.path.isfile(box_path):
        sleep(10)
    print ('Vagrant box successfully generated.')


def create_vagrantfile(name, vm_number, memory, cpus):
    output_name = 'Vagrantfile'
    context ={
        'name': name,
        'number': vm_number,
        'memory': memory,
        'cpus': cpus
    }

    with open(output_name, 'w') as f:
        vagrantfile = TEMPLATE_ENVIRONMENT.get_template('vagrantfile').render(context)
        f.write(vagrantfile)


def setup_vmagent(args):
    # Check if the google credential exists
    if not os.path.isfile(google_credential):
        raise SystemExit('\033[91m' + 'Unable to find google_credential.json in folder ./credentials/'
            + '\033[0m')

    # Remove the box file if it exists in the current directory
    if os.path.isfile(box_path):
        os.remove(box_path)

    create_vagrantbox(args.token, args.memory)

    # Remove the box if it's in vagrant, since it could be generated before, which might
    # be different from current box
    output = subprocess.check_output(['vagrant', 'box', 'list'])
    if args.name in output:
        subprocess.call(['vagrant', 'box', 'remove', args.name])

    subprocess.call(['vagrant', 'box', 'add', '--name', args.name, box_path])
    create_vagrantfile(args.name, args.vm_number, args.memory, args.cpus)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setting up buildkite agents \
        using Ubuntu Trusty virtual machines.')
    parser.add_argument('--token', required=True, help='Buildkite agent\'s token.')
    parser.add_argument('--vm_number', required=True, type=int, help='Number of \
        buildkite agents to set up.')
    parser.add_argument('--name', default='buildkite_agent', help='Name of the \
        vagrant box.')
    parser.add_argument('--memory', default=1024, type=int,
        help='Memory of each buildkite agent VM (in megabytes).')
    parser.add_argument('--cpus', default=1, type=int,
        help='Number of cpus for each buildkite agent VM.')
    args = parser.parse_args()
    setup_vmagent(args)
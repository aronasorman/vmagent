#!/usr/bin/env python

import os
import argparse
import subprocess
from time import sleep
from jinja2 import Environment, FileSystemLoader


box_path = 'packer_virtualbox-iso_virtualbox.box'
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
	autoescape=False,
	loader=FileSystemLoader(os.path.join(PATH, 'templates')),
	trim_blocks=False)


def create_vagrantfile(name, number):
	output_name = 'Vagrantfile'
	context ={
		'name': name,
		'number': number
	}

	with open(output_name, 'w') as f:
		vagrantfile = TEMPLATE_ENVIRONMENT.get_template('vagrantfile').render(context)
		f.write(vagrantfile)



def parse_requirements(args):
	# Check if the box is already generated
    if not os.path.isfile(box_path):
    	agent_token = 'agent_token={}'.format(args.token)
    	agent_memory = 'memory={}'.format(args.memory)
    	subprocess.call(['packer', 'build', '-var', agent_token, '-var', 
    		agent_memory, 'build.json'])
    	while not os.path.isfile(box_path):
    		sleep(10)
    	print ('Vagrant box successfully generated.')
    output = subprocess.check_output(['vagrant', 'box', 'list'])
    if args.name not in output:
    	subprocess.call(['vagrant', 'box', 'add', '--name', args.name, box_path])
    create_vagrantfile(args.name, args.number)
    subprocess.call(['vagrant', 'up'])
    	

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setting up buildkite agents \
    	using Ubuntu Trusty virtual machines.')
    parser.add_argument('--token', required=True, help='Buildkite agent\'s token.')
    parser.add_argument('--number', required=True, type=int, help='Number of \
    	buildkite agents to set up.')
    parser.add_argument('--name', default='buildkite_agent', help='Name of the \
    	vagrant box.')
    parser.add_argument('--memory', default='1024', type=int,
    	help='Memory of each buildkite agent VM (in megabytes).')
    parser.add_argument('--google_credential', required=True, help='Path to the \
        service account key for your Google API credentials.') 
    args = parser.parse_args()
    parse_requirements(args)
# VMagent
## Summary
Create a VM image to be a buildkite agent that can be run on multiple platforms, set up a corresponding VirtualBox machine and export it to be a Vagrant box.

## Requirements
- VirtualBox
- Python 2.7 (Haven't tested on Python 3 yet)
- Packer v1.0.4
- Vagrant v1.9.3
- Jinja2

## Get started
Before running the program, you need to:
* Generate a service account key for your Google API credentials and *name it google_credential.json* to put into `credentials/` directory.
* Have a buildkite-agent token to pass to the program

To see the usage of the program, you can type `python vmagent.py -h` in the terminal:
```
Usage: vmagent.py [-h] --token TOKEN --vm_number VM_NUMBER --google_credential
                  GOOGLE_CREDENTIAL [--name NAME] [--memory MEMORY]
                  [--cpus CPUS]
Setting up buildkite agents using Ubuntu Trusty virtual machines.
optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         Buildkite agent's token.
  --vm_number VM_NUMBER
                        Number of buildkite agents to set up.
  --google_credential GOOGLE_CREDENTIAL
                        Path to the service account key for your Google API
                        credentials.
  --name NAME           Name of the vagrant box.
  --memory MEMORY       Memory of each buildkite agent VM (in megabytes).
  --cpus CPUS           Number of cpus for each buildkite agent VM.
```

To run the program, please type:
```javascript
python vmagent.py --token <buildkite_agent_token> --vm_name <number_of_vms_to_setup> --google_credential <path_to_the_credential>
```

You can also add options such as `memory` and `cpus` to configure the memory and number of cpus used in the virtual machines.

After this command you will have a Vagrant box in the `output/` folder, which is also already added to your Vagrant, and a Vagrantfile in the current directory. You can change the configurations in Vagrantfile and simply do `vagrant up` to run the virtual machines.

After you do `vagrant up`, the virtual machines will start running, and buildkite agents on these machines will be started as well.

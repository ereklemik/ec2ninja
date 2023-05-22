# EC2 Ninja

EC2 Ninja is a Python package that provides convenient methods for managing EC2 instances using the Boto3 library.

## Features

- Start an EC2 instance
- Stop an EC2 instance
- Get information about an EC2 instance
- SSH into an EC2 instance

## Installation

You can install EC2 Ninja using pip:

```shell
pip install ec2ninja

# Usage

import ec2ninja.manager

# Start an EC2 instance
ec2ninja.manager.start_instance('instance_id')

# Stop an EC2 instance
ec2ninja.manager.stop_instance('instance_id')

# Get information about an EC2 instance
instance_info = ec2ninja.manager.get_instance_info('instance_id')

# SSH into an EC2 instance
ec2ninja.manager.ssh_to_instance('instance_id', 'username', 'private_key_file')

.
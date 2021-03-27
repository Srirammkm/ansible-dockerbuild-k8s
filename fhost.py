#!/bin/python3

import boto3
import json

def tag(ec2):
    service = []
    for i in ec2.instances.filter(Filters=[]):
        for tags in ec2.Instance(i.id).tags:
            if tags["Key"] == 'Ansible':
                name = tags["Value"]
                if name not in service:
                    service.append(name)
    return service
def hosts(ec2,i):
    n = {'Name':'tag:Ansible','Values':[i]}
    host = []
    for i in ec2.instances.filter(Filters=[n]):
        host.append(i.public_ip_address)
    return host
def main():
    ec2 = boto3.resource("ec2",region_name='ap-southeast-1')
    services = tag(ec2)
    user = ""
    groups = {}
    for i in services:
        grp = hosts(ec2,i)
        if i == "ubuntu" or i == "master":
            user = "ubuntu"

        else:
            user = "ec2-user"
        groups[i] = {
                    'hosts':grp,
                    'user':user
                    }
    print(groups)
if __name__ == "__main__":
    main()
    

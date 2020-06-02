#!/usr/bin/env python3

from aws_cdk import (
    aws_ec2 as ec2,
    core
)

from aws_cdk_stacks.stacks.private import *
from aws_cdk_stacks.stacks.network_stack import NetworkStack

app = core.App()

org = 'DevOps'

environments = {
    'pro': {
        'env': core.Environment(region=REGION, account=ACCOUNT),
        'ips': '10.1.0.0/16',
        'mx_azs': 2,
    },
    'dev': {
        'env': core.Environment(region=REGION, account=ACCOUNT),
        'ips': '10.1.0.0/16',
        'mx_azs': 2,
    },
}

for key, value in environments.items():

    networkstack = NetworkStack(
        app, f'{org}-{key}-network',
        env=value.get('env'),
        org=f'{org}',
        environment=f'{key}',
        cidr=value.get('ips'),
        max_azs=value.get('mx_azs'))


app.synth()

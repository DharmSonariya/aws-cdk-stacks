#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk_stacks.stacks.private import *
from aws_cdk_stacks.aws_cdk_stacks_stack import AwsCdkStacksStack

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

    awsCdkStacksStack = AwsCdkStacksStack(
        app, f'{org}-{key}-AwsCdkStacksStack',
        env=value.get('env'),
        org=f'{org}',
        environment=f'{key}',
    )

app.synth()

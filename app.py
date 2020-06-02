#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_stacks.aws_cdk_stacks_stack import AwsCdkStacksStack


app = core.App()
AwsCdkStacksStack(app, "aws-cdk-stacks")

app.synth()

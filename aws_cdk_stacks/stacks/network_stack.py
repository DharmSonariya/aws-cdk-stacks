from aws_cdk import (
    aws_ec2 as ec2,
    core
)

# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2.README.html#vpc


class NetworkStack(core.Stack):
    def __init__(
            self, scope: core.Construct, id: str, org, environment, cidr, max_azs, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        subnet1 = ec2.SubnetConfiguration(
            name="public_stack",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=28)
        subnet2 = ec2.SubnetConfiguration(
            name="app_stack",
            subnet_type=ec2.SubnetType.PRIVATE,
            cidr_mask=24,)
        subnet3 = ec2.SubnetConfiguration(
            name="db_stack",
            subnet_type=ec2.SubnetType.ISOLATED,
            cidr_mask=28)

        self.vpc = ec2.Vpc(self, f"{org}-{environment}-vpc",
                           max_azs=max_azs,
                           cidr=cidr,
                           nat_gateways=1,
                           subnet_configuration=[subnet1, subnet2, subnet3]
                           )

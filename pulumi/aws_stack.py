import pulumi
import pulumi_aws as aws

class AwsStack(pulumi.Stack):
    def __init__(self, stack_name):
        super().__init__(stack_name)

        # Configure AWS provider region
        aws.Provider("aws-provider", region="eu-west-2")

        # Create security group for HTTP access
        security_group = aws.ec2.SecurityGroup(
            "web-sg",
            ingress=[aws.ec2.SecurityGroupIngressArgs(
                protocol="tcp",
                from_port=80,
                to_port=80,
                cidr_blocks=["0.0.0.0/0"]
            )]
        )

        # Launch EC2 instance with Python server
        instance = aws.ec2.Instance(
            "web-server",
            ami="ami-0c55b159cbfafe1f0",  # Amazon Linux 2 AMI
            instance_type="t2.micro",
            vpc_security_group_ids=[security_group.id],
            user_data="""#!/bin/bash
            echo "Hello from Pulumi" > index.html
            nohup python -m http.server 80 2>&1 &
            """
        )

        # Export public IP for verification
        self.export("public_ip", instance.public_ip)

# Register the stack
stack = AwsStack(pulumi.get_stack())
stack.register_outputs({
    "public_ip": stack.public_ip
})

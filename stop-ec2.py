import boto3
ec2 = boto3.client('ec2')
response = ec2.stop_instances(
    InstanceIds=[
        'i-0d25018aa9f104363',
    ],
    Force=True
)
print (response)
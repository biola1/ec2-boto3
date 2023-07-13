import boto3
ec2 = boto3.client('ec2')
response = ec2.start_instances(
    InstanceIds=[
        'i-0f856e79240fc3baa','i-0d25018aa9f104363','i-0739f45ebce2a52c0',
    ]
)
print(response)
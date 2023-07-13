import boto3
ec2 = boto3.client('ec2')
response = ec2.create_image(
                              InstanceId='i-08222cde91dd6d0fd',
                               Name='Black-image'
                             )
Response = response["ImageId"]
print(Response)



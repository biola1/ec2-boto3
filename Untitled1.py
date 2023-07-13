import boto3
client = boto3.client('ec2')
resp=client.run_instances(ImageId='ami-06ca3ca175f37dd66',
                      InstanceType='t2.micro',
                      MinCount=2,
                      MaxCount=2,
                      KeyName='dade.pem',
                      TagSpecifications=[
                          {
                              'ResourceType': 'instance',
                              'Tags': [{'Key': 'Name','Value': 'Linux Server'},
                                       {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
for i in resp['Instances']:
      print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))



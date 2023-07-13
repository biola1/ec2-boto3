import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(ImageId='ami-0f1d81f096d85d94b',
                                   KeyName='dade',
                                   MaxCount=3,
                                   MinCount=3,
                                   InstanceType='t2.micro',
                                  TagSpecifications=[
                                {
                                    'ResourceType': 'instance',
                                    'Tags': [
                                        {
                                            'Key': 'Name',
                                            'Value': 'dev environment'
                                        },
                                        {'Key': 'Name1',
                                        'Value': 'dev1 environment'
                                        },
                                        {'Key': 'Name2',
                                        'Value': 'dev2 environment'
                                        }
                                        
                                    ]
                                },
                            ],
                            )
for i in response['Instances']:
    print('Instance ID Created is :{} Instance Type Created is : {}' .format(i['InstanceId'],i['InstanceType']))
![image](https://github.com/biola1/ec2-boto3/assets/90300917/62bd6083-67de-4c3a-851c-1ebdb938a177)# ec2-boto3
HOW TO LAUNCH AN EC2 INSTANCE USING PYTHON BOTO3 
Hello Team, This is going to be a very interesting  topic today.
Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. The Managers are complaining about the rising cost of our development lab and need to save money by stopping our (for this example) 3 ec2 instances after all engineers are clocked out.
I will create a Python script that you can run that will stop all instances. Push your code to GitHub and include the link in your write up.
 Using python script to run AWS services is a short cut to many services,   relax while I take you for a smooth ride
The prerequisite for the projects are;
	1) AWS account
	2) Boto3 Documentation click here https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services
We will be using this documentation to create our python scripts. This has really simplified the creation of the scripts. 
	
For simplicity lets break this project into steps
	1) Set up boto3 environment
	(Please explain how to set up the boto 3 environment )
	
On your IAM generate Access Key and Secret Keys because without this you wont be able to perform this task.
Next go to your cli and install boto3 
Pip install boto3 
Aws configure
Paste your access key and secret key. 
Do not click forced update when it pops up 
Click continue without……
Now lets get busy after environment setup.
	1) I will create an AMI from my boto3 instance.
	Create a new file from template and select the  python 
Go to the boto3 documentation search for create_AMI and we will see the request to create the AMI. Here we only need the Required to create AMI which is the InstanceId 'string' and Name 'String' .The instance Id I got from the EC2 I created from the cloud9 from boto3 . The response we need is just the Image Id. Which we will use to create the EC2 instance. 
 Another method is to use the Image ID  from the AWS console when we launch the ec2 instance we will see the AMI for amazon linux and so many AMI which we can copy the AMI ID. 
• Save and run this file and Image ID is created.
	2) Next I created my key pair in the AWS console. 
	3) Create 3  ec2 instances. Make sure  with 3 different names. 
• Create a file on your AWS boto3  IDE
• Click New from template file . Select the python
• Go to the boto3 documentation and find 'run_instance'. This is the script to create the ec2 instances. So we have the follow ;
• ImageId : It is an Amazon Machine Image (AMI) id. When we create an EC2 instance the first step is to select AMI id. And it changes according to the region you choose. Here I am using us-east-1 (N. Virginia Region).
• MinCount : This specifies the minimum number of EC2 instances you want to create. You can also change it if you want.
• MaxCount : This specifies the maximum number of EC2 instances you want to create. You can also change it if you want.
• InstanceType: This specifies the type of the EC2 instance you want to create. t2.micro is the free instance type.
• Keypair: This will be the key pair we created from our console. 
• Tag: the Key and value of the instances awe created. Key will be the name and the value I used the environment. So I used dev environment and test environment and production environment 
• Save and run the script and we will see our instaces created.





 
import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(ImageId='ami-0f1d81f096d85d94b',
                                   KeyName='****',
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

	5) Create script to automate the stop of the instance 

• Create a new file. Click on file and select New from template file . Select the python
• Go to the boto3 documentation and find 'stop_instances'. This is the script to stop the ec2 instances.
• We find the required field which is the instanceId which is the name of instance we want to stop. Then we select Force to True. As seen below 

import boto3
ec2 = boto3.client('ec2')
response = ec2.stop_instances(
    InstanceIds=[
        'i-0d25018aa9f104363',
    ],
    Force=True
)
print (response)

Next is to click save and run the file and the instance is stopped 

	6) Create script to automate the stop of the instance 
• Create a new file. Click on file and select New from template file . Select the python
• Go to the boto3 documentation and find 'start_instances'. This is the script to start a stopped or hibernated  ec2 instances.
• find the required field which is the instanceId which is the name of instance we want to start. 
• Click save and run the file and all the instance are back running 
import boto3
ec2 = boto3.client('ec2')
response = ec2.start_instances(
    InstanceIds=[
        'i-0f856e79240fc3baa','i-0d25018aa9f104363'
    ]
)
print(response)


Now we are able to create, stop and start EC2 instances. I will push my codes to my github repo. 
In my next project We want to ensure that only our Development instances are stopped to make sure nothing in Production is accidentally stopped. Add logic to your script that only stops running instances that have the Environment: Dev tag.
Use your script in a Lambda function using Python 3.7 or higher runtime. Make sure the lambda runs on a set schedule daily. No one should be working in the Dev environment past 7pm. (Note: to test you may need to modify the time accordingly so you aren't waiting for 7pm)
Go to AWS console search for lambda 
First  create a lambda function 


 create a policy to start and stop ec2 
{
    "Version": "2012-10-17",
    "Statement": [
        {"Sid":"blackstopEC2",
            "Effect": "Allow",
            "Action":[
            "ec2:DescribeInstances",
            "ec2:StartInstances",
            "ec2:DescribeTags",
            "logs:*",
            "ec2:DescribeInstanceTypes",
            "ec2:StopInstances",
            "ec2:DescribeInstanceStatus"
        ],
        "Resource": "*"
        
    }]
}

Click Next Tag 
Create policy
Create a role attach the policy 
Attach the existing role in the lambda function 

Next is to create a script in python to stop ec2 instances 
Test it on lamba by creating a test 
If it returns a 200 then we are good 
Next is to schedule when the ec2 instance to stop running 
I will be using the AWS EvenBridge schedule. 
Go to eventbridge and create a new event 
Give it a name and click schedule 
Click recurring schedule and give it a time using the cron to schedule stop instance
To test I will use one-off schedule and set to 5 mins

Now our instances are stop 
Thank you for your time and I will push my code to github 
Please don’t forget to delete when you are done if you are practicing 

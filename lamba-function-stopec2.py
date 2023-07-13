import json

import boto3

ec2_resource = boto3.resource('ec2', region_name ='us-east-1')

def lambda_handler(event, context):
    ec2_instances = ec2_resource.instances.all() 

    for ec2_instance in ec2_instances: 
        ec2_instance_state = ec2_instance.state["Name"] 
        tag = ec2_instance.tags 
    
        for tag in ec2_instance.tags:
            if ("Dev" == tag['Value']) & (ec2_instance_state == 'running'): 
                stop_instance = ec2_instance.stop() 
            
                print('Dev EC2 instances are stopped: ' + str(ec2_instance.id))
    
    return "success"
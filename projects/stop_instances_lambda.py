import boto3

ec2_client = boto3.client('ec2', region_name="us-east-1")

# Define filters
dev_filter = [{'Name': 'tag:env', 'Values': ['dev']}]
qa_filter = [{'Name': 'tag:env', 'Values': ['qa']}]
prod_filter = [{'Name': 'tag:env', 'Values': ['prod']}]
stopped_instance = {'Name': 'instance-state-name', 'Values': ['stopped']}
instance_type_filter = {'Name': 'instance-type', 'Values': ['t2.micro']}

def listInstances(filters):
    """This function lists the EC2 instances based on the provided filters."""
    try:
        response = ec2_client.describe_instances(Filters=filters)
        instance_list = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_list.append(instance_id)
        return instance_list
    except Exception as e:
        print(f"ERROR: {e}")
        return None  # Return None in case of error



def stopInstances(instance_list):
    """This function stops the EC2 instances."""
    if instance_list:
        try:
            ec2_client.stop_instances(InstanceIds=instance_list)
            print("The instance has stopped successfully...")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No instances to stop.")
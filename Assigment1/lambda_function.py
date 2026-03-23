import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_instances_by_tag(ec2_client, tag_value):
    """Return list of instance IDs matching Action=<tag_value>."""
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': [tag_value]},
            {'Name': 'instance-state-name',
             'Values': ['running'] if tag_value == 'Auto-Stop' else ['stopped']}
        ]
    )
    instance_ids = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]
    return instance_ids


def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1') 

    stop_ids = get_instances_by_tag(ec2, 'Auto-Stop')
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        logger.info(f"Stopped instances: {stop_ids}")
    else:
        logger.info("No running instances found with tag Auto-Stop")
        
    start_ids = get_instances_by_tag(ec2, 'Auto-Start')
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        logger.info(f"Started instances: {start_ids}")
    else:
        logger.info("No stopped instances found with tag Auto-Start")

    return {
        'statusCode': 200,
        'body': {
            'stopped': stop_ids,
            'started': start_ids
        }
    }
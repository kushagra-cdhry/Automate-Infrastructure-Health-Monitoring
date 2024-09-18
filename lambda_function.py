import boto3
import logging
import urllib.request
import json
import os

# AWS Clients
ec2_client = boto3.client('ec2')
rds_client = boto3.client('rds')
elb_client = boto3.client('elbv2')
dynamodb_client = boto3.client('dynamodb')

# Fetch Slack Webhook URL from environment variable
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

# Logger Configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def send_slack_notification(message):
    if not SLACK_WEBHOOK_URL:
        logger.error('Slack Webhook URL is not set in environment variables.')
        return
    
    payload = json.dumps({"text": message}).encode('utf-8')
    try:
        req = urllib.request.Request(SLACK_WEBHOOK_URL, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                logger.info(f'Slack notification sent: {message}')
            else:
                logger.error(f'Failed to send Slack notification. Status: {response.status}')
    except Exception as e:
        logger.error(f'Error sending Slack notification: {e}')

def check_ec2_health():
    try:
        response = ec2_client.describe_instance_status(IncludeAllInstances=True)
        instances = response.get('InstanceStatuses', [])
        for instance in instances:
            instance_id = instance['InstanceId']
            status = instance['InstanceStatus']['Status']
            logger.info(f'EC2 Instance {instance_id}: {status}')
            if status != 'ok':
                send_slack_notification(f'EC2 Instance {instance_id} is {status}')
    except Exception as e:
        logger.error(f'Error checking EC2 health: {e}')

def check_rds_health():
    try:
        response = rds_client.describe_db_instances()
        db_instances = response.get('DBInstances', [])
        for db_instance in db_instances:
            db_instance_id = db_instance['DBInstanceIdentifier']
            status = db_instance['DBInstanceStatus']
            logger.info(f'RDS Instance {db_instance_id}: {status}')
            if status != 'available':
                send_slack_notification(f'RDS Instance {db_instance_id} is {status}')
    except Exception as e:
        logger.error(f'Error checking RDS health: {e}')

def check_elb_health():
    try:
        response = elb_client.describe_load_balancers()
        load_balancers = response.get('LoadBalancers', [])
        for lb in load_balancers:
            lb_arn = lb['LoadBalancerArn']
            lb_name = lb['LoadBalancerName']
            target_groups_response = elb_client.describe_target_groups(LoadBalancerArn=lb_arn)
            target_groups = target_groups_response.get('TargetGroups', [])
            for tg in target_groups:
                tg_arn = tg['TargetGroupArn']
                health_response = elb_client.describe_target_health(TargetGroupArn=tg_arn)
                target_healths = health_response.get('TargetHealthDescriptions', [])
                for target_health in target_healths:
                    target_id = target_health['Target']['Id']
                    health_status = target_health['TargetHealth']['State']
                    logger.info(f'ELB Load Balancer {lb_name} Target {target_id}: {health_status}')
                    if health_status != 'healthy':
                        send_slack_notification(f'ELB Load Balancer {lb_name} Target {target_id} is {health_status}')
    except Exception as e:
        logger.error(f'Error checking ELB health: {e}')

def check_dynamodb_health():
    try:
        response = dynamodb_client.list_tables()
        tables = response.get('TableNames', [])
        for table_name in tables:
            logger.info(f'DynamoDB Table {table_name} is available.')
    except Exception as e:
        logger.error(f'Error accessing DynamoDB tables: {e}')
        send_slack_notification(f'DynamoDB tables check encountered an error: {e}')

def lambda_handler(event, context):
    logger.info('Starting AWS monitoring script')
    check_ec2_health()
    check_rds_health()
    check_elb_health()
    check_dynamodb_health()
    logger.info('AWS monitoring script finished')

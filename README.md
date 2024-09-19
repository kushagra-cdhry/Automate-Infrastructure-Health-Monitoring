# Automate Infrastructure Health Monitoring

This repository contains a zip file of a Python script designed to monitor the health of AWS resources and send notifications to Slack when issues are detected. The script performs health checks on EC2 instances, RDS instances, ELB load balancers, and DynamoDB tables.

## Features

### EC2 Health Checks
- Monitors the status of EC2 instances.
- Sends a Slack notification if any instance is not in an `ok` state.

### RDS Health Checks
- Checks the status of RDS instances.
- Sends a Slack notification if any instance is not `available`.

### ELB Health Checks
- Monitors the health of targets behind ELB (Elastic Load Balancer).
- Sends a Slack notification if any target is not `healthy`.

### DynamoDB Checks
- Confirms the availability of DynamoDB tables.
- Sends a Slack notification if any table is not in `ACTIVE` state or if there’s an error accessing tables.

## Setup Instructions

1. **Slack Setup**:
   - First, set up slack locally or over the browser and create a workspace.
     <img width="1440" alt="Screenshot 2024-09-19 at 12 05 04 AM" src="https://github.com/user-attachments/assets/d0b616de-4f43-4543-8d14-015a1dd579a3">
   - Get the Slack Webhook URL. You can follow the instructions [here](https://api.slack.com/messaging/webhooks) to learn how to get webhook URL in your Slack application.
   - Add a custom app in your Slack application from scratch and get the webhook URL
     <img width="1440" alt="Screenshot 2024-09-19 at 4 05 30 AM" src="https://github.com/user-attachments/assets/b335c6f2-1879-4a57-a170-cecebfdbbf96">
     <img width="1440" alt="Screenshot 2024-09-19 at 12 17 09 AM" src="https://github.com/user-attachments/assets/8ecd85df-d0fe-4783-bc13-a2b3a6963277">
     <img width="1440" alt="Screenshot 2024-09-19 at 12 19 16 AM" src="https://github.com/user-attachments/assets/479d0cc4-3deb-4879-8afc-08d1e842cf1d">


3. **IAM Permissions**:
   - Ensure your Lambda function has a inline policy attached with the necessary permissions to access EC2, RDS, ELB, and DynamoDB services. Use the following JSON policy:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "Statement1",
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeInstanceStatus",
                   "rds:DescribeDBInstances",
                   "elasticloadbalancing:DescribeLoadBalancers",
                   "elasticloadbalancing:DescribeTargetGroups",
                   "elasticloadbalancing:DescribeTargetHealth",
                   "dynamodb:ListTables",
                   "dynamodb:DescribeTable"
               ],
               "Resource": "*"
           }
       ]
   }
4. **Deploy the Lambda Function**:
   - Upload the zip file given in the repository into your lambda function.
     <img width="1440" alt="image" src="https://github.com/user-attachments/assets/fe7670a1-1872-429a-b924-b7d5ab51d091">
   - Set the Slack Webhook URL as a environment variable in your lambda configuration.
     <img width="1440" alt="image" src="https://github.com/user-attachments/assets/56945cf9-cdaf-44e2-910b-170ad360c938">
     




  
5. **Setup cloudwatch rule to trigger the lambda function and schedule it for the desired time you want your lambda function to get triggered and then select the target which is again the lambda function you want to trigger**.
   <img width="1440" alt="image" src="https://github.com/user-attachments/assets/b288bedf-72bf-4c78-95d5-0e960d6f5fb4">
   <img width="1440" alt="image" src="https://github.com/user-attachments/assets/65dd0c06-4ea9-47f6-849c-4a8dff571bd3">
   <img width="1440" alt="image" src="https://github.com/user-attachments/assets/20a66706-572c-4f2e-aeb5-b7b5dcad02e2">



7. **Testing**:
   - Trigger the Lambda function manually first to ensure it correctly monitors the services and sends notifications.
   <img width="1440" alt="Screenshot 2024-09-19 at 4 17 17 AM" src="https://github.com/user-attachments/assets/0e14fdae-05d8-4dc1-b72c-d9127a48b008">


## Functional Logging in Cloudwatch and Notifications in Slack
- The function logs gets stored in cloudwatch log group with timestamps and notifications are coming on slack in realtime.
  <img width="1438" alt="image" src="https://github.com/user-attachments/assets/766aad56-7ae3-4c2b-9de3-f4a81d97ef1e">
  <img width="1439" alt="image" src="https://github.com/user-attachments/assets/45f2f165-b2a4-4076-b524-07ec5ecd95f7">
  ![image](https://github.com/user-attachments/assets/e5b605fb-ec29-4710-bf07-9230bbf94969)


## Conclusion
This Lambda function monitors important AWS services and helps you quickly fix any issues by sending notifications to Slack.

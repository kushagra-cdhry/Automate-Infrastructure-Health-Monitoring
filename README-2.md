# Automate Infrastructure Health Monitoring

This README file contains setup instaruction to perform the same task but in a differnt way and that is by dockerizing the python script and pushing it to ECR and then we will run lambda by that container image.

## Features
This includes the same features as the previous one so you can refer README.md file in the given repository.

## Setup Instructions

1. **Slack Setup**:
   - This step will be exactly same as it was in the README.md file.
  
2. **IAM Permissions**:
   - This will also have the inline policy with same permissions which wee in README.md.

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
4. **Create Docker image from the given Dockerfile in the repository, push it to ECR and then Deploy the Lambda Function from this container image**:
   - Push the image to ECR.
     ![image](https://github.com/user-attachments/assets/842dba5b-1a19-4d00-9500-049e851f3fd3)
   - Crete the lambda function from this container image and carefully choose the architecture of function. If you created yor image on arm architecture based system (Mac) then select arm, otherwise selct x86_64 if you created your image from Windows.
     ![image](https://github.com/user-attachments/assets/e732fa3c-598d-4dad-b9ff-6f4e34821652)
   - Set the Slack Webhook URL as a environment variable in your lambda configuration.
     <img width="1440" alt="image" src="https://github.com/user-attachments/assets/56945cf9-cdaf-44e2-910b-170ad360c938">


5. **Setup cloudwatch rule to trigger the lambda function and schedule it for the desired time you want your function to get triggered and then select your function as target**.
   - Steps for this setu will be same as it was in README.md.
   - Just select target carefully.
  
6. **Testing**:
   - Trigger the Lambda function manually first to ensure it correctly monitors the services and sends notifications:
     ![image](https://github.com/user-attachments/assets/805bf7b7-1d4d-4dab-92d6-67152630b046)


7. **Functional Logging in Cloudwatch and Notifications in Slack**:
   - The function logs gets stored in cloudwatch log group with timestamps and notifications are coming on slack in realtime.
     <img width="1438" alt="image" src="https://github.com/user-attachments/assets/766aad56-7ae3-4c2b-9de3-f4a81d97ef1e">
     <img width="1439" alt="image" src="https://github.com/user-attachments/assets/45f2f165-b2a4-4076-b524-07ec5ecd95f7">
     ![image](https://github.com/user-attachments/assets/e5b605fb-ec29-4710-bf07-9230bbf94969)


## Conclusion
This Lambda function which is created with the container image of a python script monitors important AWS services and helps you quickly fix any issues by sending notifications to Slack.

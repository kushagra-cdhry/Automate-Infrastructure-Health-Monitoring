# AWS Monitoring Script

This repository contains a Python script designed to monitor the health of AWS resources and send notifications to Slack when issues are detected. The script performs health checks on EC2 instances, RDS instances, ELB load balancers, and DynamoDB tables.

## Features

- **EC2 Health Checks**: Monitors the status of EC2 instances and sends notifications if any instance is not in an `ok` state.
- **RDS Health Checks**: Checks the status of RDS instances and sends notifications if any instance is not `available`.
- **ELB Health Checks**: Monitors the health of targets behind ELB load balancers and sends notifications if any target is not `healthy`.
- **DynamoDB Checks**: Confirms the availability of DynamoDB tables and sends notifications if there is an error accessing tables.

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. [Install Docker](https://docs.docker.com/get-docker/).
- **AWS Credentials**: Ensure your AWS credentials are set up in the environment where the container runs. The script uses `boto3` to interact with AWS services.

## Environment Variables

- **SLACK_WEBHOOK_URL**: Your Slack webhook URL for sending notifications. Set this environment variable when running the Docker container.

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/aws-monitoring-script.git
   cd aws-monitoring-script

2. **Build the Docker Image**

docker build -t aws-monitoring-script . 

3. **Run the Docker Container**
   ```bash
   docker run -e SLACK_WEBHOOK_URL="your_slack_webhook_url" aws-monitoring-script
Replace "your_slack_webhook_url" with your actual Slack webhook URL.

4. Verify the Script is Running
Check the logs to ensure the script is running as expected and sending notifications to Slack. You can view the logs using:
   ```bash
   docker logs <container_id>  
Replace <container_id> with the ID of your running container, which you can obtain using docker ps.

5. **Script Details**
File: your_script.py
Dependencies: boto3

6. **Contributing**
If you have suggestions or improvements, please open an issue or submit a pull request.

7. **License**
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions:

1. **Replace placeholders**: Replace `yourusername` with your GitHub username and `your_script.py` with the actual name of your script file if it's different.
2. **Add a License**: If you use a license, include the `LICENSE` file in the repository; otherwise, adjust the license section as needed.

Feel free to adjust the content according to your needs or add any additional sections relevant to you

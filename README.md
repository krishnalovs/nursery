
Django Application Deployment Documentation:
Table of Contents
• Introduction
• Prerequisites
• Creating EC2 Instance and Git Setup
o Create EC2 Instance
o SSH into EC2 Instance
o Install Git
o Clone the Repository
• Installing Required Tools on EC2
o GitHub
o Django
o Docker
o Jenkins
• Deploying a Django Application on EC2
• Dockerizing the Django Application
• Configuring Jenkins for Automation
• Additional Steps
o Git Clone and Virtual Environment Setup
o Install Widget Tweaks and Auto Slugs
• Conclusion
Introduction
This documentation guides you through deploying a Django application on an EC2 instance, 
Docker zing it, and configuring Jenkins for automated deployment. The process involves 
setting up tools, deploying manually, Docker zing, and automating with Jenkins.
Prerequisites
Ensure you have:
• AWS Account
• Key pair for SSH access to EC2
• Django application ready for deployment
Creating EC2 Instance and Git Setup:
Create EC2 Instance
• Log in to your AWS Management Console.
• Navigate to the EC2 dashboard.
• Click "Launch Instance" and choose an Amazon Linux 2 AMI.
• Configure instance details, add storage, and configure security groups to allow SSH (port 
22).
• Launch the instance and select your key pair.
SSH into EC2 Instance
# Replace key.pem with your private key file
ssh -i "key.pem" ec2-user@<your-ec2-ip>
Launch an ec2 instance and connect putty,mobaxtrem etc to connect instance with your key pair
In inside instance select root user and to follow these steps:
Installing Required Tools on EC2:
Install Git:
sudo yum install git
Clone the Repository
# Replace <repository_url> with your Git repository URL
git clone <repository_url>
cd <project_directory>
So the project is cloned sucessfully in your server so open the project directory
Ex: cd nursery/nursery2-main\NurseryLatest
Dockerfile,db.sqlite3,drive,manage.py,media,my_drive,Requirements.txt,venv
these files shown
Install Django on ec2:
Open your project directory like cd nursery/nursery2-main\NurseryLatest
And install Django following these commands
sudo yum install python3-pip
pip install django
pip install django-widget-tweaks django-autoslug
python3 manage.py migrate
python manage.py runserver 0.0.0.0:8001( which port you give replace it that no)
NOTE: YOUR DJANGO APP IS SUCESSFULLY DEPLOY IN EC2 SERVER
DOCKERIZE DJANGO APP:
Open your project directory like cd nursery/nursery2-main\Nursery-Latest
In this directory to install docker and start the docker following these commands
sudo yum install -y docker
sudo service docker start
sudo docker –version
> next build the docker image what you give in Dockerfile
docker build . -t <give any name>
Ex: docker build . -t myapp 
> your docker image is successfully build as your docker file code and give the image id
To show the docker images use this cmd
docker images
docker inspect <image name>
> next run your build image following this command
docker run -p 8002:8002 ImageID (in this which port no you used to write it and give image 
id)
NOTE: YOU SUCESSFULLY CREATE YOUR DOCKER IMAGE AND RUN A CONTAINER
>TEST THIS CASE YOU USE YOUR INSTANCE IP: PORTNO (EX:172.32.34.56:8002)
To install Jenkins, set up a basic configuration, and deploy an application through GitHub 
using a webhook, follow these steps:
Step 1: Install Jenkins on EC2
a) SSH into your EC2 instance. Open your instance and connect it next these steps 
follow.
b) Install Java (Jenkins requires Java):
sudo yum install java-1.8.0-openjdk
c) Add the Jenkins repository key:
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhatstable/jenkins.repo
d) Import the repository GPG key:
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
e) Install Jenkins:
sudo yum install jenkins –y
f) Start Jenkins service:
sudo systemctl start jenkins
g) Enable Jenkins to start on boot
sudo systemctl enable jenkins
h) Check Jenkins service status:
sudo systemctl status jenkins
I) Open your browser and navigate to http://your_ec2_instance_ip:8080. Retrieve 
the Jenkins unlock key from the Jenkins server log.
i) Access Jenkins log:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
j) Follow the instructions on the Jenkins web interface to complete the setup.
Step 2: Install GitHub Plugin in Jenkins
• Once Jenkins is installed and running, navigate to "Manage Jenkins" -> "Manage Plugins" -> 
"Available" tab.
• Search for "GitHub Integration" or "GitHub" in the available plugins list.
• Select the checkbox next to "GitHub Integration" and click "Install without restart."
Step 3: Set Up Jenkins Job
• Create a new Jenkins job:
o Click on "New Item" on the Jenkins dashboard.
o Enter a name for your project and select "Freestyle project" or another relevant project 
type.
o Click "OK."
• Configure the job:
o Under the "Source Code Management" section, select "Git."
o Enter your GitHub repository URL.
o In the "Build Triggers" section, check "GitHub hook trigger for GITScm polling."
o In the "Build" section, add build steps as needed (e.g., running shell commands, Docker 
build, etc.).
• Save the configuration.
Step 4: Set Up GitHub Webhook
• In your GitHub repository, go to "Settings" -> "Webhooks" -> "Add webhook."
• Set the Payload URL to your Jenkins server's GitHub webhook endpoint 
(http://your_jenkins_server/github-webhook/).
• Content type should be "application/json."
• Set the webhook to trigger on "Just the push event" or customize as needed.
• Add the webhook.
Step 5: Deploy Application
• Whenever you push changes to your GitHub repository, the Jenkins job should be triggered 
automatically.
• Monitor the Jenkins job console output for the build and deployment process.
• You've successfully set up Jenkins to deploy your application through a GitHub webhook.
NOTE: Ensure your Jenkins server and GitHub repository have the necessary permissions and 
configurations for this integration to work seamlessly. Adjust security settings and credentials as 
needed

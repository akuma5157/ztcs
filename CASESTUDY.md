# Part 1:
1. Write an ansible playbook for installing nginx, docker, logrotate. Ensure nginx container is running on port 8080 on host and log rotation is cleaning the logs of stdout of nginx container once it reaches 100mb. (Separate roles should be created for the tasks mentioned inline) 
2. Create a Dockerfile and docker-compose to run a 3 Tier application with backend api(node, python or any sample backend application), database and a nginx server. Mount volumes for persistent data for database Server.  
  a. Configure nginx to enable https  
  b. Redirect http to https  
  c. Create a self signed certificate - document how to do it.  
  d. Whitelist Ip’s  
  e. Any other important configurations  
2. Setup a python script that connects to remote servers over ssh and does the following:  
  a. Accept commands to be executed on all the remote machines at once  
  b. Wait for the execution to be completed on all the remote machines  
  c. Accept next input only once the previous execution is completed on all the machines (failed/successful)
# Part 2:
4. Create a Two tier application infrastructure any cloud provider (Preferably in AWS) using Terraform, components that should be included are mentioned below  
  a. VPC   
  b. Security Group  
  c. Subnet (Public and Private)  
  d. NAT (Instance or service)  
  e. EC2 instance  
  f. Terraform should use modules for reusability  
5. Shell script to take third most CPU & Memory consuming process, this should output to output file with the following properties  
  a. Process Name  
  b. % CPU  used  
  c. % Memory used   
  d. PORT  
  e. PID 
6. Write a kubernetes (preferably helm) template that deploys nginx with custom configuration and exposes services as NodePort 

**Mandatory to choose at least 1 out of 3 questions in each part to be attempted.**

#after restarting the ec2 instance repeat this steps

#!/bin/bash

sudo systemctl start docker

aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 217870417089.dkr.ecr.ap-south-1.amazonaws.com

docker pull 217870417089.dkr.ecr.ap-south-1.amazonaws.com/ml-iris-api:latest

docker rm -f iris-api 2>/dev/null

docker run -d --restart unless-stopped --name iris-api -p 80:5000 217870417089.dkr.ecr.ap-south-1.amazonaws.com/ml-iris-api:latest

echo "App Started Successfully"



# give permissions
#chmod +x start_app.sh

#execute the .sh file
#./start_app.sh


# 🚀 ML Docker Deployment with AWS (Iris Classifier)

## 📌 Project Overview
This project demonstrates an end-to-end deployment of a Machine Learning model using:
- Scikit-learn
- Flask
- HTML/CSS
- Docker
- AWS ECR
- AWS EC2

The application predicts Iris flower species using a web UI and API.

---

## 🎯 Features
- ML model training
- REST API
- Web UI
- Dockerized app
- AWS deployment

---

## 🧱 Project Structure
ml-docker-deploy/
├── app/
│   ├── app.py
│   ├── model.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── Dockerfile
├── docker-compose.yml
└── README.md

---

## ⚙️ Local Setup
python3 -m venv venv  
source venv/bin/activate  
pip install -r app/requirements.txt  
cd app  
python app.py  

Open: http://127.0.0.1:5000/

---

## 🐳 Docker
docker build -t ml-iris-api .  
docker run -d -p 5000:5000 ml-iris-api  

---

## ☁️ AWS Deployment
Push:
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com  
docker tag ml-iris-api:latest <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/ml-iris-api:latest  
docker push <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/ml-iris-api:latest  

EC2:
sudo systemctl start docker  
docker pull <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/ml-iris-api:latest  
docker run -d -p 80:5000 ml-iris-api  

---

## 🌐 Access
http://<EC2_PUBLIC_IP>/

---

## 🔌 API
GET /health  
POST /predict  

---

## ⚠️ Challenges
- Port conflicts
- Docker issues
- AWS auth errors
- ARM vs AMD64 mismatch

---

## 👨‍💻 Author
Pavan Ramavath  
SVNIT Surat  

⭐ Star this repo if helpful!
EOF

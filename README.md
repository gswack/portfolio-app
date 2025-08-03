## Overview
A python-based web application designed to demonstrate scalable development and modern DevOps practices. It leverages Docker, Kubernetes, and GitOps principles to showcase infrastructure-as-code, automated CI/CD pipelines, and declarative deployment using Helm and ArgoCD.

## 🧱 Tech Stack
- Helm  
- Docker  
- Kubernetes  
- Terraform  
- GitHub Actions (CI/CD)
- ArgoCD    

## 🚀 How to Run Locally  
# Clone the repo
git clone https://github.com/gswack/portfolio-app.git
cd portfolio-app
# Run the Python app
python app.py
# Build Docker image
docker build -t gswack/portfolio-app .
# Run container locally
docker run -p 5000:5000 gswack/portfolio-app

## Deployment instructions
helm install myapp ./charts/myapp

## ⚙️ CI/CD Overview
This project uses **GitHub Actions** to automate testing and integration.
- The workflow is defined in `.github/workflows/ci.yml`
- It runs automatically on:
  - Pushes to the `main` branch
  - Pull requests
- It installs dependencies and runs test scripts to ensure code quality
- Test results are visible directly in the GitHub Actions tab
- Failed runs trigger email or GitHub notifications with 
- Syncs between GitHub and ArgoCD for webhooks

## Project Structure
portfolio-app/
├── app/  
│   └── app.py
├── Dockerfile
├── charts/
│   └── myapp/
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md

## License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.

See the LICENSE file for full details.

## Contributions
Contributions are welcome and appreciated! If you'd like to improve this project, feel free to:

Fork the repository
Create a new branch (git checkout -b feature-name)
Make your changes
Submit a pull request
Please ensure your code follows the existing style and passes all tests before submitting.

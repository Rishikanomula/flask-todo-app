# 📝 To-Do App with Flask, Docker, and GitHub Actions CI/CD:

•A simple and clean task manager built using Flask with features like user authentication, task creation/editing, dark mode, and due dates.

•This project is containerized using Docker and uses GitHub Actions for automated CI/CD.

## 🚀 Features:
•User Registration & Login (Flask-Login)

•Create, Edit, Complete & Delete Tasks

•Dark Mode Toggle

•Due Date & Reminder Support (coming soon)

•Dockerized for easy deployment

•GitHub Actions for CI/CD (Docker image built and pushed on every push to main)

## 🛠 Tech Stack:
•Backend: Python + Flask

•Frontend: HTML, CSS (Bootstrap)

•Database: SQLite

•Authentication: Flask-Login

•DevOps: Docker, GitHub Actions

## 📦 Setup Instructions:
1. Clone the Repository

    git clone https://github.com/yourusername/flask-todo-app.git

    cd flask-todo-app

2. Create Virtual Environment (for local dev)

-     python -m venv venv

or

    venv\Scripts\activate  # on Windows

next

    pip install -r requirements.txt

3. Run the App Locally

    python app.py

•Visit: http://127.0.0.1:5000

## 🐳 Docker Usage:

•Build Docker Image:

    docker build -t flask-todo-app .

•Run Docker Container:

    docker run -p 5000:5000 flask-todo-app

## 🤖 CI/CD with GitHub Actions:

•On every push to main, GitHub Actions:

 - Builds the Docker image

 - Pushes it to Docker Hub

•To enable:

  - Create GitHub repo

  - Add DOCKER_USERNAME and DOCKER_PASSWORD in GitHub → Settings → Secrets

  - Push your code to GitHub

• Workflow file is in .github/workflows/deploy.yml

## 🌐 Deployment (Optional)

•You can deploy your Docker container on:

•Render

•Fly.io

•Railway

•AWS / EC2 / DigitalOcean (manual)

## 📁 File Structure

flask-todo-app/

│

├── app.py                  # Main Flask app

├── templates/              # HTML templates (index.html, login.html, etc.)

├── static/                 # CSS and JS files

├── requirements.txt        # Python dependencies

├── Dockerfile              # Docker instructions

├── .github/workflows/      # GitHub Actions CI/CD

└── README.md

## ✍️ Author:

• Nomula Rishika

• GitHub: @Rishikanomula

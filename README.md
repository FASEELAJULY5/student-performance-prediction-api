# Student Performance Prediction API

A machine learning application that predicts student performance based on **study hours** and **attendance**.

The trained machine learning model is served through a **FastAPI REST API** and containerized using **Docker** for a consistent and reproducible deployment environment.

## 🚀 Project Overview

This project demonstrates how a trained machine learning model can be converted into a usable API and deployed inside a Docker container.

The workflow is:

**Machine Learning Model → FastAPI → Docker → Swagger/OpenAPI**

## 🛠️ Technologies Used

* Python
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* NumPy
* Docker
* Swagger/OpenAPI

## 🤖 Machine Learning Model

A **Decision Tree Classifier** is used to predict the student's result.

### Input Features

* `study_hours`
* `attendance`

### Output

* `Pass`
* `Fail`

The trained model is saved using **Joblib** and loaded by the FastAPI application.

## 🔌 API Endpoint

### POST `/predict`

The API accepts study hours and attendance as input.

Example request:

```json
{
  "study_hours": 5,
  "attendance": 80
}
```

Example response:

```json
{
  "prediction": "Pass"
}
```

## 🐳 Docker Deployment

The FastAPI application and trained machine learning model are packaged into a Docker image.

The application runs inside a Docker container using:

```bash
docker run -p 8000:8000 ml-fastapi
```

The port mapping:

```text
8000:8000
```

connects port **8000 on the host machine** to port **8000 inside the Docker container**.

## 📖 API Documentation

Once the Docker container is running, the API can be tested using the automatically generated Swagger/OpenAPI documentation:

```text
http://127.0.0.1:8000/docs
```

The `/predict` endpoint can be tested directly from Swagger.

## 📁 Project Structure

```text
student-performance-prediction-api/
│
├── newmodel.py
├── newmodel.pkl
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## ▶️ How to Run

### 1. Build the Docker image

```bash
docker build -t ml-fastapi .
```

### 2. Run the container

```bash
docker run -p 8000:8000 ml-fastapi
```

### 3. Open Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

### 4. Test the prediction endpoint

Use:

```json
{
  "study_hours": 5,
  "attendance": 80
}
```

The API returns the predicted result.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Training and saving a machine learning model
* Loading a trained model using Joblib
* Building a REST API with FastAPI
* Testing an API using Swagger/OpenAPI
* Creating a Docker image
* Running an ML application inside a Docker container
* Managing Python dependencies
* Understanding Docker port mapping
* Verifying application files and dependencies inside a running container

## 📌 Project Purpose

This project was created as a practical learning project to understand the process of taking a machine learning model from **training to API deployment and containerization**.

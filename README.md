# 🏠 House Price Prediction — MLOps Project

This project demonstrates an **end-to-end Machine Learning pipeline** for predicting house prices, with a focus on **MLOps best practices** — including reproducibility, automation, CI/CD, and API deployment.

---

## 🚀 Project Overview

The goal of this project is to build, train, and serve a machine learning model capable of predicting house prices based on property features.
It integrates core **MLOps concepts** such as:

* Environment management with `venv`
* Automated workflows with `Makefile`
* Continuous integration via **GitHub Actions**
* Model persistence (`joblib`)
* API deployment using **FastAPI**
* Model retraining & hyperparameter optimization using **GridSearchCV**

---

## 🧠 Project Structure

```
HousePricePrediction/
├── app.py               # FastAPI app for prediction and retraining
├── main.py              # Main ML pipeline
├── retrain.py           # Retrain model with GridSearchCV
├── prepare.py           # Data loading and preprocessing
├── train.py             # Model training
├── test.py              # Model testing
├── evaluate.py          # Model evaluation
├── Makefile             # Automates the pipeline and API testing
├── requirements.txt     # Python dependencies
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml   # GitHub Actions workflow
├── house_price_model.joblib     # Saved trained model
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/farahderbell/HousePricePrediction.
cd HousePricePrediction
```

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧩 Usage

### ▶️ Run the full ML pipeline

```bash
make pipeline
```

### 🔄 Retrain the model with GridSearchCV

```bash
python retrain.py
```

### 🌐 Run the FastAPI app

```bash
make run_api
```

Access Swagger docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Test the API

```bash
make test_api
```

or manually:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"data": {"bedrooms": 3, "bathrooms": 2.0, "sqft_living": 1800, "sqft_lot": 5000, "floors": 1}}'
```

---

## ⚙️ GitHub Actions Workflow (CI/CD)

A CI/CD workflow is configured in `.github/workflows/mlops-pipeline.yml` to automate key steps.

### 🔁 Workflow Overview

* **Trigger**: Runs on each `push` or `pull_request` to the `main` branch.
* **Setup**:

  * Checks out the repo
  * Sets up Python (3.10 or 3.12)
  * Installs all dependencies
* **Pipeline Test**:

  * Executes `make pipeline` to ensure the model trains successfully
* **API Check**:

  * Runs a simple FastAPI server test to validate `/predict` endpoint
* **Artifacts**:

  * Saves the trained model (`house_price_model.joblib`) as a workflow artifact

### 📄 Example Workflow File

```yaml
name: MLOps Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-train:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Run pipeline
        run: |
          source venv/bin/activate
          make pipeline

      - name: Upload model artifact
        uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: house_price_model.joblib
```

---

## 🧪 MLOps Concepts Applied

| Concept                    | Implementation                            |
| -------------------------- | ----------------------------------------- |
| **Reproducibility**        | Virtual environment + pinned dependencies |
| **Automation**             | Makefile for pipeline orchestration       |
| **Continuous Integration** | GitHub Actions workflow                   |
| **Versioning**             | Saved model artifacts                     |
| **Deployment**             | FastAPI REST endpoint                     |
| **Continuous Training**    | `/retrain` endpoint with GridSearchCV     |

---

## 📊 Future Enhancements

* Add automated model evaluation metrics to CI logs
* Include data versioning (DVC)
* Deploy containerized API (Docker + AWS/GCP)
* Integrate monitoring tools (EvidentlyAI, MLflow)

---

## 👩‍💻 Author

**Farah Derbel**
📧 farah.derbel2016@gmail.com


---




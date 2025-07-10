# 🩺 VitalGuard AI: Real-Time Health Monitoring System

## 🚀 Live Demo Links
| Component        | Link                                                                 |
|------------------|----------------------------------------------------------------------|
| 🔌 API Endpoint  | [https://vitalguard-api.onrender.com](https://vitalguard-api.onrender.com) |
| 🖥️ Frontend UI   | [https://vitalguard-ai-insights-28.vercel.app](https://vitalguard-ai-insights-28.vercel.app) |
| 🧾 GitHub Repo   | [https://github.com/richartdo/vitalguard-ai-insights-28](https://github.com/richartdo/vitalguard-ai-insights-28) |
| 📊 Pitch Deck    | [📎 Click here to view the Canva Pitch Deck](#) *(Replace this with your Canva link)* |

---

**VitalGuard AI** is an end-to-end health monitoring system that uses artificial intelligence to detect anomalies in heart rate and blood oxygen levels. Built as a final project for the **AI for Software Engineering** course, it demonstrates the complete AI lifecycle — from data simulation to model training, deployment, and frontend integration.

---

## 📌 Problem Statement

Access to real-time, affordable health monitoring is limited for many individuals, especially in remote or underserved areas. VitalGuard AI provides a solution by:

- Monitoring health data from wearables or manual input  
- Detecting anomalies like abnormal heart rate or oxygen drops  
- Recommending immediate or preventive actions  

---

## 🎯 Project Goals

- Use AI to analyze health data in real-time  
- Build a user-friendly interface for manual data input and insights  
- Deploy the model and API to the cloud  
- Make the solution accessible as a portfolio-ready product  

---

## 🧱 Project Structure

vitalguard-api/
├── app.py # Flask REST API
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
├── models/
│ └── health_anomaly_model.pkl # Trained anomaly detection model
├── .gitignore
└── README.md


---

## 🧪 AI Workflow

1. **Simulated Health Data**
   - Generated random values for `heart_rate` and `blood_oxygen`
   - Used pandas and numpy for simulation

2. **Anomaly Detection Model**
   - Trained an `IsolationForest` model to flag abnormal readings
   - Saved using `joblib`

3. **API Development**
   - Built a RESTful API using Flask with a `/predict` endpoint
   - Enabled CORS to support frontend connection
   - Hosted the API using Render

4. **Frontend Interface**
   - Built a modern interface using [Lovable](https://www.lovable.so)
   - Deployed on [Vercel](https://vercel.com)
   - Connected to the live Flask API using a POST request

---

## ⚙️ Tools & Technologies Used

| Task                    | Tool/Library            |
|-------------------------|-------------------------|
| AI Model                | Scikit-learn (IsolationForest) |
| Data Handling           | Pandas, NumPy           |
| Backend API             | Flask, Flask-CORS       |
| Model Serialization     | Joblib                  |
| Deployment              | Render.com              |
| Frontend UI             | Lovable + Vercel        |
| Model Training          | Google Colab            |
| Version Control         | Git + GitHub            |

---

## 🧠 Sample API Request

**POST** `https://vitalguard-api.onrender.com/predict`

### ✅ Request:
```json
{
  "heart_rate": 90,
  "blood_oxygen": 95
}

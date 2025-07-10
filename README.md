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

## 📈 Project Structure

```bash
vitalguard-api/
├── app.py                      # Flask REST API
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment config
├── models/
│   └── health_anomaly_model.pkl  # Trained anomaly detection model
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
### ✅ Sample Response:

{
  "status": "Normal",
  "recommendation": "Stay active and hydrated."
}

## ✅ Steps Taken

- ✅ Defined the problem and health metrics (heart rate, SpO2)
- ✅ Simulated health data and visualized it in notebooks
- ✅ Built and trained an AI model for anomaly detection
- ✅ Serialized and saved the trained model
- ✅ Created a Flask API to serve predictions
- ✅ Deployed the API on Render
- ✅ Built a frontend UI using Lovable and deployed via Vercel
- ✅ Integrated the UI with the API for real-time predictions
- ✅ Designed a project pitch deck using Canva

---

## 📈 Future Improvements

- Integrate with real wearable device APIs (e.g., Fitbit, Apple Health)
- Add additional health metrics (e.g., sleep, steps, temperature)
- Implement user accounts and data history
- Improve UI styling and responsiveness
- Add multi-language support and chatbot health assistant

---

## 💬 License & Credits

Built by **Brian Richard** as part of the **AI for Software Engineering** course.  
Free to reuse and modify with attribution.

# 🩺 AI-Powered Personal Health Assistant

### 🔗 Live App  
👉 [https://ai-health-assistant-v2rr.onrender.com](https://ai-health-assistant-v2rr.onrender.com)

### 📂 GitHub Repository  
👉 [Repo with initial files hosted by Render.](https://github.com/richartdo/ai-health-assistant.git)

### 📽️ Pitch Deck (Canva)  
👉 [MY PITCH DECK](https://www.canva.com/design/DAGsxyOi9hE/N5nt0GNcXBk13sumfpHgHg/edit?utm_content=DAGsxyOi9hE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### 🎥 Live Demo Video  
👉 [Google Drive Video](https://drive.google.com/file/d/1ZAUzU_XIHi5Xe5aRFSBgyRRHV69FmzNR/view?usp=sharing)  


---

## 🧠 Problem Statement

In regions where access to healthcare professionals may be limited, many individuals struggle with diagnosing symptoms or understanding their potential health conditions. This project provides an **AI-powered personal health assistant** that helps users:

- Select their symptoms from a structured list
- Receive AI-generated diagnosis insights
- Track health conditions over time
- Prompt further action like visiting nearby healthcare facilities

---

## 📊 Dataset Used

**Name:** `Training.csv`  
**Source:** [Kaggle Disease Prediction Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)  
**Description:** The dataset contains 4924 rows with 131 symptoms (as binary columns) and a `prognosis` label indicating the diagnosed condition.

---

## 🧪 Google Colab Development Process

1. **Dataset Loading:**
   - Imported using `pandas` into a DataFrame.
   - Target column: `prognosis`.

2. **Data Preprocessing:**
   - Binary encoding of symptom presence.
   - Label encoding of disease names using `LabelEncoder`.
   - Removal of classes with fewer than 2 samples (for `stratify` compatibility).

3. **Model Training:**
   - Model used: `DecisionTreeClassifier` from `scikit-learn`.
   - 80/20 train/test split using `train_test_split`.

4. **Model Evaluation:**
   - Metrics: Accuracy, classification report, confusion matrix.
   - Accuracy achieved: ~98% (depending on preprocessing).

5. **Model Saving:**
   ```python
   joblib.dump(clf, 'disease_model.pkl')
   joblib.dump(le, 'label_encoder.pkl')
   joblib.dump(symptom_list, 'symptom_list.pkl')

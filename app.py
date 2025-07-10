from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained AI model
model = joblib.load("models/health_anomaly_model.pkl")

@app.route('/')
def home():
    return "✅ VitalGuard AI API is live."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    df = pd.DataFrame([{
        'heart_rate': data['heart_rate'],
        'blood_oxygen': data['blood_oxygen']
    }])

    prediction = model.predict(df)[0]
    result = 'Anomaly' if prediction == -1 else 'Normal'
    recommendation = (
        "Consult a doctor immediately." if result == 'Anomaly'
        else "Stay active and hydrated."
    )

    return jsonify({
        'status': result,
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
 

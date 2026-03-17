from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

# ML Model
model = IsolationForest(contamination=0.1, random_state=42)
scaler = StandardScaler()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 👇 ADD THIS API ENDPOINT HERE 👇
@app.route('/api/analyze')
def analyze_api():
    np.random.seed(42)
    # Generate network data (90 normal + 10 attacks)
    normal = np.random.normal(1000, 200, (90, 5))
    attack = np.random.normal(50000, 10000, (10, 5))
    data = np.vstack([normal, attack])
    
    # ML Detection
    data_scaled = scaler.fit_transform(data)
    predictions = model.fit_predict(data_scaled)
    threat_count = sum(1 for p in predictions if p == -1)
    
    # Create threat details
    threats = []
    for i, p in enumerate(predictions):
        if p == -1:
            threats.append({
                'id': i+1,
                'score': round(np.random.uniform(0.2, 0.9), 2),
                'severity': 'HIGH' if np.random.rand() > 0.5 else 'MEDIUM'
            })
    
    return jsonify({
        'threat_count': threat_count,
        'total_traffic': len(data),
        'threats': threats,
        'timestamp': datetime.now().isoformat()
    })
# 👆 END API CODE 👆

if __name__ == '__main__':
    app.run(debug=True, port=5000)
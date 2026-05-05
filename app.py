from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/analyze')
def analyze_api():
    # Simulate realistic network traffic analysis
    total_traffic = random.randint(800, 1500)
    threat_count = random.randint(8, 25)
    
    # Generate realistic threat data
    threats = []
    for i in range(threat_count):
        threats.append({
            'id': i+1,
            'score': round(random.uniform(0.15, 0.95), 3),
            'severity': random.choice(['CRITICAL', 'HIGH', 'MEDIUM']),
            'ip': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'action': random.choice(['QUARANTINE', 'BLOCK', 'MONITOR', 'ALERT'])
        })
    
    # Simulate ML results
    accuracy = round(random.uniform(91.5, 98.2), 1)
    
    return jsonify({
        'threat_count': threat_count,
        'total_traffic': total_traffic,
        'accuracy': accuracy,
        'threats': threats[:10],  # Show top 10
        'timestamp': datetime.now().isoformat(),
        'status': 'ANALYSIS_COMPLETE'
    })

@app.route('/api/stats')
def stats():
    return jsonify({
        'active_threats': random.randint(3, 12),
        'blocked_ips': random.randint(45, 89),
        'uptime': '99.97%',
        'response_time': f"{random.uniform(0.1, 0.8):.1f}s"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
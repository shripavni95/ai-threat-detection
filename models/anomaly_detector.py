import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AdvancedThreatDetector:
    def __init__(self):
        self.isolation_forest = IsolationForest(contamination=0.08, random_state=42)
        self.scaler = StandardScaler()
        self.feature_names = ['bytes_in', 'bytes_out', 'packets_in', 'packets_out', 
                            'duration', 'src_port', 'dst_port']
    
    def fit(self, X):
        X_scaled = self.scaler.fit_transform(X[self.feature_names])
        self.isolation_forest.fit(X_scaled)
    
    def predict(self, X):
        X_scaled = self.scaler.transform(X[self.feature_names])
        return self.isolation_forest.predict(X_scaled)
    
    def anomaly_scores(self, X):
        X_scaled = self.scaler.transform(X[self.feature_names])
        return self.isolation_forest.decision_function(X_scaled)
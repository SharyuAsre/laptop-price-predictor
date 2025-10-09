import joblib
import pandas as pd
import numpy as np
from pathlib import Path

print("--- Checking Laptop Price Model from models directory ---", flush=True)

# Define model path in models directory
model_path = Path("model") / "laptop_price_model.pkl"

try:
    # Try loading the laptop price model from models directory
    model = joblib.load(model_path)
    print(f"✅ Model loaded successfully from: {model_path}", flush=True)
    
    # Check model type
    print(f"Model type: {type(model)}", flush=True)
    
    # Test with sample data
    sample_data = pd.DataFrame({
        'Company': ['Apple'],
        'TypeName': ['Ultrabook'], 
        'Ram': [16],
        'OpSys': ['Mac'],
        'Weight': [1.37],
        'TouchScreen': [0],
        'IPS': [1], 
        'PPI': [226.98],
        'CPU_name': ['Intel Core i7'],
        'CPU_name1': ['Intel Core i7'],
        'HDD': [0],
        'SSD': [512],
        'Gpu brand': ['Intel']
    })
    
    # Make prediction
    prediction = model.predict(sample_data)
    print(f"✅ Sample prediction: ₹{prediction[0]:,.2f}", flush=True)
    
except FileNotFoundError:
    print(f"❌ Model file not found at: {model_path}", flush=True)
    print("Available files in models directory:", flush=True)
    models_dir = Path("models")
    if models_dir.exists():
        for file in models_dir.iterdir():
            print(f"  - {file.name}", flush=True)
    else:
        print("❌ Models directory does not exist!", flush=True)
    
except Exception as e:
    print(f"❌ Error loading model: {e}", flush=True)

print("Model check completed.", flush=True)

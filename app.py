import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path

# --- Load Model from models directory ---
model_path = Path("model") / "laptop_price_model.pkl"

try:
    model = joblib.load(model_path)
    st.success(f"✅ Model loaded from: {model_path}")
except FileNotFoundError:
    st.error(f"❌ Model not found at: {model_path}")
    st.error("Please check if models/laptop_price_model.pkl exists")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# --- Rest of your Streamlit app code ---
st.title("💻 Laptop Price Predictor")
st.write("Enter laptop specifications to get price prediction")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Specifications")
    
    company = st.selectbox("Company", 
        ['Apple', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Toshiba', 'Samsung'])
    
    type_name = st.selectbox("Type", 
        ['Ultrabook', 'Notebook', 'Gaming', 'Workstation', '2 in 1 Convertible'])
    
    ram = st.selectbox("RAM (GB)", [4, 6, 8, 12, 16, 24, 32, 64])
    
    op_sys = st.selectbox("Operating System", 
        ['Windows', 'Mac', 'Linux', 'Chrome OS', 'Other'])
    
    weight = st.number_input("Weight (kg)", min_value=0.5, max_value=4.0, value=2.0, step=0.1)

with col2:
    st.subheader("Display & Performance")
    
    touchscreen = st.checkbox("Touchscreen")
    ips = st.checkbox("IPS Display")
    ppi = st.number_input("PPI (Pixels Per Inch)", min_value=50, max_value=400, value=150)
    
    cpu_name = st.selectbox("CPU Brand", 
        ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9',
         'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD A6', 'Other'])
    
    cpu_name1 = cpu_name

# Storage section
st.subheader("Storage")
col3, col4, col5 = st.columns(3)

with col3:
    hdd = st.selectbox("HDD (GB)", [0, 500, 1000, 2000])
with col4:
    ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024])
with col5:
    gpu_brand = st.selectbox("GPU Brand", ['Intel', 'AMD', 'Nvidia'])

# --- Prediction Logic ---
if st.button("🚀 Predict Laptop Price"):
    
    # Create input DataFrame
    input_data = pd.DataFrame({
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'OpSys': [op_sys], 
        'Weight': [weight],
        'TouchScreen': [1 if touchscreen else 0],
        'IPS': [1 if ips else 0],
        'PPI': [ppi],
        'CPU_name': [cpu_name],
        'CPU_name1': [cpu_name1],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu brand': [gpu_brand]
    })
    
    try:
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        st.success(f"💰 Predicted Laptop Price: ₹{prediction[0]:,.2f}")
        
        # Additional info
        st.info(f"""
        **Laptop Configuration:**
        - **Brand:** {company} {type_name}
        - **RAM:** {ram}GB | **Storage:** {hdd}GB HDD + {ssd}GB SSD
        - **CPU:** {cpu_name} | **GPU:** {gpu_brand}
        - **Display:** {'Touchscreen' if touchscreen else 'Non-touch'} {'IPS' if ips else 'TN'} ({ppi} PPI)
        - **Weight:** {weight}kg | **OS:** {op_sys}
        """)
        
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

st.markdown("---")
st.markdown("### 📊 Model Information")
st.write("Model loaded from: models/laptop_price_model.pkl")

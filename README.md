# 💻 Laptop Price Predictor

A Machine Learning web app that predicts 
laptop prices based on hardware specifications.

## 🚀 Live Demo
Enter specs → Get instant price prediction!

## ✨ Features
- Predicts price from 13 hardware parameters
- Supports all major brands (Apple, Dell, HP, Lenovo...)
- CPU, GPU, RAM, Storage based prediction
- Clean Streamlit UI with real-time results

## 🛠️ Tech Stack
Python | Scikit-learn | Streamlit | 
Pandas | NumPy | Joblib

## 📁 Project Structure
- notebook/data_preprocessing.ipynb → Data cleaning & EDA
- notebook/model_trainning.ipynb    → Model training
- model/laptop_price_model.pkl      → Saved ML model
- app.py                            → Streamlit web app
- data.py                           → Data utilities

## ⚙️ How to Run
pip install -r requirements.txt
streamlit run app.py

## 📊 Input Parameters
RAM, CPU, GPU, SSD, HDD, 
Display (IPS/Touchscreen/PPI), 
Brand, Type, OS, Weight

from pymongo import MongoClient
import pandas as pd
import os

# -------------------------------
# ⚡ User Configuration
# -------------------------------
MONGO_URI = "mongodb+srv://sharyuasre169_db_user:panda169@cluster0.u4160g.mongodb.net/"  # <-- replace with your URI
DATABASE_NAME = "AIML"       # <-- replace with your DB name
COLLECTION_NAME = "laptop_price"   # <-- replace with your Collection name

# Output CSV file
OUTPUT_PATH = "data/raw_data.csv"

# -------------------------------
# Ensure data folder exists
# -------------------------------
if not os.path.exists("data"):
    os.makedirs("data")

# -------------------------------
# MongoDB Connection & Data Load
# -------------------------------
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    data = list(collection.find())
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Loaded {len(df)} records and saved to {OUTPUT_PATH}")
except Exception as e:
    print(f"❌ Error: {e}")

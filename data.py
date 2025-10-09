from  pymongo import MongoClient
import pandas as pd



MONGO_URI = "mongodb+srv://sharyuasre169_db_user:panda169@cluster0.uysrodh.mongodb.net/"  # <-- replace with your URI
DATABASE_NAME = "aiml"       # <-- replace with your DB name
COLLECTION_NAME = "laptop_price" 

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
data = list(collection.find())
df = pd.DataFrame(data)
#df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Loaded {len(df)} records and saved to {OUTPUT_PATH}")
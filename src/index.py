from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["contract_dev"]  # Substitua pelo nome do seu banco

@app.route("/")
def home():
    count = db.rows.count_documents({})
    return f"Bem-vindo! Documentos na coleção: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
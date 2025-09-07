from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGO_URI:
    raise RuntimeError("A variável de ambiente MONGO_URI não está definida!")

if not DATABASE_NAME:
    raise RuntimeError("A variável de ambiente DATABASE_NAME não está definida!")

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]  # Substitua pelo nome do seu banco

@app.route("/")
def home():
    count = db.rows.count_documents({})
    return f"Bem-vindo! Documentos na coleção: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) 
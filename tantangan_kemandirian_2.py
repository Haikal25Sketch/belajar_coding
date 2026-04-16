"""
TANTANGAN KEMANDIRIAN 2: FULL STACK RAG PIPELINE
Tantangan: Gabungkan semua teknik yang dipelajari:
1. OOP & Inheritance (Class Management)
2. JSON Handling (Persistence)
3. Decorators (Logging & Timing)
4. Generators (Data Processing)
5. API Integration (Embeddings)
6. Math (Cosine Similarity)

Instruksi:
- Buat class sistem RAG yang menyimpan riwayat input dalam file JSON.
- Gunakan decorator untuk mencatat setiap kali query dilakukan.
- Gunakan generator untuk memecah data teks yang panjang sebelum diproses.
"""

import json
import time
import requests
import os
import math
from dotenv import load_dotenv

load_dotenv()

# Decorator untuk mencatat waktu eksekusi
def log_waktu(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"--- Menjalankan fungsi: {func.__name__} ---")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"--- Selesai dalam {end - start:.4f} detik ---")
        return result
    return wrapper

class RAGSystem:
    def __init__(self, db_file="rag_database.json"):
        self.db_file = db_file
        self.data = self._load_db()

    def _load_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {"documents": []}

    def save_document(self, title, content):
        self.data["documents"].append({"title": title, "content": content})
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"Dokumen '{title}' disimpan.")

    # Generator untuk chunking teks
    def chunk_generator(self, text, size=5):
        words = text.split()
        for i in range(0, len(words), size):
            yield " ".join(words[i:i + size])

    @log_waktu
    def get_embedding(self, text):
        token = os.getenv("HUGGINGFACE_TOKEN")
        url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json={"inputs": text})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.text}")
            return None

    def calculate_similarity(self, vec_a, vec_b):
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = math.sqrt(sum(a**2 for a in vec_a))
        mag_b = math.sqrt(sum(b**2 for b in vec_b))
        return dot / (mag_a * mag_b)

def run_system():
    rag = RAGSystem()
    
    # Menambahkan data
    rag.save_document("Info", "Saya belajar pemrograman Python dengan Gemini CLI.")
    
    query = input("Masukkan pertanyaan anda: ")
    
    # Ambil data dari db untuk dibandingkan
    target = rag.data["documents"][0]["content"]
    
    # Ambil embedding
    vec_q = rag.get_embedding(query)
    vec_t = rag.get_embedding(target)
    
    if vec_q and vec_t:
        score = rag.calculate_similarity(vec_q, vec_t)
        print(f"Skor kemiripan: {score:.4f}")
        if score > 0.5:
            print("Jawaban ditemukan: " + target)
        else:
            print("Tidak ditemukan informasi yang relevan.")

if __name__ == "__main__":
    run_system()

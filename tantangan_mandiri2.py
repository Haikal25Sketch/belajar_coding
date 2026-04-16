"""
TANTANGAN MANDIRI 2: INTEGRASI SISTEM RAG
Petunjuk: Isilah bagian yang ditandai dengan [____] untuk melengkapi logika.

Materi yang harus diimplementasikan:
1. Decorator: 'hitung_waktu' untuk mengukur performa fungsi.
2. Dunder Methods: Implementasikan __str__ pada class untuk representasi data.
3. Generators: 'generator_chunks' untuk memecah teks.
4. JSON: Fungsi load dan save data ke file.
5. API & Logic: Implementasi RAG (Embedding + Cosine Similarity).
"""

import json
import time
import requests
import os
import math
from dotenv import load_dotenv

load_dotenv()

# [____] (Buat decorator untuk menghitung waktu eksekusi)
def hitung_waktu(func):
    pass

class RAGManager:
    def __init__(self, filename="data_rag.json"):
        self.filename = filename
        self.data = [] # [____] (Inisialisasi data)

    def save_to_json(self):
        # [____] (Implementasikan penyimpanan ke file JSON)
        pass

    def load_from_json(self):
        # [____] (Implementasikan pemuatan dari file JSON)
        pass

    def __str__(self):
        # [____] (Implementasikan dunder method untuk print objek)
        return "Manager RAG"

    def generator_chunks(self, teks, ukuran=3):
        # [____] (Implementasikan generator untuk memotong teks)
        pass

# [____] (Terapkan decorator di bawah)
def get_embedding(text):
    token = os.getenv("HUGGINGFACE_TOKEN")
    url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
    # [____] (Lakukan request POST dan return embedding)
    pass

def cosine_similarity(vec_a, vec_b):
    # [____] (Implementasikan rumus Cosine Similarity manual)
    pass

def main():
    manager = RAGManager()
    
    # Alur Utama:
    # 1. Input teks dari user
    # 2. Chunking teks menggunakan generator
    # 3. Dapatkan embedding
    # 4. Simpan ke database JSON
    # 5. Uji kemiripan (Cosine Similarity)
    print("--- SISTEM RAG MANDIRI ---")
    
if __name__ == "__main__":
    main()

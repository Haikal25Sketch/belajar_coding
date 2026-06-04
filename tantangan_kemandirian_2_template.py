"""
TANTANGAN KEMANDIRIAN 2: FULL STACK RAG PIPELINE (TEMPLATE)
Instruksi: Isilah bagian yang ditandai dengan # TODO: ...

Materi yang harus diterapkan:
1. OOP: Buat class RAGSystem.
2. JSON: Fungsi simpan & load database.
3. Decorator: Hitung waktu eksekusi.
4. Generator: Chunking teks panjang.
5. API: Request embedding ke HuggingFace.
6. Math: Cosine Similarity manual.
"""

import json
import time
import requests
import os
import math
from dotenv import load_dotenv

load_dotenv()

# TODO: Buat decorator @log_waktu untuk mencatat waktu fungsi

class RAGSystem:
    def __init__(self, db_file="rag_database.json"):
        # TODO: Inisialisasi database (load dari JSON jika ada)
        pass

    def save_document(self, title, content):
        # TODO: Simpan dokumen ke dalam self.data dan tulis ke JSON
        pass

    def chunk_generator(self, text, size=5):
        # TODO: Generator untuk memotong teks per 'size' kata
        pass

    # TODO: Gunakan decorator @log_waktu di sini
    def get_embedding(self, text):
        # TODO: Request ke HuggingFace API untuk mendapatkan embedding
        pass

    def calculate_similarity(self, vec_a, vec_b):
        # TODO: Implementasikan rumus Cosine Similarity manual
        pass

def run_system():
    # TODO: Implementasikan alur utama:
    # 1. Instansiasi RAGSystem
    # 2. Input query dari user
    # 3. Dapatkan embedding query
    # 4. Bandingkan dengan data yang ada
    # 5. Tampilkan hasil
    pass

if __name__ == "__main__":
    run_system()

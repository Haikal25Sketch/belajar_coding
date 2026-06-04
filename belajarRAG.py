# Embeddings : Ringkasan singkat yang bisa dibandingkan,berupa deret(vektor) angka yang mempresentasikan makna dari sebuah teks.

#Contoh
"""
"Saya lapar"      [0.2, 0.8, 0.1, 0.9, ...]
"Perut saya kosong"  [0.21, 0.79, 0.11, 0.88, ...]
"Mobil saya merah"  [0.9, 0.1, 0.7, 0.2, ...]

"""
#Embeddings membaca makna,bukan kata,bisa dilihat bahwa kalimat 1 dan 2 memiliki deret angka yang berdekatan dan itulah yang menjadi acuan kemiripan atar embeddings

"""
Bayangkan alur RAG seperti ini:
Dokumen PDF → dipotong jadi chunks kecil
             → tiap chunk diubah jadi embedding (angka)
             → disimpan di database

User nanya → pertanyaan diubah jadi embedding juga
           → dicari chunk yang embeddingnya PALING MIRIP
           → chunk itu dikasih ke AI sebagai konteks
           → AI jawab berdasarkan konteks itu

jika embeddings tidak ada,maka pencarian tidak dapat dilakukan,toh buang buang waktu doang.

Ini sebabnya haikal diharuskan kembali ke Embeddings dulu baru masuk ke RAG ,karena RAG bergantung penuh pada Embeddings untuk bisa bekerja

JADI SABAR YAA
"""

"""
COSINE SIMILARITY

Cara komputer mengukur kemiripan vector di dunia embeddings,

"Saya lapar"      [0.2, 0.8, 0.1, 0.9, ...]
"Perut saya kosong"  [0.21, 0.79, 0.11, 0.88, ...]
"Mobil saya merah"  [0.9, 0.1, 0.7, 0.2, ...]

Bisa dilihat contoh kalimat pertama dan kedua,keduanya memilki angka yang saling berdekatan. 0.2 dengan 0.21 0.8 dengan 0.79 dst.

1= sama persis
0= jauh beda
0.= hampir mirip
Contoh nyata:
"""
import requests
import os
from dotenv import load_dotenv
import math
import logging

load_dotenv() #-> mengambil data .env

token = os.getenv("HUGGINGFACE_TOKEN")

headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}

data = {
    "inputs":[ "I am Hungry",
               "I want to eat",
               "My stomatch is empty",
               "I am sewing"
             ]
}

url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"

response = requests.post(url, headers=headers,json = data)

if response.status_code == 200:
    embeddings = response.json()
    

print ("===Membandingkan Embeddings===")

def cosine_similarity(a, b):
    dot = sum(x*y for x, y in zip(a, b)) #zip: menggabungkan list menjadi 1 pasangan,
    mag_a = math.sqrt(sum(x**2 for x in a)) #-> jumlahkan dulu hasil dari pangkatnya berapa,lalu hasilnya diakar kuadratkan
    mag_b = math.sqrt(sum(x**2 for x in b))
    return dot / (mag_a * mag_b)

print ("HASIL EMBEDDING LAPAR DAN MAKAN ADALAH : ",round(cosine_similarity(embeddings[0],embeddings[1]),2))

print ("HASIL EMBEDDING LAPAR DAN PERUT KOSONG ADALAH : ",round(cosine_similarity(embeddings[0],embeddings[2]),2))

print ("HASIL EMBEDDING LAPAR DAN MENJAHIT : ",round(cosine_similarity(embeddings[0],embeddings[3]),2))

print ("HASIL EMBEDDING LAPAR DAN LAPAR : ",round(cosine_similarity(embeddings[0],embeddings[0]),2))
# INI SEMUA ADALAH PERMULAAN UNTUK RAG,RAG ASLI DATANYA BUKAN MANUAL ATAUPUN INPUT USER,BISA DARI :
#-FILE PDF
#-FILE TXT
#-WEBSITE
#-DATABASE

"""
RAG YANG AKAN DIBABGUN:
1. Punya dokumen teks (data/pengetahuan)
2. Potong jadi chunks kecil
3. Ubah tiap chunk jadi embedding
4. Simpan chunks + embeddingnya

5. User nanya
6. Ubah pertanyaan jadi embedding
7. Cari chunk yang paling mirip
8. Kasih chunk itu ke Groq AI
9. Groq jawab berdasarkan chunk itu

Gw udah sedikit memahami 3,5,6,7
"""

"""MEMBANGUN RAG STEP BY STEP"""
# Di belajarGroq.py gw mengirim pesan ke Groq dengan format
"""
messages = [    {"role": "system", "content": "kamu adalah assistent yang membantuku untuk membandingkan kecantikan karakter fiksi."}]
"""
#Di RAG kita akan menambahkan sesuatu di bagian "contentnya" yaitu data
"""
messages = [
    {"role": "system", "content": f"Berdasarkan data ini {data.pdf} jawab pertanyaan ini {input_user}"}]
"""





import requests
import os
from dotenv import load_dotenv
import math
print ("BELAJAR EMBEDDINGS")
#Embeddings : cara komputer nyimpen kata/kalimat sebagai angka yang punya makna.Bukan biner biasa — tapi list angka yang merepresentasikan artinya:
#"kucing" = [0.2, 0.8, 0.1, 0.9, ...]
#"anjing" = [0.2, 0.7, 0.1, 0.8, ...]  # mirip kucing!
#"mobil"  = [0.9, 0.1, 0.8, 0.2, ...]  # beda jauh!

# Cara komputer mengetahui kemiripan seperti anjing dengan kucing adalah dengan methode SIMILARITY,yaitu mengukur seberapa mirip kedua embeddings

# COSINE SIMILARITY adalah pengukuran yang populer dilakukan
#Hasilnya antara 0 sampai 1:
#0.9 → sangat mirip
#0.5 → agak mirip
#0.1 → sangat beda

"""Fungsi Embeddings"""
#Mencari hubungan dan makna antar kata/kalimat

#RAG = Retrieval Augmented Generation
#intinya adalah "Sebelum AI jawab, dia nyari dulu informasi yang relevan(bisa dari data yang kita beri), baru jawab berdasarkan info itu"

#Jadi RAG itu solusi untuk 2 masalah:
#1. AI ga tau data spesifik kamu (dokumen perusahaan, database, dll)
#2. AI ga tau informasi terbaru (hanya tau info terakhir dia knowledge cutoff)

#Cara RAG menggunakan embeddings:
#1. Dokumen dipecah jadi potongan kecil
#2. Tiap potongan → diubah jadi embedding → disimpan
#3. User tanya sesuatu → pertanyaan → diubah jadi embedding
#4. Bandingkan embedding pertanyaan vs semua embedding dokumen
#5. Ambil yang paling mirip
#6. Kasih ke AI → "jawab berdasarkan ini!"
#7. AI jawab dengan akurat
"""CONTOH

Contoh nyata:
Dokumen: "Kebijakan cuti 12 hari per tahun"
User tanya: "Berapa hari cuti saya?"

Embedding "cuti saya" ≈ embedding "kebijakan cuti"
→ dokumen relevan ditemukan!
→ AI jawab: "12 hari per tahun"
"""
#cara mendapatkan embeddings dari sebuah kalimat:
#User kirim klimat ke API -> API mengembalikan list angka,contoh

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}

data = {
    "inputs":[ "aku suka hutao",
               "rizal suka yaemiko",
               "fajri suka nahida",
               "pizza"
             ]
}

url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
response = requests.post(url, headers=headers,json = data)

print (response.status_code)
if response.status_code == 200:
    embeddings = response.json()
    print ("EMBEDDINGS BERHASIL DIDAPATKAN!")
    print (f"Dimensi tiap kalimat = {len(embeddings[0])}")
    print ("jumlah kalimat = ",len(embeddings))
else:
    print (f"Error {response.status_code}: {response.text}")

print()
"""Membandingkan Embedding dengan math,device gw ga bisa sklearn anjir"""
print ("===Membandingkan Embeddings===")

def cosine_similarity(a, b):
    dot = sum(x*y for x, y in zip(a, b)) #zip: menggabungkan list menjadi 1 pasangan,
    mag_a = math.sqrt(sum(x**2 for x in a)) #-> jumlahkan dulu hasil dari pangkatnya berapa,lalu hasilnya diakar kuadratkan
    mag_b = math.sqrt(sum(x**2 for x in b))
    return dot / (mag_a * mag_b)


print ("HuTao vs Yaemiko",round(cosine_similarity(embeddings[0],embeddings[1]),3)) #0.538 -> mirip
print ("Yaemiko vs Nahida",round(cosine_similarity(embeddings[1],embeddings[2]),3)) #0.566 -> sedikit lebih mirip
print ("HuTao vs Pizza",round(cosine_similarity(embeddings[0],embeddings[3]),3)) #0.161 -> jauh beda
print ("HuTao vs HuTao",round(cosine_similarity(embeddings[0],embeddings[0]),3)) #1.0

print()
print ("HuTao vs Yaemiko",cosine_similarity(embeddings[0],embeddings[1])) #0.538 -> mirip

print()
print (embeddings[0])

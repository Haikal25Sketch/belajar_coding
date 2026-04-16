"""
TANTANGAN MANDIRI: MENGUASAI DASAR HINGGA RAG
File ini dirancang untuk menguji pemahaman Anda tentang semua materi di folder belajarclass.
Isilah bagian yang kosong sesuai instruksi.

TOPIK:
1. Dunder Methods & OOP (Inheritance/Polymorphism)
2. Decorators
3. Generators (yield)
4. JSON Handling
5. API Request & Logic RAG (Cosine Similarity)
"""

import json
import math
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. DECORATOR & LOGGING
# Buatlah decorator 'hitung_waktu' untuk mencatat 
# berapa lama sebuah fungsi dijalankan.
# ==========================================

def hitung_waktu(func):
    def wrapper(*args, **kwargs):
        # TULIS KODE DISINI (Gunakan time.time())
        print ("MULAI")
        start = time.time()
        result = func(*args,**kwargs)
        print ("SELESAI")
        stop = time.time()
        selisih = stop - start
        print ("WAKTU KODE BERJALAN ADALAH : ",selisih)
        return result
    return wrapper

@hitung_waktu
def sapa(nama):
    print (f"Hai {nama},aku suka kamu")

sapa("Sephia")
print()
# ==========================================
# 2. DUNDER & OOP
# Buat class 'Dokumen' sebagai base class, 
# lalu 'Chunk' sebagai child class (Inheritance).
# ==========================================

class Dokumen:
    def __init__(self, judul, konten):
        self.judul = judul
        self.konten = konten

    def __str__(self):
        # Kembalikan string: "[Judul] - Konten..."
        return f"[{self.judul}] - {self.konten[:20]}..."

class Chunk(Dokumen):
    def __init__(self, judul, konten, embedding=None):
        super().__init__(judul, konten)
        self.embedding = embedding

    def __len__(self):
        # Gunakan dunder len untuk menghitung jumlah kata di konten
        return len(self.konten.split())

# ==========================================
# 3. GENERATORS (yield)
# Buat generator untuk memotong teks panjang 
# menjadi chunks kecil (simulasi RAG).
# ==========================================

def potong_teks(teks,ukuran=2):
    kata = teks.split()
    # TULIS KODE DISINI (Gunakan yield untuk mengembalikan list kata per ukuran_chunk)
    for i in range(0,len(kata),ukuran):
        potongan = kata[i:i+ukuran]
        yield potongan
        
for kata in  potong_teks("Aku mencintai Nahida dan HuTao karena mereka imut"):
    print (kata)


# ==========================================
# 4. MATH LOGIC (Cosine Similarity)
# Hitung kemiripan dua vektor secara manual.
# ==========================================
print()

def manual_cosine_similarity(vec_a, vec_b):
    if not vec_a or not vec_b: return 0
    else:
        dot = sum(x*y for x,y in zip(vec_a,vec_b))
        mag_a = math.sqrt(sum(x**2 for x in vec_a))
        mag_b = math.sqrt(sum(x**2 for x in vec_b))
    # TULIS KODE DISINI
    return dot / (mag_a * mag_b)
vector_a = [0.9,0,8,0.3,0.6]
vector_b = [0.3,0.31,0.99,0.76]
hasil = manual_cosine_similarity(vector_a,vector_b)
print ("Hasil dari kemiripan vector a dan b adalah : ",round(hasil,3))

print()

# ==========================================
# 5. INTEGRASI (MAIN CHALLENGE)
# =========================================



class user:
    def __init__(self,name,hobby):
        self.name = name
        self.hobby = hobby
        self.data = []
    def save (self,location):
        data = {
            "name":self.name,
            "hobby":self.hobby,
            "data":self.data
            }
            
        with open(location,"w") as f:
            json.dump(data,f,indent = 4)

    def load (self,location):
        self.name = None
        self.hobby = None
        self.data = None
        try:
            with open(location,"r") as f:
                data = json.load(f)
                self.name = data["name"]
                self.hobby = data["hobby"]
                self.data = data["data"]
        except FileNotFoundError as e:
            print ("FILE TIDAK ADA : ",e)

        except json.JSONDecodeError as e:
            print ("FILE RUSAK : ",e)

        except KeyError as e:
            print ("KEY TIDAK ADA : ",e)

    def add_data(self,*args):
        self.data.extend([args])

user_1 = user("HuTao","Mengubur Mayat")
user_1.add_data("AKU MENCINTAI HAIKAL","AKU MERINDUKAN HAIKAL")
user_1.save("User.json")

def jalankan_tantangan(location):
    # A. JSON LOAD: Ambil data dari 'anak.json' atau buat manual jika tidak ada
    try:
        with open(location, "r") as f:
            data_json = json.load(f)
    except:
        data_json = {"nama": "User", "hobi": "Belajar Python"}

    print(f"--- Selamat Datang {data_json.get('name')} ---")

    # B. API & RAG:
    # 1. Ambil input dari user.
    # 2. Gunakan HuggingFace API untuk mendapatkan embedding dari input user.
    # 3. Bandingkan dengan embedding dummy atau data yang ada.
    with open("User.json","r") as f:
        data_json = json.load(f)
    kalimat = input("Masukkan Kalimat : ")

    token = os.getenv("HUGGINGFACE_TOKEN")

    url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"

    headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
    }

    # Ambil kalimat pertama dari list data untuk dibandingkan
    target_kalimat = data_json["data"][0][0]
    payload = {"inputs":[kalimat, target_kalimat]}

    if not token:
        print("Error: HUGGINGFACE_TOKEN tidak ditemukan di .env")
        return
    else:
        response = requests.post(url,headers=headers,json = payload)
        if response.status_code == 200:
            embeddings = response.json()
            print ("MEMBANDINGKAN EMBEDDINGS")
            lanjut = input("ENTER UNTUK LANJUT...")
            vec_a = embeddings[0]
            vec_b = embeddings[1]
            hasil = manual_cosine_similarity(vec_a,vec_b)
            print (f"Hasil perbandingan antara class {user_1.__class__.__name__} dengan input user adalah : { round(hasil,3)}")
            print (f"Target kalimat: {target_kalimat}")
    # TULIS LOGIC RAG SEDERHANA ANDA DI SINI
    # - Ambil input()
    # - Kirim requests.post ke HuggingFace
    # - Gunakan manual_cosine_similarity
 
    print("\n[Tantangan Selesai]")

if __name__ == "__main__":
    jalankan_tantangan("User.json")


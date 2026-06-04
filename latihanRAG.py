import requests
import os
from dotenv import load_dotenv
import logging
import math

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    terminal_handler = logging.StreamHandler()
    terminal_handler.setLevel(logging.DEBUG)

    stream_fmt = logging.Formatter("%(levelname)s |  %(message)s")
    terminal_handler.setFormatter(stream_fmt)

    logger.addHandler(terminal_handler)
    return logger

logger = setup_logging()

def get_embeddings(data_list):
    if not data_list:
        logger.error("Data tidak boleh kosong")
        raise ValueError ("Data tidak boleh kosong")

    logger.info("Melakukan pengambilan Embeddings")
    token = os.getenv("HUGGINGFACE_TOKEN")

    url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction" 

    headers = {
        "Authorization":f"Bearer {token}",
        "Content-Type":"application/json"
    }

    data={"inputs":data_list}

    try:
        # Menambahkan timeout agar program tidak gantung jika koneksi lambat
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        if response.status_code == 200:
            logger.info("Koneksi ke API berhasil")
            logger.info("Embeddings berhasil didapatkan")
            return response.json()
        elif response.status_code == 429:
            logger.error("ERROR: Rate limit tercapai. Silakan tunggu sebentar.")
            return None
        else:
            logger.error(f"Koneksi ke API gagal: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        logger.error("ERROR: Waktu permintaan habis (Timeout). Periksa koneksi internet.")
        return None
    except requests.exceptions.ConnectionError:
        logger.error("ERROR: Gagal terhubung ke server. Periksa jaringan internet.")
        return None
    except Exception as e:
        logger.error(f"ERROR TIDAK TERDUGA: {e}")
        return None

def pembanding (vector_a,vector_b):
    dot = sum(x*y for x,y in zip(vector_a,vector_b))
    mag_a = math.sqrt(sum(x**2 for x in vector_a))
    mag_b = math.sqrt(sum(x**2 for x in vector_b))
    return dot / (mag_a * mag_b)

load_dotenv()

data =[
        "Saya suka makan nasi",
        "Nasi goreng enak sekali",
        "Saya hobi bermain bola",
        "Sepak bola olahraga populer",
        "Saya lapar ingin makan"
]

try:
    embeddings_awal = get_embeddings(data)
except Exception as e:
    logger.error(f"Gagal memproses data awal: {e}")
    embeddings_awal = None

print(f"Embeddings awal: {embeddings_awal}")

if embeddings_awal:
    user_input = input("Masukkan kalimat : ")

    user_embeddings = get_embeddings([user_input])[0] #->[0] untuk unpack

    higher = 0
    best =""
    for i,emb in enumerate(embeddings_awal):
        skor = pembanding(emb,user_embeddings)
        if skor > higher :
            higher = skor 
            best = data[i]
    print (f"Kalimat termirip adalah {best} dengan skor kemiripan {higher} ")

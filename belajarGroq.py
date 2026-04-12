import requests
import os
from dotenv import load_dotenv

# 1. Load API Key dari file .env
load_dotenv()
token = os.getenv("GROQ_API_KEY")

# 2. Header untuk autentikasi ke API Groq
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# 3. Inisialisasi daftar pesan (HISTORY)
# Kita mulai dengan pesan 'system' untuk mengatur kepribadian AI
messages = [
    {"role": "system", "content": "kamu adalah assistent yang membantuku untuk membandingkan kecantikan karakter fiksi."}
]

print("=== Chat Interaktif Groq (Ketik 'exit' untuk berhenti) ===")

# 4. LOOP Utama agar bisa chatting terus menerus
while True:
    # Ambil input dari kamu
    user_input = input("Kamu: ")

    # Cek jika kamu ingin berhenti
    if user_input.lower() in ["exit", "keluar", "quit"]:
        print("Sampai jumpa!")
        break

    # MASUKKAN pesan kamu ke dalam history (Role: user)
    messages.append({"role": "user", "content": user_input})

    # 5. Siapkan payload data dengan SELURUH history pesan
    # AI butuh history lengkap supaya dia ingat apa yang diomongin sebelumnya
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages
    }

    # 6. Kirim Request ke API Groq
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )

        # Cek apakah request berhasil
        if response.status_code == 200:
            data = response.json()
            # Ambil teks jawaban AI
            balasan_ai = data["choices"][0]["message"]["content"]
            
            print(f"AI: {balasan_ai}")
            print("-" * 30) # Garis pembatas biar rapi

            # 7. PENTING: Masukkan balasan AI ke history (Role: assistant)
            # Tanpa ini, AI bakal lupa apa yang baru saja dia katakan
            messages.append({"role": "assistant", "content": balasan_ai})
            
        else:
            print(f"Error dari API: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Terjadi kesalahan koneksi: {e}")

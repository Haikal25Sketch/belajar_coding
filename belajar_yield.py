import random
import time

# --- 1. Generator Data (Simulasi Dataset Besar) ---
def sensor_stream_generator(limit=100):
    """
    Simulasi sensor yang mengirimkan data terus menerus.
    Alih-alih menyimpan 100 data di list, kita 'yield' satu per satu.
    """
    for i in range(limit):
        # Simulasi data suhu (antara 20.0 sampai 35.0 derajat)
        suhu = round(random.uniform(20.0, 35.0), 2)
        
        # 'yield' menghentikan fungsi sementara dan mengirimkan data ke luar
        yield {"id": i, "suhu": suhu, "timestamp": time.time()}

# --- 2. Fungsi Preprocessing (Data Cleaning) ---
def clean_data_generator(data_stream):
    """
    Menerima generator, memprosesnya, dan 'yield' hasilnya kembali.
    Hanya mengirimkan data yang suhunya di atas 25 derajat (Filtering).
    """
    for data in data_stream:
        if data["suhu"] > 25.0:
            # Kita hanya ambil nilai suhunya saja
            yield data["suhu"]

# --- 3. Training Loop Sederhana (Simulasi AI) ---
def train_simple_model():
    print("--- Memulai Proses Data AI (Pure Python) ---")
    
    # Inisialisasi generator
    raw_data = sensor_stream_generator(limit=20)
    cleaned_data = clean_data_generator(raw_data)
    
    total_suhu = 0
    count = 0
    
    # Kita melakukan iterasi pada generator 'cleaned_data'
    # Data baru benar-benar diproses DI SINI (Lazy Evaluation)
    for suhu in cleaned_data:
        total_suhu += suhu
        count += 1
        print(f"Memproses data ke-{count}: Suhu {suhu}°C (Diterima)")
        time.sleep(0.1) # Simulasi waktu komputasi

    if count > 0:
        rata_rata = total_suhu / count
        print(f"\n--- Hasil Analisis AI ---")
        print(f"Total data diproses: {count}")
        print(f"Rata-rata suhu: {rata_rata:.2f}°C")

# Jalankan program
if __name__ == "__main__":
    train_simple_model()

'''
CONTOH PENGGUNAAN DESCRIPTOR DALAM AI ENGINEERING
------------------------------------------------
Descriptor sangat berguna untuk:
1. Validasi Hyperparameter (Learning Rate, Batch Size, Epochs)
2. Validasi Struktur Data (Dimensi Embedding, Tipe Data Tensor)
3. Logging otomatis saat parameter berubah

Pendekatan ini membuat sistem AI lebih "Robust" (kokoh) seperti di Robust_pipeline.py
'''

import math

# 1. Descriptor untuk Hyperparameter
class Hyperparameter:
    def __init__(self, name, min_val=None, max_val=None, type_expected=float):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val
        self.type_expected = type_expected

    def __set_name__(self, owner, name):
        self.internal_name = f"_{name}"

    def __set__(self, instance, value):
        # Validasi Tipe
        if not isinstance(value, self.type_expected):
            raise TypeError(f"[ERROR] {self.name} harus bertipe {self.type_expected.__name__}")
        
        # Validasi Range
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"[ERROR] {self.name} minimal {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"[ERROR] {self.name} maksimal {self.max_val}")
        
        print(f"[LOG] {self.name} diatur ke: {value}")
        instance.__dict__[self.internal_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.internal_name)

# 2. Descriptor untuk Embedding (Validasi Dimensi)
class EmbeddingValidator:
    def __init__(self, expected_dim):
        self.expected_dim = expected_dim

    def __set_name__(self, owner, name):
        self.internal_name = f"_{name}"

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("[ERROR] Embedding harus berupa list angka")
        
        if len(value) != self.expected_dim:
            raise ValueError(f"[ERROR] Dimensi embedding salah! Diharapkan {self.expected_dim}, didapat {len(value)}")
        
        instance.__dict__[self.internal_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.internal_name)

# 3. Class Model AI yang menggunakan Descriptor
class AIModelConfig:
    # Menggunakan Descriptor untuk validasi otomatis
    learning_rate = Hyperparameter("Learning Rate", min_val=0.0, max_val=1.0)
    batch_size = Hyperparameter("Batch Size", min_val=1, type_expected=int)
    embedding_vector = EmbeddingValidator(expected_dim=3) # Contoh dimensi kecil (x, y, z)

    def __init__(self, lr, batch, emb):
        self.learning_rate = lr
        self.batch_size = batch
        self.embedding_vector = emb

# --- PENGGUNAAN ---

print("=== Skenario 1: Konfigurasi Valid ===")
try:
    config = AIModelConfig(lr=0.001, batch=32, emb=[0.1, 0.5, 0.9])
    print("Konfigurasi Berhasil!")
except Exception as e:
    print(e)

print("\n=== Skenario 2: Validasi Learning Rate (Terlalu Besar) ===")
try:
    config.learning_rate = 1.5 # Akan memicu ValueError
except Exception as e:
    print(e)

print("\n=== Skenario 3: Validasi Batch Size (Salah Tipe) ===")
try:
    config.batch_size = "32" # Akan memicu TypeError
except Exception as e:
    print(e)

print("\n=== Skenario 4: Validasi Dimensi Embedding ===")
try:
    # Meniru data dari belajar_Embeddings.py tapi dimensinya salah
    config.embedding_vector = [0.1, 0.2] # Diharapkan 3
except Exception as e:
    print(e)

print("\n=== Skenario 5: Akses Data ===")
print(f"Learning Rate saat ini: {config.learning_rate}")

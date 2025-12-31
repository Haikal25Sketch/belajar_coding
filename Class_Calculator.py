
import math
from abc import ABC, abstractmethod
import os,sys
import json
# ==========================================================
#                      CLASS UTAMA
# ==========================================================
def clear_screen():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')


class Kalkulator:
    def __init__(self):
        self.file_riwayat = "riwayat_biasa.json"
        self.riwayat = self.load_riwayat()

    def load_riwayat(self):
      """memuat riwayat dari file JSON."""
      if os.path.exists(self.file_riwayat):
        try:
          with open(self.file_riwayat,'r') as f:
            content = f.read()
            if content:
              data = json.loads(content) # parse
              print (f"[INFO] Berhasil memuat {len(data)} riwayat dari {self.file_riwayat}")
              return data
            return []
        except(json.JSONDecodeError, FileNotFoundError) as e :
          print(f"[WARNING] Error saat memuat riwayat : {e}")
          return[]
      return[]

    def save_riwayat(self):
      """Mwnyimpan riwayat ke file JSON"""
      try:
        with open(self.file_riwayat,'w') as f :
          json.dump(self.riwayat,f,indent=4)
        print(f"[INFO] Riwayat disimpan ke {self.file_riwayat}")
      except Exception as e :
        print (f"[ERROR] Gagal menyimpan riwayat :{e}")
        

    def get_input(self):
        '''method untuk mendapatkan input dari user'''
        try:
            num_1 = float(input("Masukkan Angka Pertama : "))
            operator = input("Masukkan pilihan operasi:\n1.PENJUMLAHAN\n2.PENGURANGAN\n3.PERKALIAN\n4.PEMBAGIAN\n: ")
            num_2 = float(input("Masukkan Angka Kedua : "))
            return num_1, operator, num_2
        except ValueError:
            print("Error: Input harus Angka")
            return None, None, None

    # untuk tambah
    def tambah(self, a, b):
        return a + b

    # untuk kurang
    def kurang(self, a, b):
        return a - b

    # untuk bagi
    def bagi(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Tidak bisa dibagi 0")
        return a / b

    # untuk kali
    def kali(self, a, b):
        return a * b

    def hitung(self):
        '''method utama untuk menghitung'''
        num_1, operator, num_2 = self.get_input()
        
        if num_1 is None:
            return

        try:
            if operator == '1':
                hasil = self.tambah(num_1, num_2)
            elif operator == '2':
                hasil = self.kurang(num_1, num_2)
            elif operator == '3':
                hasil = self.kali(num_1, num_2)
            elif operator == '4':
                hasil = self.bagi(num_1, num_2)
            else:
                print("Operasi Tidak Valid")
           
            simbol_map ={'1':'+','2':'-','3':'x','4':'/'}
            simbol = simbol_map.get(operator,'?')

            operation = f"{num_1} {simbol} {num_2} = {hasil}"
            self.riwayat.append(operation)

            print(f"Hasil = {hasil}")

            # Simpan riwayat setiap kali selesai menghitung
            self.save_riwayat()
            

        except Exception as e:
            print(f"Error: {e}")

    def tampilkan_history(self):
        '''menampilkan riwayat perhitungan'''
        print("===== RIWAYAT PERHITUNGAN =====")
        if not self.riwayat:
          print ("Belum ada perhitungan")
        else:
          for i,riwayat in enumerate(self.riwayat,1):
            print (f"{i}. {riwayat}")
            

# ==========================================================
#      IMPLEMENTASI 4 Pilar OOP ======================
# 1. Inheritance & Polymorphism --- Buat Class Turunan
# ==========================================================
class KalkulatorScientific(Kalkulator): # Inheritance
    def __init__(self): 
        super().__init__() # panggil constructor parent
        self.nama = "kalkulator scientific"
        self.file_riwayat = "riwayat_scientific.json" #file khusus untuk scientific
        self.riwayat = self.load_riwayat()

    def get_input(self): # override method get_input
        '''method untuk mendapatkan input dari user'''
        try:
            num_1 = float(input("Masukkan Angka Pertama : "))
            operator = input("Masukkan pilihan operasi:\n1.PENJUMLAHAN\n2.PENGURANGAN\n3.PERKALIAN\n4.PEMBAGIAN\n5.PANGKAT\n6.AKAR\n: ")
            if operator in ['1', '2', '3', '4', '5']:
                num_2 = float(input("Masukkan Angka Kedua : "))
            else:
                num_2 = None # Untuk operasi akar, num_2 tidak diperlukan
            return num_1, operator, num_2
        except ValueError:
            print("Error: Input harus Angka")
            return None, None, None

    # Method tambahan untuk kalkulator scientific
    def pangkat(self, a, b):
        return a ** b

    def akar(self, a):
        return math.sqrt(a)

    def hitung(self): # override method hitung
        '''method utama untuk menghitung...'''
        num_1, operator, num_2 = self.get_input()

        if num_1 is None:
            return

        try:
            if operator == '1':
                hasil = self.tambah(num_1, num_2)
            elif operator == '2':
                hasil = self.kurang(num_1, num_2)
            elif operator == '3':
                hasil = self.kali(num_1, num_2)
            elif operator == '4':
                hasil = self.bagi(num_1, num_2)
            elif operator == '5': 
                hasil = self.pangkat(num_1, num_2)
            elif operator == '6':
                hasil = self.akar(num_1)
            else:
                print("Operasi Tidak Valid")
                return
            simbol_map ={'1':'+','2':'-','3':'x','4':'/','5':'**'}
            simbol = simbol_map.get(operator,'?')

            # Menyesuaikan format string operasi untuk kasus akar
            if operator == '6':
                operation = f"akar({num_1}) = {hasil}"
            else:
                operation = f"{num_1} {simbol} {num_2} = {hasil}"
            
            self.riwayat.append(operation)

            print(f"Hasil = {hasil}")

            #simpan riwayat
            self.save_riwayat()
            
        except Exception as e:
            print(f"Error: {e}")
    def tampilkan_history(self):
      '''menampilkan riwayat perhitungan'''
      print ("===== RIWAYAT SCIENTIFIC ====")
      if not self.riwayat:
        print ("Belum ada perhitungan")
      else:
        for i,riwayat in enumerate(self.riwayat,1):
          print(f"{i}. {riwayat}")
      
# ==========================================================
# 2. Abstraction --- Buat kerangka/template abstrac untuk kontrak
# ==========================================================
class TemplateKalkulator(ABC):
    @abstractmethod
    def hitung(self):
        pass
    
    @abstractmethod
    def tampilkan_history(self):
        pass

# ==========================================================
# 3. Encapsulation (sudah diterapkan dengan __riwayat)
# 4. Polymorphism (diterapkan di program utama)
# ==========================================================
# Implementasi Abstract Class
class KalkulatorBasic(TemplateKalkulator): # Inheritance dari Abstract
    def __init__(self):
        self.file_riwayat ="riwayat_basic.json"
        self.riwayat = self.load_riwayat()

    def load_riwayat(self):
        """Memuat riwayat dari file JSON."""
        if os.path.exists(self.file_riwayat):
          try:
            with open(self.file_riwayat,'r') as f:
              content = f.read()
              if content:
                data =json.loads(content)
                print(f"[INFO] Berhasil memuat {len(data)} riwayat dari {self.file_riwayat}")
                return data
              return []
          except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"[WARNING] Error saat memuat riwayat: {e}")
            return []
        return []

    def save_riwayat(self):
        """Menyimpan riwayat ke file JSON."""
        try:
            with open(self.file_riwayat, 'w') as f:
                json.dump(self.riwayat, f, indent=4)
            print(f"[INFO] Riwayat disimpan ke {self.file_riwayat}")
        except Exception as e:
            print(f"[ERROR] Gagal menyimpan riwayat: {e}")

    def hitung(self): # #Polymorphism - implementasi konkrit
        '''implementasi sederhana'''
        try:
            angka_1 = float(input("Angka Pertama : "))
            angka_2 = float(input("Angka Kedua : "))
            hasil = angka_1 + angka_2 # Logika yang hilang: hitung hasil terlebih dahulu
            print("--- HANYA PENJUMLAHAN ---")
            self.riwayat.append(f"{angka_1} + {angka_2} = {hasil}")
            print(f"Hasil Tambah = {hasil}")

            #simpan riwayat
            self.save_riwayat()
            
        except:
            print("Error")
            
    def tampilkan_history(self): # Method yang wajib ada dari abstract class
        print("===== RIWAYAT BASIC =====")
        if not self.riwayat:
          print ("Belum ada perhitungan")
        else:
          for i, riwayat in enumerate(self.riwayat, 1):
            print(f"{i}. {riwayat}")

# ==========================================================
# ===================== PROGRAM UTAMA ======================
# ==========================================================

if __name__ == "__main__":

    # ---- Demonstrasi Polimorfisme ---- Different forms same interface
    while True:
      clear_screen()
      kalkulator_list = [
            Kalkulator(),
            KalkulatorScientific(),
            KalkulatorBasic()
        ]

      print("PILIH JENIS KALKULATOR")
      print("1. KALKULATOR BIASA")
      print("2. KALKULATOR SCIENTIFIC")
      print("3. KALKULATOR SEDERHANA")
        
      try:
          pilihan_kalkulator = input("Pilih Kalkulator(1-3): ")
          calc = kalkulator_list[int(pilihan_kalkulator)-1]
      except:
          print("Pilihan tidak valid, menggunakan kalkulator biasa.")
          calc = Kalkulator() # Default jika input salah

      while True:
            clear_screen()
            print("\n" + "="*25)
            print("PROGRAM SEDERHANA CLASS CALCULATOR")
            print("SILAHKAN PILIH OPSINYA!!!")
            print("1. MENGHITUNG")
            print("2. LIHAT RIWAYAT")
            print("3. GANTI")
            print("4. KELUAR")

            pilih = input("SILAHKAN MASUKKAN OPSI : ")

            if pilih == '1':
                clear_screen()
                calc.hitung()
            elif pilih == '2':
                clear_screen()
                calc.tampilkan_history()
            elif pilih == '3':
              break

            elif pilih =='4' :
             sys. exit()
            
            else:
                print("PILIHAN TIDAK VALID")

            lanjut = input('Lanjut atau Tidak (y/n) : ')
            if lanjut == 'n':
              print("TERIMA KASIH")
              break






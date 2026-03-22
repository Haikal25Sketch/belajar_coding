'''Belajar JSON'''
import json
"""JSON :
 format menyimpan data dalam bentuk teks terstruktur.
Mirip dictionary Python, tapi disimpan di file.
"""
#Contoh Json
{
  "nama": "Haikal",
  "saldo": 12000,
  "riwayat": [
    "Setor 2000",
    "Tarik 500"
  ]
}

#Alasan json sering dipakai:
"""
•mudah dibaca manusia
•ringan
•hampir semua bahasa pemrograman bisa memakainya
•sering dipakai untuk API dan data exchange
"""

"""
Secara sederhana:
Python object -> JSON file :

Object python yaitu seperti list int dict dan semacamnya diubah jadi format json lalu disimpan ke file

JSON file -> Python object :

saat file json dibaca diubah lagi jadi python object(dict)

"""

# Contoh penggunaan pada Dompet

{
  "Haikal": {
    "saldo": 12000,
    "riwayat": [
      "Setor 2000",
      "Tarik 500"
    ]
  },
  "HuTao": {
    "saldo": 17000,
    "riwayat": []
  }
}

# nama dompet -> key "Haikal HuTao"
# data dompet-> value "saldo riwayat"

"""Fungsi utama JSON
•json.dump() -> untuk menyimpan dari dict ke file (tulis ke file)
•json.load() -> untuk membaca dari file ke dict (baca dari file)
•json.dumps() -> untuk menyimpan dari dict ke string
•json.loads() -> untuk membaca dari file ke string
"""


#Contoh Penggunaan sederhana

class bini:
    def __init__(self,nama,umur,alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def save(self,location):
        data = {
        "nama": self.nama,
        "umur": self.umur,
        "alamat": self.alamat
        }
        with open(location, "w") as f:
            json.dump(data, f, indent=4) # -> Indent = 4 agar JSON rapih
    def load(self,location):
        with open(location,"r") as f:
            data = json.load(f)
            self.nama = data["nama"] # -> masuk ke objek
            self.umur = data["umur"] 
            self.alamat = data["alamat"]

b = bini("HuTao",19,"Liyue")

b.save("Bini.json")

"""Membaca Json"""

def baca(location):
    with open(location,"r") as f:
        return json.load(f)
data = baca("Bini.json")

"""UPDATE DATA JSON"""

data["nama"] = "Lilim"
def save(location,data):
    with open(location, "w") as f:
        json.dump(data, f, indent=4)

save("Bini.json",data)
b = bini("",0,"")
b.load("Bini.json")
print (b.nama) # -> Output masih data lama karena data sekarang belum di save,sedangkan data lama sudah di save
print (b.umur)
print (b.alamat)

print()

"""VALIDASI SEDERHANA

try:
    with open("Bini.json", "r") as f:
        data = json.load(f)
except:
    data = {}

"""

"""Error handling Json"""

"""Error 1 — File tidak ada"""
# Kalau Bini.json belum ada, langsung crash!
"""with open("Bini.json", "r") as f:
    data = json.load(f)"""
# FileNotFoundError: No such file or directory
"""Error 2 — JSON rusak"""
# Isi file rusak / tidak valid
# misal isinya: {nama: HuTao}  ← tanpa tanda kutip
"""data = json.load(f)"""
# json.JSONDecodeError: Expecting property name
"""Error 3 — Key tidak ada"""

"""data = {"nama": "HuTao", "umur": 19}"""
#print(data["alamat"])  # ← key ini tidak ada!
# KeyError: 'alamat'


class anak:
    def __init__(self,nama,umur,hobi):
        self.nama = nama
        self.umur = umur
        self.hobi = hobi

    def save(self,location):
        data = {
        "nama": self.nama,
        "umur": self.umur,
        "hobi": self.hobi
        }
        with open(location, "w") as f:
            json.dump(data, f, indent = 4) # -> Indent = 4 agar JSON rapih
    def load(self,location):
        try:
        
            with open(location,"r") as f:
                data = json.load(f)
                self.nama = data["nama"] # -> masuk ke objek
                self.umur = data["umur"] 
                self.hobi = data["hobi"]

        except FileNotFoundError as e:
            print (f"ERROR {e}")

        except json.JSONDecodeError as e:
            print (f"ERROR {e}")

        except KeyError as e:
            print (f"ERROR {e}")
anak1 = anak("Sagiri",12,"Menggambar")
anak1.save("anak.json")
anak1.load("anak.json")

anak1.load("ana.json") # test FileNotFoundError

with open("anak.json","w") as f: # test json.JSONDecodeError
    f.write('setan') # masuk ke file
anak1.load("anak.json") 

with open("anak.json","w") as f: # test KeyError
    json.dump({"nama":"sagiri"},f) # -> Merubah file
anak1.load("anak.json") # Error karena ga ada umur sama hobi

"""Nested Json"""

#Nested JSON : json di dalam json
#contoh

data = {
"nama":"sagiri",
"umur":12,
"hobi":"menggambar",
"alamat":{
"kota":"tokyo",
"kode_pos":12345
}
}
#Alamat bukan berisi string melainkan dictionary lagi
for key,value in data.items():
    if isinstance(value,dict):
        print (f"{key}: ") # -> buat key untuk nested list alamat
        for k,v in value.items(): #-> breakdown kotq dan kode pos
            print (f"{k}:{v}")
    else:
        print (f"{key} : {value}")
print()
#contoh campuran

response = {
    "model": "claude-sonnet",
    "content": [
        {"type": "text", 
        "text": "Halo!"}
    ],
    "usage": {
        "input_tokens": 10,
        "output_tokens": 8
    }
}

for key,value in response.items():
    if isinstance(value,dict):
        print (f"{key} : ")
        for k,v in value.items():
            print (f"{k} : {v}")

    elif isinstance(value,list):
        print (f"{key} : ")
        for item in value:
            for k,v in item.items():
                print (f"{k} : {v} ")

    else:
        print (f"{key} : {value} ")

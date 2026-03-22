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


def baca(location):
    with open(location,"r") as f:
        return json.load(f)


def save(location,data):
    with open(location, "w") as f:
        json.dump(data, f, indent=4)

def write(location,data):
    with open (location,"w") as f:
        f.write(data)
        
"""Membaca Json"""

data = baca("Bini.json")

"""UPDATE DATA JSON"""

data["nama"] = "Lilim"
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
            print (f"File ga ada sat : {e}")

        except json.JSONDecodeError as e:
            print (f"File lu rusak ngentot :{e}")

        except KeyError as e:
            print (f"Si bangsat,Key lu ga ada di filenya : {e}")
            
anak1 = anak("Sagiri",12,"Menggambar")
anak1.save("anak.json")
anak1.load("anak.json")
print ("===isi dari anak.json===")
print (anak1.nama)
print (anak1.umur)
print (anak1.hobi)

print()

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
        for k,v in value.items(): #-> breakdown kota dan kode pos
            print (f"{k}:{v}")
    else:
        print (f"{key} : {value}")
print()
#contoh campuran terdiri dari list dan dict

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




print()

data = {
    "user": {
        "nama": "Haikal",
        "umur": 19,
        "akun": [
            {
                "platform": "github",
                "followers": 120
            },
            {
                "platform": "twitter",
                "followers": 500
            }
        ]
    },
    "status": "aktif"
}
"""UPDATE DATA"""

data["user"]["akun"][0]["followers"] = 200
save("user.json",data)


"""SIMULASI Request and Response API"""
#Cara buat Request

request = {
    "model": "claude-sonnet-4-20250514",  # ← AI mana yang mau dipake
    "max_tokens": 1000,                   # ← maksimal panjang jawaban
    "messages": [                         # ← list percakapan
        {
            "role": "user",               # ← yang ngomong siapa
            "content": "Halo Claude!"     # ← isi pesannya
        }
    ]
}

"""
"model"      → pilih AI nya mau yang mana
               kayak pilih kasir McDonald's mana

"max_tokens" → batas panjang jawaban
               1 token ≈ 1 kata
               max_tokens: 10 → jawaban pendek
               max_tokens: 1000 → jawaban panjang

"messages"   → list percakapan
               bisa isi lebih dari 1 pesan!
               kayak history chat


message harus list karena pesan bisa banyak dan tiap item di list(disini dict) itu satu giliran bicara"""

response = {
    "id": "msg_123abc",
    "type": "message",
    "role": "assistant",
    "model": "claude-sonnet-4-20250514",
    "content": [
        {
            "type": "text",
            "text": "Halo! Ada yang bisa dibantu?"
        }
    ],
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 10,
        "output_tokens": 8
    }
}

"""
"id"          → nomor unik tiap percakapan
                kayak nomor struk belanja

"role"        → yang ngomong siapa
                "assistant" = Claude yang bales

"content"     → isi jawaban AI (list of dict!)
                                ↑
                         kamu udah tau ini! 😄

"stop_reason" → kenapa AI berhenti jawab
                "end_turn" = jawaban udah selesai

"usage"       → laporan pemakaian
                input_tokens  = panjang pertanyaan kamu
                output_tokens = panjang jawaban AI
"""

print ("Ini pesan : ",response["content"][0]["text"])
print ("ini model ai :",response["model"])
total = response["usage"]["input_tokens"] + response["usage"]["output_tokens"]
print ("total token : ",total)
cek = response["stop_reason"]
print ("Apakah Stop reason adalah end turn ? ",True if cek == "end_turn" else False)
print()
"""Simulasi penggabungan Request dam Response"""

request = {
    "model": "lilim -reinhart- 76897",
    "max_toxens":1250,
    "messages":[
    {
        "role":"user",
        "content":"Hai,namaku Haikal"
    }
    ]
}


response = {
    "id": "msg_123abc",
    "type": "message",                                              "role": "assistant",
    "model": "lilim -reinhart- 76897",
    "content": [
        {
            "type": "text",
            "text": "Halo!Aku Lilim Ai assistant.Ada yang bisa aku bantu?" }
    ],
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 7,
        "output_tokens": 10
    }
}

jawaban = response["content"][0]["text"]
model = response["model"]
total = response["usage"]["input_tokens"]+response["usage"]["output_tokens"]

print ("Pertanyaan  : ",request["messages"][0]["content"])
print ("Jawaban     : ",jawaban)
print ("Model       : ",model)
print ("Total token : ",total)

print()
request["messages"].append({
"role":"assistant",
"content":jawaban
}
)
request["messages"].append({
"role":"user",
"content":"Aku ingin belajar JSON"
}
)
request["messages"].append({
"role":"assistant",
"content":"Baik akan lilim bantu sampai bisa"
}
)

for pesan in request["messages"]:
    print (f'{pesan["role"]} : {pesan["content"]}')

save("latihan_request.json",request)
save("latihan_response.json",response)

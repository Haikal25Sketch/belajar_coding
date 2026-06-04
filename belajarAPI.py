import logging
import requests
from dotenv import load_dotenv
import requests
import os

#API : Perantara antara user dan server
# user minta data -> API proses -> balik data ke user

#cara pakai:
response = requests.get("https://api.github.com") # () tempat isi url yang menjadi Alamat API
# isi dalam kurung GET:
"""
requests.get(
    url,                    # wajib
    headers=headers,        # kartu identitas
    params={"page": 1,"per_page" : 10},     # filter/pencarian di URL artinya tampilkan halaman 1 perhalaman 10 item(bisa diseting)
    
    timeout=5,              # batas waktu tunggu response,kalau lebih dari yang ditentukan ,lempar Timeout
    verify=True,            # verifikasi SSL(Keamanan antara server dan user, itulah kenapa https lebih aman dibandigkan http karena data yang dikirim ke server dienkripsi (diubah menjadi kode acak)
    
)
params otomatis jadi:
url?page=1
params: cara kita memberikan instruksi spesifik kepada server
  tentang data apa yang kita inginkan tanpa mengubah alamat utama (endpoint) API-nya.

Biasanya digunakan untuk 4 hal utama:
   * Filtering: "Tampilkan hanya data yang kategorinya 'elektronik'."
   * Sorting: "Urutkan data dari yang 'termurah'."
   * Pagination: "Tampilkan data di 'halaman 5'."
   * Searching: "Cari data dengan kata kunci 'laptop'."


"""

print ("response.status_code-nya adalah : ",response.status_code)

#print (response.json()) INI BELUM RAPI
data = response.json() # Data menjadi dict
for key,value in data.items():
    print (f"{key} : {value}") # INI RAPI

print()

#status code
"""200: sukses
404:tidak ditemukan
500: error server
"""

"""
GET: Ambil data dari laci server
POST : Kirim data ke laci server
"""

"""
response itu dict karena data.json() ,tolong pahami haikal
""" 
"""
username = "Haikal25Sketch"  # github gw
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()

print("Username:", data["login"])
print("Public Repos:", data["public_repos"])
print("Akun dibuat:", data["created_at"])
print()
"latihan mengambil data repos dari github"
print ("===data repos===")
url = f"https://api.github.com/users/{username}/repos" #-> yang paling pojok adalah endpoint
response = requests.get(url)
data = response.json()
#print (data) masih acak acakan
#repos itu list of dict ,jadi harus diunpack dulu
for repo in data:
    print ("Repos : ",repo["name"])
"""
"""belajar API key"""

print()
#API key : kata sandi khusus yang digunakan untuk mengidentifikasi dan mengizinkan sebuah aplikasi untuk mengakses API

load_dotenv() #-> buka dan baca file .env (file tersembunyi ,bisa dilihat di ls -a)
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}"
}

url = "https://api.github.com/user"
response = requests.get(url, headers=headers)
data = response.json()
print (data)
print()
print ("LATIHAN POST ")
#isi post

"""
requests.post(
    url,                    # wajib
    headers=headers,        # informasi tambahan yang dikirim ke server,bisa sebuah identitas(token) dan format data(json atau form)
    json=data,              # kirim data format JSON
    data=data,              # kirim data format form
    timeout=5,              # batas waktu tunggu
)
"""
url ="https://httpbin.org/post" # -> API khusuz untuk testing yang akan mengembalikan apa yang kita kirim
data ={
"nama":"Sagiri",
"umur":12
}

response = requests.post(url,json = data)
print ("response.status_code-nya adalah : ",response.status_code)
print ("OUTPUT : ")
print (response.json())
# Output
{'args': {}, 'data': '{"nama": "Sagiri", "umur": 12}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '30', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.33.0', 'X-Amzn-Trace-Id': 'Root=1-69cb9093-6877c5c60f07e18274479a1d'}, 'json': {'nama': 'Sagiri', 'umur': 12}, 'origin': '103.121.16.127', 'url': 'https://httpbin.org/post'}

print()

"LATIHAN ERROR HANDLING API"

#response = requests.get("https://contoh-website-yang-tidak-ada.com") -> error

#print("Program selesai") # ga kecetak soalnya program berhenti



try:
    response = requests.get("https://contoh-website-yang-tidak-ada.com")
    print ("request berhasil") #-> ini g akan keluar karena code ini berada setelah error terjadi dan di dalam try
except:
    print("Terjadi error!")

print("Program selesai")

"""jenis error dalam API yang sering terjadi"""

#•ConnectionError : internet mati atau url salah total,contoh:
#requests.get("https://urlygasalah123.com")

#•HTTPError: Url bener tapi server balik error,jenisnya:
#404 → endpoint ga ada
response = requests.get("https://api.github.com/tidakada123")
print ("HTTPError:", response.status_code)

#401 → token salah/expired
headers = {"Authorization": "token tokenpalsu123"}
response = requests.get("https://api.github.com/user", headers=headers)
print ("Token salah :", response.status_code)

#403 → ga punya akses
response = requests.get("https://api.github.com/users/ghost/settings")
print("Tidak memiliki akses :", response.status_code)

#429 → spam request
for i in range(2):
    response = requests.get("https://api.github.com")
print("Spam requests terdeteksi:", response.status_code)

print()

headers = {
    "Authorization": f"token {token}"
}
try:
    response = requests.get("https://api.github.com/tidakada123",headers = headers)
    response.raise_for_status() #-> fungsinya otomatis lempar error kalau status 400 keatas

except requests.exceptions.HTTPError as e:
    print (f"HTTP Error: {e}")
#Urutan error dari yang spesifik - umum
#requests.exceptions.ConnectionError   # koneksi mati
#requests.exceptions.Timeout           # kelamaan
#requests.exceptions.HTTPError         # status 400+
#requests.exceptions.JSONDecodeError   # response bukan JSON
#requests.exceptions.RequestException  # semua


"""Contoh penggunaan"""

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
terminal = logging.StreamHandler()
terminal.setLevel(logging.WARNING)
stream_fmt = logging.Formatter("%(levelname)s |  %(message)s")
terminal.setFormatter(stream_fmt)
logger.addHandler(terminal)

headers = {
    "Authorization": f"token {token}"
}
def ambil_API(url):
    try:
        response = requests.get(url,headers = headers,timeout = 5)
        response.raise_for_status() #-> angkat error diatas 400
        data = response.json()
        for key,value in data.items():
            print (f"{key} : {value}")
            
    except requests.exceptions.ConnectionError:
        logger.error("KONEKSI INTERNET MATI,TIDAK BISA MENGAKSES!")
    except requests.exceptions.Timeout:
        logger.warning("TERLALU LAMA!!")

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTPS ERROR!!! : {e} ")

    except requests.exceptions.RequestException as e :
        logger.error(f"ERROR!!! {e} ")
    print ("RESPONSE BERHASIL!!")
take = ambil_API
take("https://api.github.com")


# ============================================================
# TINGKAT LANJUT: API UNTUK AI ENGINEERING
# ============================================================
"""
Sebagai AI Engineer, kamu akan sering berurusan dengan:
1. Validasi Output (Pydantic) - Memastikan data API bersih sebelum masuk ke Model AI.
2. Robustness (Retries) - Menangani API Model (OpenAI/HuggingFace) yang sering timeout/rate limit.
3. Batch Processing (Async) - Mengirim banyak data sekaligus ke model.
"""

# 1. VALIDASI DATA DENGAN PYDANTIC (Sangat penting di AI!)
# Jika data dari API kotor, model AI bisa berhalusinasi atau crash.
try:
    from pydantic import BaseModel, Field, ValidationError
    from typing import List, Optional

    class GithubUser(BaseModel):
        login: str
        id: int
        bio: Optional[str] = "Tidak ada bio" # Default jika null
        public_repos: int = Field(alias="public_repos")

    def ambil_user_aman(username):
        url = f"https://api.github.com/users/{username}"
        resp = requests.get(url)
        if resp.status_code == 200:
            try:
                # Validasi otomatis: jika 'id' bukan int, akan lempar error
                user = GithubUser(**resp.json()) 
                print(f"VALIDASI SUKSES: {user.login} punya {user.public_repos} repos.")
                return user
            except ValidationError as e:
                print(f"DATA API TIDAK VALID: {e}")
        return None

    print("\n--- Testing Pydantic Validation ---")
    ambil_user_aman("Haikal25Sketch")

except ImportError:
    print("\n[HINT] Install pydantic untuk belajar validasi data: pip install pydantic")


# 2. HANDLING RATE LIMITS (Exponential Backoff)
# AI API sering membatasi jumlah request per menit.
import time
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

def session_dengan_retry():
    session = requests.Session()
    retry = Retry(
        total=3,            # Coba lagi maksimal 3 kali
        backoff_factor=1,   # Tunggu 1 detik, lalu 2, lalu 4 (exponential)
        status_forcelist=[429, 500, 502, 503, 504], # Retry hanya jika status ini
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session

print("\n--- Testing Robust Session ---")
s = session_dengan_retry()
try:
    r = s.get("https://api.github.com", timeout=5)
    print(f"Status dengan Retry logic: {r.status_code}")
except Exception as e:
    print(f"Gagal setelah 3x percobaan: {e}")


# 3. ASYNC REQUESTS (Cuplikan Konsep)
"""
Untuk AI Engineer, gunakan library 'httpx' untuk memanggil API secara paralel.
Contoh (Pseudo-code):
import asyncio
import httpx

async def panggil_model_ai(data):
    async with httpx.AsyncClient() as client:
        resp = await client.post("URL_MODEL", json=data)
        return resp.json()

# Ini memungkinkan kamu memanggil 100 model AI secara bersamaan!
"""

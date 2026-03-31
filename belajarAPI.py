import requests

#API : Perantara antara user dan server
# user minta data -> API proses -> balik data ke user

#cara pakai:
response = requests.get("https://api.github.com") # () tempat isi url yang menjadi Alamat API
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
response itu dict karena data ,tolong pahami haikal
"""

username = "Haikal25Sketch"  # github gw
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()

print("Username:", data["login"])
print("Public Repos:", data["public_repos"])
print("Akun dibuat:", data["created_at"])
print()
"""latihan mengambil data repos dari github"""
print ("===data repos===")
url = f"https://api.github.com/users/{username}/repos" #-> yang paling pojok adalah endpoint
response = requests.get(url)
data = response.json()
#print (data) masih acak acakan
#repos itu list of dict ,jadi harus diunpack dulu
for repo in data:
    print ("Repos : ",repo["name"])

"""belajar API key"""
print()

from dotenv import load_dotenv
import requests
import os

load_dotenv() #-> buka dan baca file .env (file tersembunyi ,bisa dilihat di ls -a)
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}"
}

url = "https://api.github.com/user"
response = requests.get(url, headers=headers)
data = response.json()

print("Login:", data["login"])
print("Name:", data["name"])

print()
print ("LATIHAN POST ")
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

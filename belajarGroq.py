import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}

data_2 ={
    "model":"llama-3.3-70b-versatile",
    "messages":[
        {"role":"system","content":"kamu adalah assisten yanv membantuku mempelajari python dengan tujuan menjadi ai enginering."},
        {"role":"user","content":"beritahu aku penggunaan dekorator secara lengkap"}
]
}
#role ada 3.system,user,assistant
#system: kepribadian Ai nya
#user : pesan dari pengguna
#assistant : balasan dari ai nya letaknya di data["choices"][0]["message"]["content"]
response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers = headers,
    json = data_2
)

data = response.json()
print (data["choices"][0]["message"]["content"])


print()



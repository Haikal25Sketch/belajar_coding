
import json

def save(location,data):
    with open(location,"w")as f:
        json.dump(data,f,indent = 4)

def read(location):
    with open(location,"r") as f:
        return json.load(f)
         

class istri:

    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def save(self,location):
        try:
            with open(location,"r") as f:
                data_lama = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            data_lama ={}

        data_lama[self.nama]={
        "umur":self.umur}

        with open(location,"w") as f:
            json.dump(data_lama,f,indent= 4)

    def load(self,location): #-> baca file
        with open(location,"r") as f:
            self.nama = None
            self.umur = None

            data = json.load(f)
            self.nama = data["nama"]
            self.umur = data["umur"]


istri1 = istri("Sagiri",12)
istri2 = istri("Lilim",14)
istri3 = istri("Saia",17)
istri4 = istri("Klee",20)
istri5 = istri("HuTao",13)

istri1.save("MyBini.json")
istri2.save("MyBini.json")
istri3.save("MyBini.json")
istri4.save("MyBini.json")
istri5.save("MyBini.json")

data = read("MyBini.json")
data["Sagiri"]["Hobi"] = "Menggambar"
data["HuTao"]["Hobi"] = "Nawarin Kuburan"
data["Klee"]["Hobi"] = "Ngebom Teyvat"
save("MyBini.json",data)

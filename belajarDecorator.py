"""DECORATOR"""
# menambahkan kemampuan fungsi tanpa mengubah isi fungsi tersebut

# Dasarnya: fungsi bisa masuk ke fungsi lain atau dengan kata lain fungsi membungkus fungsi lain
def sapa():
    print ("Haikal suka sephia")
sapa() # Output Haikal suka sephia

print()

def lapis2(fungsi_lain):
    print ("*******")
    fungsi_lain() # memanggil fungsi lain
    print ("*******")
lapis2(sapa)

print()

def decorator(function):
    def lapis():
        print ("==SEBELUM==")
        function()
        print ("==SESUDAH==")
    return lapis

@decorator
def salam():
    print ("Arigato")
salam()
print()


#Gini juga bisa,pilih salah satu aja
greet = decorator(salam)
greet()

print()
#contoh lain
def transaksi(function):
    def lapis(*args,**kwargs):
        print ("===SEBELUM TRANSAKSI===")
        function(*args,**kwargs)
        print ("===SESUDAH TRANSAKSI===")
    return lapis

@transaksi
def tarik(jumlah):
    print ("MENARIK ",jumlah)

tarik(500)

#latihan validasi decorator
print()

def validasi(function):
    def lapis(*args,**kwargs):
        if args[0] <= 0:
            print ("ERROR,ANGKA HARUS LEBIH DARI 0")
        else:
            function(*args,**kwargs)
    return lapis

@validasi
def tarik(jumlah):
    print ("MENARIK ",jumlah)

tarik(500)
print()
tarik(-7)


def pembungkus(function):
    def isi(*args,**kwargs):
        function(*args,**kwargs)
    return isi

@pembungkus
def sapa(nama):
    print ("hai ",nama)

sapa(nama= 9)
sapa(9)

#latihan decorator

def log_proses(function):
    def isi(*args,**kwargs):
        print (f"[LOG] {args[0].__class__.__name__} dimulai")
        hasil = function(*args,**kwargs) # ini diperlukan jika function memiliki return
        print (f"[LOG] {args[0].__class__.__name__} selesai")
        return hasil
    return isi



class Tarik:
    def __init__(self,jumlah):
        self.jumlah = jumlah

    @log_proses
    def proses(self,saldo):
        return saldo - self.jumlah

tarik = Tarik(1000)
print (tarik.proses(9))

# alur proses:
"""
log_proses(proses):
    isi(tarik,9) -> args[0],args[1]
        print (f"[LOG] {args[0].__class__.__name__} dimulai")
        hasil = proses(tarik,9)
        #didalam proses terjadi return saldo(9)- self.jumlah(1000) yait        u -991 yang disimpan di variabel hasil
        print (f"[LOG] {args[0].__class__.__name__} selesai")
        return hasil -> mengembalikan isi hasil
    return isi -> mengembalikan isi isi

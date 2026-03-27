"""DECORATOR"""
# menambahkan kemampuan fungsi tanpa mengubah isi fungsi tersebut

# Dasarnya: fungsi bisa masuk ke fungsi lain atau dengan kata lain fungsi membungkus fungsi lain
def sapa():
    print ("Haikal suka sephia")
sapa() # Output Haikal suka sephia

print()

def lapis2(fungsi_lain):
    print ("sebelum")
    fungsi_lain() # memanggil fungsi lain
    print ("sesudah")
lapis2(sapa)


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

import time
kata =[
'ini adalah materi Dunder']
for word in kata :
  for wor in word :
    print (wor,end='',flush = True)
    time.sleep(0.1)
  print()
  time.sleep(0.2)
'''belajar __str__ dan __repr__'''
# __str__ dipakai untuk mencetak objek 
#dengan output yang bagus

# __repr__ dipakai untuk mencetak objek 
#dengan output yang jelas dan terstruktur

print ('belajar __str__ dan __repr__')
print()
class user:
  def __init__(self,nama,id):
    self.nama = nama
    self.id = id

  def __str__ (self):  # dunder ini dibuat agar print() bisa digunakan
    return f'{self.nama} : {self.id}'

  def __repr__(self): # dunder ini dibuat agar print(repr()) bisa digunakan:
    return f"user(nama:'{self.nama}'\nid:'{self.id}')"

user1 = user('Haikal',1707)
print (user1)
print()
print (repr(user1))

print()

'''belajar perbandingan objek(__eq__,__ne__,__lt__,__gt__,__le__,__ge__)'''
#sama seperti == , != , < , > , <= , >= outputnya boolean (True and False)
print ('belajar perbandingan')
print()

class produk:
  def __init__(self,nama,harga):
    self.nama = nama
    self.harga = harga

  def __str__(self):
    return f'{self.nama} : {self.harga}'

  def __repr__(self):
    return f"produk(nama :'{self.nama}'\nharga : '{self.harga}')"

  def __eq__(self,other):
    if not isinstance(other,produk):
      return NotImplemented
    return self.harga == other.harga and self.nama == other    .nama

  def __ne__(self,other):
    return self.harga != other.harga
    
  def __lt__(self,other):
    return self.harga < other.harga

  def __gt__(self,other):
    return self.harga > other.harga

  def __le__(self,other):
    return self.harga <= other.harga

  def __ge__(self,other):
    return self.harga >= other.harga

p1 = produk('Kopi',2000)
p2 = produk('Teh',1000)

print (p1) 
print (p2)
print (repr(p1))
print (repr(p2))
print (f'Harga {p1.nama} == Harga {p2.nama}  : {p1==p2}')
print (f'Harga {p1.nama} != Harga {p2.nama}  : {p1!=p2}')
print (f'Harga {p1.nama} <  Harga {p2.nama}  : {p1<p2} ')
print (f'Harga {p1.nama} >  Harga {p2.nama}  : {p1>p2} ')
print (f'Harga {p1.nama} <= Harga {p2.nama}  : {p1<=p2}')
print (f'Harga {p1.nama} >= Harga {p2.nama}  : {p1>=p2}')

'''belajar operasi matematika dasar untuk objek (__add__,__sub__,__mul__,__truediv__,__pow__):'''
print()
print ('belajar operasi matematika objek')
print()

class mtk():
  def __init__ (self,num):
    self.num = num

  def __str__ (self):
    return f'{self.num}'
    
  def __add__ (self,other):
    return mtk (self.num + other.num) #kalo self.num + other.num juga bisa,ini biar menghasilkan objek baru aja

  def __sub__ (self,other):
    return mtk(self.num - other.num)

  def __mul__ (self,other):
    return mtk(self.num * other.num)

  def __truediv__(self,other):
    try:
      hasil = self.num / other.num
      return mtk(hasil)
    except ZeroDivisionError:
      print ("Tidak bisa dibagi dengan 0")
      return None
      

  def __pow__(self,other):
    return mtk(self.num ** other.num)
    
a = mtk(1)
b = mtk(2)
c = mtk(0)

print (a+b)
print (a/c)
print (b-a)
print (a+b)
print (b**c)

'''belajar akses data (__len__,__getitem__,__setitem__,__delitem__)'''
print()
print ('Belajar akses data')
print()

class bookshelf:
  def __init__ (self):
    self.shelf = []

  def __str__(self):
    return f'{self.shelf}'

  def add (self,*buku):  #menambahkan buku ke self.shelf[]
    for b in buku:
      self.shelf.append(b)
  def __len__(self):  #mengakses panjang data
    return len(self.shelf)

  def __getitem__(self,index): # mengambil data
    return self.shelf[index]

  def __setitem__(self,index,value): # mengubah data
    self.shelf[index] = value

  def __delitem__(self,index): #, menghapus data
    del self.shelf[index]

bs = bookshelf()
bs.add('Laut bercerita','Cantik itu luka','Filosofi Teras')
print (bs)
print(bs[0])
bs[1]='Rembulan Tenggelam di wajahmu'
print (bs)
del bs[1]
print (bs)
print ('jumlah bukunya ada : ',len(bs))
print()

'''belajar inisialisasi dan kontruksi (__new__,__init__,__del__)'''
print ('belajar inisialisasi dan kontruksi')
print()
#saat membuat objek baru ,python tidak langsung lompat ke __init__
#ada tahap internal dulu,yaitu __new__ diperintahkan untuk membuat objek baru yang kosong
#barulah di __init__ akan diisi semau kita 
#jika ingin menghapus objek,barulah __del__ berguna,tapi jarang digunakan
class produk:
  def __new__(cls,*args,**kwargs):
    print ("Membuat objek di __new__") #objek berasal dari sini
    obj = super().__new__(cls)
    print ("ini adalah id obj ",id(obj))
    return obj

  def __init__(self,nama,harga): #cek id self dan obj untuk
#membuktikan bahwa objek berasal dari __new__
    print ("Objek diinisialisasi (diisi apapun) di __init__")
    print ("ini adalah id self ",id(self))
    self.nama = nama
    self.harga = harga

  def __str__(self):
    return f'{self.nama} = {self.harga}'

  def __repr__(self):
    return f'produk(Nama : "{self.nama}"\nHarga : "{self.harga}")'

  def __del__(self):
    print (f'{self.nama} dihapus dari memory')

a = produk("Kopi",5000)
print (a)
print (repr(a))
del a
#print (a) akan terjadi error karena a telah dihapus
print()
print ('Belajar inisialisasi ke 2(Singletone(hanya ada 1 objek))')
print()

class akunbank:
  _instance = None

  
  def __new__(cls,*args,**kwargs):
    print ('Membuat akun di __new__')
    if cls._instance is None:
      print ('Membuat akun dengan instance baru')
      cls._instance = super().__new__(cls)
    else:
      print ('Membuat akun dengan instance yang sudah ada')

    return cls._instance

  def __init__(self,nama,no_rek):
    if not hasattr( self,"_initialized"):
      self.nama = nama
      self.no_rek = no_rek
      self._initialized = True
      print ("Inisialisasi Pertama")
    else:
       print ("Inisialisasi tidak dilakukan lagi")
     

  def __str__(self):
    return f'{self.nama} : {self.no_rek}'

a = akunbank("BRI",7766)
b = akunbank("Mandiri",9988)
print (f'ini adalah id a : {id(a)}')
print (f'ini adalah id b : {id(b)}')
print (f'apakah {a.nama} sama dengan {b.nama} : {a is b}')

'''belajar context manager __enter__ dan __exit__'''
print()
print ('belajar __enter__ dan __exit__')
#__enter__ dan __exit__ adalah dunder yang membuat 'with'
# bisa digunakan oleh objek
print()
class Test:
  def __init__(self,nama):
    self.nama = nama

  def __enter__(self): # ini disimpan dalam variable t
    print ('ini di dalam enter')
    return f'lengserkan {self.nama}'

  def __exit__(self,exc_type,exc_val,exc_tb): #exc_type(jenis error)
    print ('ini di akhir context manager') # exc_val(pesan error)
    print ('Error is ',exc_type,exc_val,exc_tb) # exc_tb(letak error)
    return False # agar error tetap dikeluarkan

with Test('Soeharto')as t:
  print (t)
print()
'''latihan __enter__ dan __exit__ lagi'''
print ('Latihan __enter__ dan __exit__ lagi')
class Try:

  def __init__(self,nama):
    self.nama = nama

  def __enter__(self):
    print (self.nama,'masuk ruangan')
    return f'{self.nama} berhasil masuk ruangan'

  def __exit__(self,exc_type,exc_val,exc_tb):
    print (f'apakah ada masalah ? {exc_type}')

    if exc_type is None :
      print (f'{self.nama} berhasil keluar ruangan')

    else:
      print (f'{self.nama} masih terjebak di dalam ruangan\ntolong perbaiki errornya')

    return False # Jika True error ga bakal raise

with Try('HuTao') as t:
  print (t)
  print (type(t)) # t tetap dicetak meski disini pass

print()
'''belajar __call__'''
# __call__ adalah dunder yang berfungsi agar objek bisa dipanggil
# dan melakukan aksinya

class Calc:
  def __init__(self):
    self.num = 7

  def __call__(self):
    self.num **=2
    return self.num

a = Calc()
print (a())
print (a())
print (a())

print()
'''belajar __iter__ dan __next__ '''
print ('belajar __iter__ dan __next__')
# __iter__ dan __next__ adalah pasangan Dunder agar for bis dipakai.
class example:
  def __init__(self,*nama):
    self.nama = nama # iterable ≠ iterator
    self.batas = 0
  def __len__(self):
    return len(self.nama) # ini adalah Iterator sekali pakai
  def __iter__(self): # __iter__ yang bagus harus mereturn iterator baru
    return self

  def __next__(self):
    if self.batas >= len(self.nama): # jika ingin dipakai berulang kali,
    #maka state harus diletakkan di bukan objek,tapi di iterator
      raise StopIteration
    nama = self.nama[self.batas]
    self.batas += 1
    return nama

wf = example ('HuTao','Nahida','Yaemiko','Raiden')
print (len(wf))
for a in  wf:
  print ('Aku karbit dan waifuku adalah ',a)

print()
print ('Latihan iter dan next 2')
print()
class countdown:

  def __init__(self,n):
    self.n = n
    self.batas = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.n <= self.batas:
      raise StopIteration
    nilai= self.n
    self.n-=1
    return nilai
c = countdown(5)
for a in c :
  print (a)

print()
print ('Latihan iter dan next 3')
print()
class genap:

  def __init__(self,nilai):
    self.awal = 0
    self.nilai= nilai

  def __iter__ (self):
    return self

  def __next__(self):
    if self.awal > self.nilai:
      raise StopIteration
    nilai = self.awal
    self.awal+=2
    return nilai

g = genap(10)
for genap in g:
  print (genap)

print()
print ('latihan iter dan next 4')
print()
class akunbank:

  def __init__(self,nama):
    self.nama = nama
    self.saldo = 0
    self.riwayat = []
    self.batas = 0

  def tambah(self,jumlah):
    if jumlah < 0:
      print ('Tidak boleh negatif')
    self.saldo += jumlah
    info = f'+{jumlah}'
    self.riwayat.append(info)

  def tarik(self,jumlah):
    if jumlah > self.saldo:
      print ('Saldo tidak cukup')
    elif jumlah < 0:
      print ('Tidak boleh negatif')
    self.saldo -= jumlah
    info = f'-{jumlah}'
    self.riwayat.append(info)

  def __iter__(self):
    return self

  def __len__(self):
    return len(self.riwayat)
    
  def __next__(self):
    if self.batas >= len(self.riwayat):
      raise StopIteration
    transaksi = self.riwayat[self.batas]
    self.batas +=1
    return transaksi

a = akunbank('Haikal')
a.tambah(1000)
a.tarik(10)
a.tambah(90)
a.tambah(80)
a.tarik(98)
print(a.riwayat)
for b,c in enumerate (a):
  print (f'transaksi ke {b+1}:{c}')

for genap in g: # output kosong,karena sekali pakai doang
  print(genap)

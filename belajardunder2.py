'''belajar __iter__ dan __next__ lanjutan'''
#iterable ≠ iterator
# iterable hanya menyediakan iterator
# iterator yang menyimpan state
print('Latihan Iter dan next lanjutan')

class rangeterbalik:

  def __init__(self,n):
    self.n = n

  def __iter__(self):
    return iterator(self.n)

class iterator:

  def __init__(self,n):
    self.current = 0
    self.n = n

  def __iter__(self):
    return self

  def __next__(self):
    if self.n <= self.current:
      raise StopIteration
    val = self.n
    self.n -=1
    return val
print (rangeterbalik.__dict__)
a = rangeterbalik(1)
print (a.__dict__)
for b in a:
  print (b)
for x in a:
  print (x) # bisa dipakai berulang kali

print()

'''belajar generator(yield)'''
print ('belajar generator(yield)')
print()
# yield merupakan mesin iterator otomatis (iter dan next
# dalam satu paket)

# yield itu :
#-return + pause lanjut lagi saat next dipanggil
#-fungsi tidak mati
#-state dibekukan
#-eksekusi berlanjut tepat setelah yield berakhir

class Ganjil:

  def __init__ (self,n):
    self.n = n

  def __iter__(self):
    current = 1
    while current <= self.n:
      yield current
      current += 2


for m in Ganjil(10):
  print (m)
print()
for n in Ganjil(4):
  print (n)
print()
print ('Latihan yield doang tanpa class')
def genap(n):
  current = 0
  while current <= n:
    yield current
    current +=2

j = genap(70) # gabisa diulang karena
for a in j: # satu state,satu generator,satu nyawa yaitu
  print (a) # j = genap(70)
print()
for b in j:
  print (b) # kosong

# tapi kalo ini bisa diulang
for a in genap(20):
  print (a) # karena state baru,generator baru,nyawa baru
print()
for b in genap(20):
  print (b)

print()
print ('Latihan yield 2')
print()
def checkpoint(n):
  current = 3
  while current <= n:
    yield current
    current += 3
a = checkpoint(11)
print (next(a))
print (next(a))
print (next(a))

print()
print ('Latihan yield 3')
print()

def otf(n): # tanpa yield,g ada state
  hasil = []
  for i in range(1,n+1):
    hasil.append(i)
  return hasil

a = otf(5)
for h in a:
  print (h)
for h in a:
  print (h)
print()

def otf_2(n): #dengan yield
  for a in range(1,n+1):
    yield a

a = otf_2(5)
for j in a:
  print (j)
for k in a:
  print (k)

def tes():
    print("mulai")
    yield 1
    print("lanjut")
    yield 2
    print('selesai')


for a in tes():
  print (a)
print()
'''belajar yield from '''
# yield from: menyambungkan mesin ke mesin lain

print ('belajar yield from')
print()
def a():
  print ('a') #next(df) kedua
  print ('b')
  yield 1
  yield 2 # next(df) ketiga
def b():
  yield 0 # dieksekusi pertama / next(df) yg pertama
  yield from a()
  print ('end') #next(df) terakhir
  yield 1

df = b()
print (next(df))
print (next(df))
print (next(df))
print (next(df))


print()


def a (*wife):
  for g in wife:
    print ('namaku istriku',g)
    yield 3
    yield 4

def b():
  yield 1
  yield 2
  yield from a('Hutao','Raiden shogun','YaeMiko')

for ls in b():
  print (ls)
# Generator (yield) itu cocok untuk 
#•alur linier
#•satu arah
#•konsumsi satu kali
#•data besar / tak terbatas

# Dan tidak cocok jika :
#•butuh akses ulang
#•butuh loncat-loncat
#•butuh state kompleks
#•butuh hasil lengkap cepat

'''belajar descriptor'''
# DESCRIPTOR
#•Objek yang mengontrol akses atribut milik objek lain.
#•Objek yg nyelip di class lain 
#3 senjata Descriptor
#__get__(self,instance,owner)
#__set__(self,instance,value)
#__delete__(self,instance)
'''latihan Descriptor'''

class nonemptystring:

	def __set_name__(self,owner,name):
		self.name = name

	def __get__(self,instance,owner):
		if instance is None:
			return self
		return instance.__dict__.get(self.name)

	def __set__(self,instance,value):
		if not isinstance(value,str):
			raise TypeError("Nilai harus string")
		if  value.strip() == "":
			raise ValueError("Nilai tidak boleh kosong")
		instance.__dict__[self.name] = value

	def __delete__(self,instance):
		if self.name in instance.__dict__:
			del instance.__dict__[self.name]

class Str:
	name = nonemptystring()

	def __init__(self,name):
		self.name = name
u = Str('Haikal') # ini benar
#b = Str(76) # ini salah
#u.name = 66 Ini salah
print()
'''latihan Descriptor 2'''
print ('latihan descriptor')

class MaxLength:
	def __init__(self,maxlength):
		self.maxlength = maxlength

	def __set_name__(self,owner,name):
		self.name = name
	def __get__(self,instance,owner):
		if instance is None:
			return self
		return instance.__dict__.get(self.name)
	def __set__(self,instance,value):
		if not isinstance(value,str):
			raise TypeError('Nilai harus String')
		if len(value) > self.maxlength:
			raise TypeError ('Karakter terlalu panjang')
		instance.__dict__[self.name] = value
	def __delete__(self,instance):
		if self.name in instance.__dict__:
			del instance.__dict__[self.name]

class data:
	name = MaxLength(10)

	def __init__(self,name):
		self.name = name

k = data('rimuru')
print (k.name)
k.name = 'latih'
print (k.name)
'''latihan'''
class transaksi:

    def __init__(self,jenis:str,jumlah:int):
        if jenis not in ("SETOR","TARIK"):
            raise ValueError("jenis hanya 'SETOR' dan 'TARIK'")
        if jumlah <= 0:
            raise ValueError("jumlah harus positif")
        self.jenis = jenis
        self.jumlah = jumlah

    def __str__(self):
        return f'{self.jenis} : {self.jumlah}'

    def __repr__(self):
        return f'transaksi("{self.jenis}" ":" "{self.jumlah}")'


class Dompet:
    def __init__(self,nama,saldo):
        self.riwayat = []
        self.nama = nama
        self.saldo = saldo
    def setor(self,value):
        self.saldo += value
        hasil = transaksi("SETOR",value)
        self.riwayat.append(hasil)
    def tarik(self,value):
        self.saldo -= value
        hasil = transaksi("TARIK",value)
        self.riwayat.append(hasil)
    def __iter__(self):
        for t in self.riwayat:
            yield t

    def __eq__(self,other):
        if not isinstance(other,Dompet):
            return NotImplemented
        return self.nama == other.nama and self.saldo == other.saldo

    def transaksi_setor(self):
        return [s for s in self.riwayat if s.jenis == "SETOR"]

    def transaksi_tarik(self):
        return [t for t in self.riwayat if t.jenis == "TARIK"]

    def total_setor(self):
        total = 0
        for s in self.riwayat:
            if s.jenis == "SETOR":
                total += s.jumlah
        return total

    def total_tarik(self):
        total = 0
        for t in self.riwayat:
            if t.jenis == "TARIK":
                total += t.jumlah
        return total
    def __enter__(self):
        self.saldo_awal = self.saldo
        print ('Saldo awal : ',self.saldo_awal)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.saldo_akhir = self.saldo
        selisih = self.saldo_akhir - self.saldo_awal
        print ('Saldo akhir :',selisih)
        print("Selisih:", selisih)
        return False

        
d = Dompet('Yaemiko',98)
d2 = Dompet('HuTao',87)
d.setor(887)
d.tarik(86)
d2.setor(8000)
d2.tarik(76)
print ('d = d2 ?',d == d2)
print (d.transaksi_setor())
print (d.transaksi_tarik())
print (d2.transaksi_setor())
print (d2.transaksi_tarik())

with d as r:
  r.setor(87)

print()
'''PENGENALAN INHERITANCE DAN POLYMORPHISM'''
print ('Pengenalan Inheritance dan Polymorphism')
print()
#Inheritance : Class baru mewakili perilaku dan struktur class lama
#MethodOverride : Class anak mengganti perilaku induk
#Polymorphism : Satu interface banyak perilaku / cara pakai samahasil beda

class kendaraan:

	def jalan (self):
		print ('kendaraan melaju')

class mobil(kendaraan): # inheritance, coba ketik mobil.jalan() dan lihat hasilnya
	pass

class motor(kendaraan):
	def jalan(self):
		print ('motor melaju') # method override

k = kendaraan()
m = mobil()
m2 = motor()
k.jalan()
m.jalan() # unik,ga ada def jalan tapi outputnya ada
m2.jalan()
print()
machine = [kendaraan(),mobil(),motor()] #Polymorphism
for mac in machine: #satu interface banyak perilaku
	mac.jalan()

'''latihan'''
print ('latihan polymorphism dan inheritance ')

class Transaksi: # ink kelas induk
	def proses(self,saldo):
		raise NotImplementedError ("Jangan dilewat proses() nya)")

class setor(Transaksi): # 3 class adalah kelas anak
	def __init__(self,saldo):
		self.saldo = saldo
		
	def proses(self,jumlah):
		return self.saldo + jumlah
		
class tarik(Transaksi):
	def __init__(self,saldo):
		self.saldo = saldo

	def proses(self,jumlah):
		return self.saldo -jumlah
		
class transfer(Transaksi):

	def __init__(self,target,jumlah):
		self.target = target
		self.jumlah = jumlah
		self.fee = 2.500

	def proses (self,saldo_pengirim):
		self.target.saldo += self.jumlah
		print (f'Transfer {self.jumlah} ke {self.target.nama} berhasil!!!')
		return saldo_pengirim - (self.jumlah + self.fee)
		
class wallet :

	def __init__(self,saldo,nama):
		self.saldo = saldo
		self.nama = nama
	def proses(self,transaksi): # polymorphism disini
		self.saldo = transaksi.proses(self.saldo)
w = wallet(8000,'Haikal')
w2 = wallet(9000,'YaeMiko')
s = setor(10000)
t = tarik(1000)
tf = transfer(w2,1000)
print (w.saldo)
w.proses(s) # w.proses(setor(10000)) juga bisa
print (w.saldo)
print ('saldo w2 :',w2.saldo)
w.proses(tf)
print ('saldo w2 :',w2.saldo)

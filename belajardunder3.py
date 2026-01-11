'''Composition vs Inheritance'''
# mirip ≠ mewariskan / pewarisan
# punya ≠ adalah
'''Inheritance'''
# A adalah B 
class Hewan:
	def makan(self):
		print ('makan')

class kucing(Hewan): 
	pass

k = kucing()
k.makan() # output 'makan' walaupun dia tidak mempunyai method makan,tetapi dia MEWARISI method makan dari class Hewan

'''Composition'''
# A punya B
class riwayat:

	def __init__(self):
		self.data = []

	def tambah(self,transaksi):
		self.data.append(transaksi)

class dompet:

	def __init__(self,saldo):
		self.saldo = saldo
		self.riwayat = Riwayat()

'''contoh composition'''


class riwayat:

    def __init__(self):
        self.data = []

    def tambah(self,transaksi):
        self.data.append(transaksi)
    def tampilkan(self):
        return self.data.copy()
class setor:

	def __init__ (self,jumlah): # self.jumlah itu jumlah setor
		self.jumlah = jumlah

	def proses (self,saldo):
		return saldo + self.jumlah

	def info (self):
		return f"SETOR {self.jumlah}"

class tarik:

	def __init__(self,jumlah):
		self.jumlah = jumlah

	def proses (self,saldo):
		if saldo < self.jumlah:
			raise ValueError("Saldo tidak cukup") # saldo itu self.saldo di dompet
		return saldo - self.jumlah

	def info (self):
		return f"TARIK {self.jumlah}"


class dompet:

	def __init__(self,nama,saldo):
		self.nama = nama
		self.saldo = saldo
		self.riwayat = riwayat() #composition disini

	def proses (self,transaksi):
		self.saldo = transaksi.proses(self.saldo)
		self.riwayat.tambah(transaksi.info())

	def info (self):
		return {
		"nama":self.nama,
		"saldo":self.saldo,
		"riwayat":self.riwayat.tampilkan()
		}

d = dompet("haikal",10000)
print (d.info())
d.proses(setor(1000))
print (d.info())
d.proses(tarik(8000))
print (d.info())

print()
'''latihan lagi'''

class dompet:

	def __init__(self,nama,saldo):
		self.nama = nama
		self.saldo = saldo
		self.riwayat = riwayat()

	def proses(self,transaksi):
		self.saldo = transaksi.proses(self.saldo)
		self.riwayat.tambah(transaksi.info())

	def info(self):
		return {
		"nama":self.nama,
		"saldo":self.saldo,
		"riwayat":self.riwayat.tampilkan()
		}

	def __str__(self):
		return f"Nama : {self.nama}\nSaldo : {self.saldo}"

	def __eq__(self,other):
		if not isinstance(other,dompet):
			raise NotImplementedError
		return self.nama == other.nama and self.saldo == other.saldo

	def __enter__(self):
		self.saldo_awal = self.saldo
		print (f"Saldo awal {self.nama} : {self.saldo_awal}")
		return self
	def __exit__(self,exc_type,exc_val,exc_tb):
		self.saldo_akhir = self.saldo
		print (f"Saldo akhir {self.nama} : {self.saldo_akhir}")
		selisih = self.saldo_akhir - self.saldo_awal
		if self.saldo_akhir > self.saldo_awal:
			print ("Bertambah : +",selisih)
		elif self.saldo_akhir < self.saldo_awal:
			print ("Berkurang : ",selisih)
		return False
		
class transaksi:

	def __init__(self,jenis,jumlah):
		if jenis not in ("SETOR","TARIK"):
			raise ValueError("HANYA BISA SETOR DAN TARIK")
		if jumlah < 0 :
			raise ValueError ("NOMINAL HARUS POSITIF")
		self.jenis = jenis
		self.jumlah = jumlah

	def proses(self,saldo):
		pass

	def info(self):
		pass

class setor(transaksi):

	def __init__(self,jumlah):
		self.jumlah = jumlah

	def proses(self,saldo):
		return saldo + self.jumlah

	def info(self):
		return f"SETOR {self.jumlah}"

class tarik(transaksi):

	def __init__(self,jumlah):
		self.jumlah = jumlah

	def proses(self,saldo):
		if saldo < self.jumlah:
			raise ValueError ("SALDO TIDAK CUKUP")
		return saldo - self.jumlah

	def info(self):
		return f"TARIK {self.jumlah}"

class riwayat:

	def __init__(self):
		self.data = []

	def tambah(self,transaksi):
		self.data.append(transaksi)

	def tampilkan(self):
		return self.data.copy()

wallet = dompet("YaeMiko",1009)
wallet2 = dompet("RaidenShogun",1000)
print (wallet.info())
print (wallet2.info())
print()
wallet.proses(setor(190))
wallet2.proses(setor(800))
print()
print (wallet.info())
print (wallet2.info())
wallet.proses(tarik(19))
wallet2.proses(tarik(98))
print()
print (wallet.info())
print (wallet2.info())
print()
print ("Apakah wallet dan wallet2 sama ?",wallet == wallet2)

with wallet as wl:
	wallet.proses(setor(80))


'''Exception & Error design'''
#Error : Kesalahan logika / struktur kode yang harus diperbaiki
'''contoh Error'''
x = 10/0 # ZeroDivisionError
a = HuTao # NameError

#Exception : Masalah yang boleh terjadi dalam dunia nyata
'''contoh Exception :
-Saldo tidak cukup
-Transaksi ilegal
-input negatif'''

#Exception Design: Bagaimana kamu membuat sebuah Exception dalam sebuah kode
'''Yang dibahas di sini:
-pakai raise di mana
-bikin custom exception apa
-hierarki exception
-message error
-kapan try-except
-kapan from e
'''
#Error design : Keputusan sistem saat masalah terjadi
'''intinya saat masalah muncul:
- Apa yang boleh berubah
- Apa yang tidak boleh berubah
- siapa yang tanggung jawab
- Apakah sistem lanjut atau berhenti

'''

'''PRINSIP ERROR DESIGN'''
#1 Exception = Komunikasi,bukan dekorasi.Pakai bahasa yang kamu paham
'''
•contoh buruk
raise Exception('Error') -> Tidak tau Error apa
•contoh bagus
raise SaldoTidakCukup("Saldo tidak mencukupi untuk menarik 100") -> error terbaca jelas
'''
#2Jangan pakai ValueError untuk semuanya

'''CUSTOM EXCEPTION
•Buat base Error domain,contoh:

class DompetError(Exception):
	pass

karena:
satu keluarga error
gampang ditangkap global

•Buat Error spesifik

class SaldoTidakCukup(DompetError)
	pass
class NominalTidakValid(DompetError)
	pass
class TransaksiIlegal(DompetError)
	pass

•lempar di tempat yng benar
ex salah:
def tarik(self,saldo):
	if saldo < self.jumlah:
		print ("saldo kurang")
		return saldo  -> harusnya jngn ada ini,kan saldonya aja kurang
ex benar:
def tarik(self,saldo):
	if saldo < self.jumlah:
		raise SaldoTidakCukup()
	return saldo - self.jumlah

'''

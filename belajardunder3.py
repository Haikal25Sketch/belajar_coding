'''Composition vs Inheritance'''
# mirip ≠ mewariskan / pewarisan
# punya ≠ adalah
'''Inheritance'''
# A adalah B 
class Hewan:
	def makan(self):
		print ('makan')

class kucing(Hewan): 
	def gerak(self):
		print("lari")

k = kucing()
k.makan()
'''Hewan.gerak() -> akan error,karena Kucing adalah hewan,tapi tidak setiap hewan adalah kucing''' # output 'makan' walaupun dia tidak mempunyai method makan,tetapi dia MEWARISI method makan dari class Hewan

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
		self.riwayat = Riwayat() # ini composition

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
		if jumlah <= 0 :
			raise ValueError ("PERBAIKI NOMINAL")
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
try:
	x = 10/0 # ini error
except ZeroDivisionError as e:
	print ("Error : ",e)
	 # ZeroDivisionError

try:
	a = HuTao # ini error
except Exception as e:
	print ("Error : ",e) # NameError

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
	return saldo - self.jumlah (hanya return jika saldo cukup)

'''
'''latihan'''

class DompetError(Exception):
    pass

class SaldoTidakCukup(DompetError):
    pass
class InputError(DompetError):
	pass
class PenerimaError(DompetError):
	pass

class Transaksi:
    def proses(self, saldo):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError

class Setor(Transaksi):
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self, saldo):
        if self.jumlah <= 0:
        	raise InputError("Nominal Harus lebih dari 0")
        return saldo + self.jumlah

    def info(self):
        return f"SETOR {self.jumlah}"

class Tarik(Transaksi):
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self, saldo):
        if saldo < self.jumlah:
            raise SaldoTidakCukup("Saldo tidak mencukupi")
        return saldo - self.jumlah

    def info(self):
        return f"TARIK {self.jumlah}"

class Riwayat:
    def __init__(self):
        self._data = []

    def tambah(self, info):
        self._data.append(info)

    def tampilkan(self):
        return self._data.copy()

class Dompet:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
        self.riwayat = Riwayat()

    def proses(self, transaksi):
        saldo_awal = self.saldo
        try:
            saldo_baru = transaksi.proses(self.saldo)
        except DompetError as e:
            print("Transaksi gagal:", e)
            return  # sistem berhenti rapi

        # hanya jika sukses
        self.saldo = saldo_baru
        self.riwayat.tambah(transaksi.info())

dompet = Dompet("Haikal",1000)
try:
	dompet.proses(Tarik(1001))
except SaldoTidakCukup() as e:
	print ("Error : ",e)
dompet.proses(Tarik(1001))
dompet.proses(Setor(-7))

'''gambaran kodingan asli Exception yang menjadi baseclass asli'''

class BaseException:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        if not self.args:
            return ""
        if len(self.args) == 1:
            return str(self.args[0])
        return str(self.args)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.args}" # self.__class__.__name,__ untuk mengakses nama class


class Exceptio(BaseException): # boleh pass,boleh diisi

	def __init__(self,message):
		self.message = message
		super().__init__(message)
'''
• *args : semua nilai yang dibuat saat bikin Exception.

raise Exceptio("Saldo Kurang")

"Saldo Kurang adalah *args nya,bisa dicek dengan kode dibawah

• self.args[0]
Mayoritas exception hanya memiliki 1 pesan error utama,jadi:
args[0] adalah pesan
str(e) pesan itu juga

bisa dicek dengan kode dibawah

• super().__init__(message)
fungsinya untuk mengisi custom exception milik Exception

kalau tidak pakai super()
str(e) kosong

args[0] kosong

jadi alurnya gini,contoh

class Exceptio('SaldoBocor')
'SaldoBocor' masuk ke init Exceptio (dia menjadi message)

selanjutnya dibawahnya ada kode super().__init__(message)

maksudnya:

si 'SaldoBocor' dikirim ke class BaseException dan disana dia menjadi *args
itulah kenapa args[0] isinya pesan tersebut
'''

print (Exceptio("Saldokurang").args)
e = Exceptio("SaldoKurang")
print(str(e)) # SaldoKurang
print(e.args[0]) # SaldoKurang
print(repr(e))
print ('e adalah instance dari  ',e.__class__) #-> mengecek ,hasilnya adalah e merupakah instance dari class Exception
print ('Nama class e adalah ',Exceptio.__name__) #-> mengecek nama class,dan ini hanya punya class,bukan instance

'''latihan'''

class GudangError(Exception):
	pass

class BarangTidakAda(GudangError):

	def __init__(self,nama_barang):
		self.nama_barang = nama_barang
		super().__init__(f"{self.nama_barang} Tidak ada")

class StokTidakCukup(GudangError):

	def __init__(self,nama_barang,stok,diminta):
		self.nama_barang = nama_barang
		self.stok = stok
		self.diminta = diminta
		super().__init__(f"stok {self.nama_barang} tidak cukup, tersisa {self.stok},diminta {self.diminta}")


class Gudang:

	def __init__(self):
		self.stok = {
		"Jeruk":10,
		"Nanas":15
		}

	def ambil(self,nama_barang,jumlah):
		if nama_barang not in self.stok:
			raise BarangTidakAda(nama_barang)
		if self.stok[nama_barang] < jumlah:
			raise StokTidakCukup(nama_barang,self.stok[nama_barang],jumlah)

		self.stok[nama_barang] -= jumlah

gudang = Gudang()

try:
	gudang.ambil("Apel",10)

except GudangError as e:
	print ("Error : ",e)

'''latihan gabungan'''


class Transaksi:
	def proses(self,saldo):
		raise NotImplementedError

class Transfer(Transaksi):

	def __init__(self,penerima,jumlah):
		self.penerima = penerima
		self.jumlah = jumlah
		self.fee = 250
	def proses(self,saldo):
		if self.jumlah < 0:	
			raise InputError("InputTidakBolehNegatif")

		if self.penerima is None:
			raise PenerimaError("PenerimaTidakDitemukan")

		total = self.jumlah + self.fee
		if total > saldo:
			raise SaldoTidakCukup("SaldoTidakMencukupi")
		
		
		saldo -= (self.jumlah + self.fee)
		self.penerima.saldo += self.jumlah
		return saldo



class Dompet:

	def __init__(self,nama,saldo):
		self.nama = nama
		self.saldo = saldo

	def proses(self,transaksi):
		saldo_awal = self.saldo
		saldo_baru = transaksi.proses(self.saldo)
		self.saldo = saldo_baru

Haikal = Dompet("Haikal",5000)
KeyChan = Dompet("KeyChan",5000)
Haikal.proses(Transfer(KeyChan,60))
print (KeyChan.saldo)
try:
	KeyChan.proses(Transfer(Haikal,8000))
except DompetError as e:
	print ("Error : ",e)
print (Haikal.saldo)
print (KeyChan.saldo)

'''from e'''
class TransaksiError(DompetError):
	pass

class Transaksi:
    def proses(self, saldo):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError

class Setor(Transaksi):
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self, saldo):
        if self.jumlah <= 0:
        	raise InputError("Nominal Harus lebih dari 0")
        return saldo + self.jumlah

    def info(self):
        return f"SETOR {self.jumlah}"

class Tarik(Transaksi):
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self, saldo):
        if saldo < self.jumlah:
            raise SaldoTidakCukup("Saldo tidak mencukupi")
        return saldo - self.jumlah

    def info(self):
        return f"TARIK {self.jumlah}"

class Dompet:
	def __init__(self,nama,saldo):
		self.nama = nama
		self.saldo = saldo

	def proses(self,transaksi):
		try:
			self.saldo = transaksi.proses(self.saldo)
		except TransaksiError as e:
			raise DompetError (f"Transaksi Error pada dompet {self.nama}") from e

HuTao = Dompet('HuTao',5000)
try:
	HuTao.proses(Tarik(6000))
except DompetError as e:
	print ("Error : ",e)
	print ("Penyebab : ",e.__cause__)

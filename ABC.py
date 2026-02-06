'''ABC'''
from abc import ABC, abstractmethod

class DompetError(Exception):
	pass
class saldokurang(DompetError):
	pass
class inputerror(DompetError):
	pass
class penerimaerror(DompetError):
	pass

class Transaksi(ABC):
	def __init__(self,jenis,nominal):
		if jenis not in ("SETOR","TARIK","TRANSFER"):
			raise inputerror("Transaksi tidak tersedia")
		if nominal <= 0:
			raise inputerror("Perbaiki Nominal")
		self.jenis = jenis
		self.nominal = nomimal

	@abstractmethod
	def proses (self,saldo):
		pass

	@abstractmethod
	def info(self):
		pass

class Tarik(Transaksi):
	def __init__(self,jumlah):
		self.jumlah = jumlah

	def proses (self,saldo):
		if saldo < self.jumlah:
			raise saldokurang("SALDO TIDAK CUKUP!!!")
		return saldo - self.jumlah

	def info(self):
		return f"TARIK {self.jumlah}"


class Setor(Transaksi):
	def __init__(self,jumlah):
		self.jumlah = jumlah

	def proses (self,saldo):
		if self.jumlah <= 0:
			raise inputerror ("PERBAIKI NOMINAL!!!")
		return saldo + self.jumlah

	def info(self):
		return f"SETOR {self.jumlah}"

class Transfer(Transaksi):

	def __init__(self,penerima,jumlah):
		self.penerima = penerima
		self.jumlah = jumlah
		self.fee = 2000
	def proses (self,saldo):
		if self.jumlah + self.fee <= 0:
			raise inputerror("PERBAIKI NOMINAL!!!")
		elif self.jumlah + self.fee > saldo :
			raise saldokurang("SALDO TIDAK CUKUP!!!")
		if self.penerima is None:
			raise penerimaerror("PENERIMA TIDAK ADA!!!")

		saldo -=(self.jumlah + self.fee)
		self.penerima.saldo += self.jumlah
		return saldo

	def info(self):
		return f"TRANSFER {self.jumlah}"
class Dompet:

	def __init__(self,nama,saldo):
		self.nama = nama
		self.saldo = saldo

	def proses(self,transaksi):
		saldo_baru = transaksi.proses(self.saldo)
		self.saldo = saldo_baru

d1 = Dompet("Haikal",0)
d2 = Dompet("HuTao",0)
print ("Saldo pertama : ",d1.saldo)
d1.proses(Setor(10000))
print ("Saldo kedua : ",d1.saldo)
d1.proses(Transfer(d2,500))
print ("Saldo ketiga : ",d1.saldo)


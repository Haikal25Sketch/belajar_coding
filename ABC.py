'''ABC'''
from abc import ABC, abstractmethod

class DompetError(Exception):
	pass
class saldokurang(DompetError):
	pass
class inputerror(DompetError):
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
	def __init__(self,jumlah);
		self.jumlah = jumlah

	def proses (self,saldo):
		if saldo < self.jumlah:
			raise saldokurang("saldo tidak mencukupi")
		return saldo - self.jumlah

	def info (self):
		return f "TARIK {self.jumlah}"


class Setor(Transaksi):
	def __init__(self,jumlah):
		

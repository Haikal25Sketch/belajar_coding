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

	def __init__(self,saldo)
		self.saldo = saldo
		self.riwayat = Riwayat()



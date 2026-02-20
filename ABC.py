'''ABC'''
# Abc : merupakan class dasar yang tidak boleh dibuat objeknya langsung dan berfungsi sebagai kontrak untuk subclass.

# Dipakai untuk memaksa subclass mengimplementasikan method tertentu.

#Kenapa perlu ABC?
'''Supaya semua turunan punya struktur yang konsisten.
Tanpa ABC:
Subclass bisa lupa bikin method penting.
Program bisa error di runtime.
Dengan ABC:
Python akan memaksa method tertentu ada.
Kalau tidak, langsung error saat instansiasi.'''

#Kapan Dipakai?
'''Dipakai saat:
Kamu ingin struktur konsisten
Kamu ingin sistem modular
Kamu ingin mencegah subclass tidak lengkap
Tidak wajib selalu dipakai.'''

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
		total = self.jumlah + self.fee
		if total <= 0:
			raise inputerror("PERBAIKI NOMINAL!!!")
		elif total > saldo :
			raise saldokurang("SALDO TIDAK CUKUP!!!")
		if self.penerima is None:
			raise penerimaerror("PENERIMA TIDAK ADA!!!")

		saldo -=total
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
print (f"Saldo ketiga,Berasal dari dompet {d1.nama} : ",d1.saldo)

'''Factory Patern'''
#Factory Patern : satu pintu untuk membuat object,yang dimana logika pembuatan objek dipisahkan dari penggunaan objek

# Factory patern lahir dari masalah 'bagaimana jika sebuah permintaan itu datang bukan secara manual kita buat,tapi dari input user,config,API,atau file
'''latihan Factory patern'''

class Notifikasi(ABC):

	@abstractmethod
	def kirim(self,pesan):
		pass

class EmailNotif(Notifikasi):

	def __init__(self,tujuan):
		self.tujuan = tujuan

	def kirim (self,pesan):
		print (f"Mengirim Email ke {self.tujuan} : {pesan}")

class SmsNotif(Notifikasi):

	def __init__(self,tujuan):
		self.tujuan = tujuan

	def kirim (self,pesan):
		print (f"Mengirim Sms ke {self.tujuan} : {pesan}")


class PushNotif(Notifikasi):

	def __init__(self,tujuan):
		self.tujuan = tujuan

	def kirim (self,pesan):
		print (f"Mengirim NotifGit ke {self.tujuan} : {pesan}")


class NotifikasiFactory:

	@staticmethod
	def buat(jenis,**data):
		jenis = jenis.upper()

		if jenis == "EMAIL":
			return EmailNotif(data["tujuan"])
		elif jenis == "SMS":
			return SmsNotif(data["tujuan"])
		elif jenis == "GIT":
			return PushNotif(data["tujuan"])
		else:
			raise ValueError("Jenis notif tidak tersedia")


jenis = input("Masukkan jenis (email/sms/git): ")
tujuan = input("Masukkan tujuan: ")
pesan = input("Masukkan pesan: ")

notif = NotifikasiFactory.buat(
    jenis,
    tujuan=tujuan
)

notif.kirim(pesan)

print (type(notif))
print()
'''Composition'''
# Composition : Hubungan kepemilikan / Kerja sama
# Inheritance : Hubungan identitas (A anak B)

# Sistem Ai lebih sering menggunakan Composition dikarenakan ia adalah hasil rakitan komponen-komponen

#contoh dasar : mobil memiliki mesin
print("Ini adalah Composition")
class mesin :

	def nyala(self):
		print ("mesin hidup")

class mobil:

	def __init__(self,mesin):
		self.mesin = mesin # disini composition terjadi
	def nyala(self):
		self.mesin.nyala()

mesin_1 = mesin()
mobil_1 = mobil(mesin_1)
mobil_1.nyala() # output mesin hidup

#contoh lain 
#Notifikasi dengan pengirim
print()
print ("Latihan Composition")
class Pengirim(ABC):
    @abstractmethod
    def kirim(self, tujuan: str, pesan: str):
        pass
class PengirimEmail(Pengirim): 
    def kirim(self, tujuan, pesan):
        print(f"[Email] ke {tujuan} : {pesan}")

class PengirimSms(Pengirim):
    def kirim(self, tujuan, pesan):
        print(f"[Sms] ke {tujuan} : {pesan}")

class PengirimGit(Pengirim):
    def kirim(self, tujuan, pesan):
        print(f"[Git] ke {tujuan} : {pesan}")

class PengirimTelegram(Pengirim):
    def kirim(self, tujuan, pesan):
        print(f"[Telegram] ke {tujuan} : {pesan}")

class Notifikasi:
	def __init__(self,tujuan:str,pengirim:Pengirim): # type hint agar tidak bingung
		self.tujuan = tujuan
		self.pengirim = pengirim #ini adalah composition

	def kirim (self,pesan):
		self.pengirim.kirim(self.tujuan,pesan) # sekarang self.pengirim bisa mengakses method kirim dari class lain ya


email_sender = PengirimEmail()
sms_sender = PengirimSms()
git_sender = PengirimGit()
tele_sender = PengirimTelegram()
notif_1 = Notifikasi("Haikal",email_sender)
notif_2 = Notifikasi ("HuTao",sms_sender)

notif_1.kirim("Hai")
notif_2.kirim("Hai Haikal")

#Campur dengan Factory
print()
print ("Composition + Factory patern")
class NotifikasiFactory_2:

	@staticmethod
	def buat(jenis,tujuan):
		jenis = jenis.upper()

		if jenis == "EMAIL":
			pengirim = PengirimEmail() # pengirim disini adalah pengirim yang sama dengan parameter class Notifikasi
		elif jenis == "SMS":
			pengirim = PengirimSms()
		elif jenis == "GIT":
			pengirim = PengirimGit()
		elif jenis == "TELE":
			pengirim = PengirimTelegram()
		else:
			raise ValueError("Jenis pengirim tidak tersedia")

		return Notifikasi(tujuan,pengirim)

while True:
	jenis = input("Masukkan jenis (email/sms/git/tele): ")
	tujuan = input("Masukkan tujuan: ")
	pesan = input("Masukkan pesan: ")

	notif = NotifikasiFactory_2.buat(jenis,tujuan)
	notif.kirim(pesan)

	lanjut = input ("Lanjut atau tidak (y/n) : ")
	if lanjut == "n" or lanjut == "N":
		break

''' agar factory patern lebih bersih dari if elif else bisa juga gini
 class NotifikasiFactory_2:

   mapping = {
        "EMAIL": PengirimEmail,
        "SMS": PengirimSms,
        "GIT": PengirimGit,
        "TELE": PengirimTelegram
    }

    @staticmethod
    def buat(jenis, tujuan):
        jenis = jenis.upper()

        kelas_pengirim = NotifikasiFactory_2.mapping.get(jenis)

        if not kelas_pengirim:
            raise ValueError("Jenis pengirim tidak tersedia")

        return Notifikasi(tujuan, kelas_pengirim()) 
'''

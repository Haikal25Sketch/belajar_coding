'''Robust Pipeline'''
#Robust pipeline : Robust yang berarti kokoh,dan pipeline yang berarti alur proses data
# Robust pipeline ialah alur data yang kokoh,dia bukan tidak error tetapi:
'''
•Sistem stabil
•Kesalahan tidak disembunyikan
•Informasi yang benar
'''


import random 
class ValidNilai:
    def __set_name__(self, owner, data):
        self.data = data

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Data harus berupa list")

        for v in value:
            if not isinstance(v, (int, float)):
                raise TypeError("Semua nilai harus angka")
            if v < 0 or v > 100:
                raise ValueError("Nilai harus antara 0 dan 100")

        instance.__dict__[self.data] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.data)
        
class DataLoader:
    data = ValidNilai()
    def __init__(self,data):
        self.data = data

    def get(self):
        print ("[INFO] GET A DATA...")
        return self.data

def transform (data):
    print ("[INFO] TRANSFORM A DATA...")
    return [num / 100 for num in data]

class Decision:

    def __init__(self,prob=0.5,seed =99):
        if not 0 <= prob <= 1:
            raise ValueError("Prob harus antara 0 dan 1 ")
        self.prob = prob
        self.num = random.Random(seed) # agar hasil random bisa diulang,dan lebih baik ditaruh di dalam saja agar tidak dipakai di seluruh tugas
#self.num menjadi object dari class Random
    def proses(self,data):
        print ("[INFO] RUNNING A MODEL...")
        hasil = []
        for num in data:
            if num >= 0.85:
                hasil.append("DITERIMA")
            elif 0.70 <= num < 0.85:
                hasil.append("DITERIMA") if self.num.random() < self.prob  else hasil.append("DITOLAK")
            else :
                hasil.append("DITOLAK")
        return hasil

def Hasil (data):
    print ("[INFO] GET A RESULT...")
    hasil = {
    "Diterima":data.count("DITERIMA"),
    "Ditolak":data.count("DITOLAK")
    }

    return hasil


class Alur:
    def __init__(self,data,transform,decision,result):
        self.data = data
        self.transform = transform
        self.decision = decision
        self.result = result

    def proses (self):
        raw_data = self.data.get()
        transformer =self.transform2(raw_data)
        model = self.decision.proses(cleaner)
        hasil = self.result (model)
        return hasil

data =[76,98,65,44,56,70,98,76,55,67]
Pipeline = Alur(DataLoader(data),transform,Decision(),Hasil)
print ("Hasil penerima beasiswa : ",Pipeline.proses())

print()

'''Belajar logger'''
# Logging : Cara mencatat kejadian di program secara terstruktur.
'''Bukan sekadar print. Tapi bisa:
•dikasih level
•dikirim ke file
•difilter
'''

'''
PERBEDAAN PRINT DAN LOGGER
print("Halo") → selalu tampil di layar → tidak bisa dikontrol

logger.info("Halo") → bisa disembunyikan → bisa dikirim ke file → bisa dibedakan tingkat pentingnya
'''

'''
LEVEL LOGGER

DEBUG: Detail internal (10) -> nilai var,saldo sebelum sesudah....
INFO: Event normal (20) -> berhasil login,berhasil masuk....
WARNING: Ada keanehan (30) -> login gagal 3x....
ERROR: Gagal (40) saldo kurang,input bukan angka....
CRITICAL: Sistem rusak parah (50)
'''

'''IMPLEMENTASI DASAR'''
'''import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

logging.debug("Saldo sebelum transaksi: 1000")
logging.info("Transfer berhasil")
logging.warning("Percobaan login gagal 3x")
logging.error("Saldo tidak cukup")
logging.critical("Database tidak bisa diakses")'''
'''

logging.basicConfig() itu untuk:
Setup awal logging
Atur level -> level =
Atur tujuan output -> filename =
Atur format -> format =
Dia bukan logger. Dia bukan method untuk mencatat log. Dia cuma konfigurator awal.
'''

'''
CATATAN

basicConfig() hanya bekerja kalau logging BELUM dikonfigurasi.
Kalau sudah pernah dipanggil sekali, pemanggilan berikutnya diabaikan.
'''
# Saat produksi sistem ,biasanya DEBUG tidak diaktifkan,ia hanya diaktifkan saat troubleshoot agar sistem tidak lemot
# yang biasanya dijalankan adalah INFO ke atas

'''Komponen utama logger
• Logger : Otaknya
• Handler : Jalur keluarnya
• Formatter : Bentuk Outputnya
'''
# Handler itu yang memutuskan output akan dikeluarkan kemana,logger yang mengirim pesan

'''Jenis jenis Handler
• StreamHandler : Output ke terminal / console
• FileHandler : output ke file, contoh error.log
• RotatingFileHandler: Versi lebih pintar dari FileHandler.
Kalau file log terlalu besar:
-otomatis buat file baru
-file lama disimpan
-bisa batasi ukuran
Ini penting banget di production.
• TimedRotatingFileHandler
Mirip rotating, tapi berdasarkan waktu.
Contoh:
-setiap hari buat file baru
-setiap jam buat file baru
• NullHandler
Tidak melakukan apa-apa.
Biasanya dipakai di library supaya tidak mengganggu logger utama.
'''

'''contoh implementasi multiple handler'''
'''import logging

logger = logging.getLogger("dompet")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Handler terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Handler file error
file_handler = logging.FileHandler("error.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# Pasang handler ke logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Transaksi berhasil")
logger.error("Saldo tidak cukup")'''



'''Penggunaan Logger pada Sistem dompet'''
from abc import ABC, abstractmethod

class DompetError(Exception):
    pass

class saldokurang(DompetError):
    pass

class inputerror(DompetError):
    pass

class penerimaerror(DompetError):
    pass


import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


class Transaksi(ABC):

    def __init__(self, jenis, nominal):
        if jenis not in ("SETOR", "TARIK", "TRANSFER"):
            logger.error("Jenis transaksi tidak tersedia")
            raise inputerror("Transaksi tidak tersedia")

        if nominal <= 0:
            logger.error("Nominal tidak valid")
            raise inputerror("Perbaiki Nominal")

        self.jenis = jenis
        self.nominal = nominal

    @abstractmethod
    def proses(self, saldo):
        pass

    @abstractmethod
    def info(self):
        pass


class Tarik(Transaksi):

    def __init__(self, jumlah):
        super().__init__("TARIK", jumlah)
        self.jumlah = jumlah

    def proses(self, saldo):

        logger.info(f"Memproses TARIK {self.jumlah}")

        if saldo < self.jumlah:
            logger.error(
                f"Gagal tarik | saldo={saldo} | tarik={self.jumlah}"
            )
            raise saldokurang("SALDO TIDAK CUKUP!!!")

        saldo_baru = saldo - self.jumlah

        logger.info(
            f"Tarik berhasil | saldo_lama={saldo} | saldo_baru={saldo_baru}"
        )

        return saldo_baru

    def info(self):
        return f"TARIK {self.jumlah}"


class Setor(Transaksi):

    def __init__(self, jumlah):
        super().__init__("SETOR", jumlah)
        self.jumlah = jumlah

    def proses(self, saldo):

        logger.info(f"Memproses SETOR {self.jumlah}")

        if self.jumlah <= 0:
            logger.error("Nominal setor tidak valid")
            raise inputerror("PERBAIKI NOMINAL!!!")

        saldo_baru = saldo + self.jumlah

        logger.info(
            f"Setor berhasil | saldo_lama={saldo} | saldo_baru={saldo_baru}"
        )

        return saldo_baru

    def info(self):
        return f"SETOR {self.jumlah}"


class Transfer(Transaksi):

    def __init__(self, penerima, jumlah):
        super().__init__("TRANSFER", jumlah)
        self.penerima = penerima
        self.jumlah = jumlah
        self.fee = 2000

    def proses(self, saldo):

        logger.info(
            f"Memproses TRANSFER {self.jumlah} ke {self.penerima.nama if self.penerima else 'UNKNOWN'}"
        )

        total = self.jumlah + self.fee

        if total <= 0:
            logger.error("Nominal transfer tidak valid")
            raise inputerror("PERBAIKI NOMINAL!!!")

        if total > saldo:
            logger.error(
                f"Gagal transfer | saldo={saldo} | total_transfer={total}"
            )
            raise saldokurang("SALDO TIDAK CUKUP!!!")

        if self.penerima is None:
            logger.error("Penerima tidak ditemukan")
            raise penerimaerror("PENERIMA TIDAK ADA!!!")

        saldo -= total
        self.penerima.saldo += self.jumlah

        logger.info(
            f"Transfer berhasil | jumlah={self.jumlah} | fee={self.fee} | saldo_sisa={saldo}"
        )

        return saldo

    def info(self):
        return f"TRANSFER {self.jumlah}"


class Dompet:

    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

        logger.info(f"Dompet dibuat | nama={self.nama} | saldo_awal={self.saldo}")

    def proses(self, transaksi):

        logger.info(
            f"{self.nama} menjalankan transaksi {transaksi.info()}"
        )

        saldo_baru = transaksi.proses(self.saldo)

        logger.debug(
            f"Update saldo | lama={self.saldo} | baru={saldo_baru}"
        )

        self.saldo = saldo_baru

d1 = Dompet('Haikal',0)
d2 = Dompet('HuTao',1000)
d1.proses(Setor(80))

#Urutan Logger
'''
Start -> logger.info (Info bahwa user sedang melalakukan aksi)
Validasi -> Apakah aksinya berhasil,jika gagal logger.Error
Success -> logger.info(user berhasil melakukan aksi
'''

# fungsi __name__ pada logging.getLogger(__name__) adalah untuk memberinama log sesuai dengan nama file,contoh pipeline.py ,nama log nya adalah pipeline

# jika di proyek kecil tidak apa jika memasukkan file² kedalam 1Log,tapi jika sudah masuk tahap besar harus dilakukan pemisahan log berdasarkan levelnya dan berdasarkan modul

# contoh jika filenya pipeline.py maka lognya pipeline.log 

'''Pipeline & Modular system'''
# Pipeline = alur kerja berantai
# contoh sederhana :
# input -> preprocess -> model -> postprocess -> output
#Setiap tahap:
'''Punya tugas spesifik
•Tidak tahu detail tahap lain
•Fokus pada satu kerjaan

Itulah modular system.
'''
#Kenapa ini penting banget buat AI?
#Karena di dunia nyata:
'''•Data mentah tidak bisa langsung masuk model
•Model tidak bisa langsung jadi output final
•Harus ada pembersihan
•Harus ada normalisasi
•Harus ada format ulang

Semua itu dipisah jadi komponen.
'''
#contoh gambaran pipeline sederhana dalam ai

class Preprocess:
	def proses(self,data):
		print ("Preprocessing data...")
		return data.lower()

class Model:
	def prediksi(self, data):
		print ("Model memproses data...")
		return f"Prediksi dari '{data}'"

class Postprocess:
    def proses(self, hasil):
        print("Postprocessing hasil...")
        return hasil.upper()


class Pipeline:
	def __init__(self,preprocess,model,postprocess): # disini composition dilakukan
		self.preprocess = preprocess
		self.model = model
		self.postprocess = postprocess

	def jalankan(self,data): # semua tersambung lewat alur data,tapi memiliki tugasnya masing masing
		data_bersih = self.preprocess.proses(data)
		hasil_model = self.model.prediksi (data_bersih)
		hasil_final = self.postprocess.proses(hasil_model)

		return hasil_final


# pemakaian
pipeline = Pipeline(
    Preprocess(),
    Model(),
    Postprocess()
)

output = pipeline.jalankan("Halo Dunia")
print("Output akhir:", output)
print()


'''latihan'''
class Cleaner: # mengubah teks menjadi lower case dan menghapus spasi berlebih
	def proses (self,data):
		print ("Memproses data ...")
		lower = data.lower()
		bersih = lower.strip()
		return bersih

class Analyzer : # mengitung jumlah karakter dan kata dari data
	def proses (self,data):
		print ("Menganalisa data ...")
		hasil = {
		"data": data,
		"jumlah_karakter":len(data),
		"jumlah_kata": len(data.split())
		}
		return hasil

class Formatter: # mwngeluarkan hasil Analyzer
	def proses(self,data):
		print ("Preprocessing hasil...")
		hasil =""
		for key,value in data.items():
			hasil += f"\n{key} : {value}"
		return hasil

class Pipeline:
	def __init__(self,cleaner,analyzer,formatter):
		self.cleaner = cleaner
		self.analyzer = analyzer
		self.formatter = formatter

	def jalankan(self,data):
		data_bersih = self.cleaner.proses(data)
		hasil_model = self.analyzer.proses(data_bersih)
		hasil_final = self.formatter.proses(hasil_model)

		return hasil_final


pipeline = Pipeline(Cleaner(),Analyzer(),Formatter())
output = pipeline.jalankan("SAya MenCintAi HuTao sepanjang HiDup saya")
print ("Output : ",output)

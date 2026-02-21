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
output = pipeline.jalankan("       SAya MenCintAi HuTao sepanjang HiDup saya")
print ("Output : ",output)

print()
'''pipeline + descriptor'''

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

class lengthstring:

    def __set_name__(self,owner,data):
        self.data = data

    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise TypeError("Nilai harus string")
        if value.strip() == "":
            raise ValueError("Nilai tidak boleh kosong")
        if len(value) >40:
            raise ValueError("Tidak boleh lebih dari 10 karakter")
        instance.__dict__[self.data] = value

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.data)

    def __delete__(self,instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.data]

class Pipeline:
    data = lengthstring()
    def __init__(self,cleaner,analyzer,formatter,data):
        self.cleaner = cleaner
        self.analyzer = analyzer
        self.formatter = formatter
        self.data = data
    def jalankan(self):
        data_bersih = self.cleaner.proses(self.data)
        hasil_model = self.analyzer.proses(data_bersih)
        hasil_final = self.formatter.proses(hasil_model)

        return hasil_final


pipeline = Pipeline(Cleaner(),Analyzer(),Formatter(),"    Hai NaMAKu Haikal   ")
output = pipeline.jalankan()
print (output)
print()

'''Latihan pipeline 2'''
class DataLoader:
	def __init__(self,data):
		self.data = data
		self.batas = 0
		
	def load(self):
		print ("Memuat data...")
		return self.data

class Preprocessor:
	def proses(self,data:list):
		print ("Mengolah data...")
		lower =[]
		for word in data:
			hasil = word.lower()
			lower.append(hasil)
		return lower

class Model:
	def prediksi(self,data:list):
		print ("Menganalisa data...")
		hasil = ["POSITIF" if "bagus" in x.lower() else
		"NEGATIF" if "jelek" in x.lower() else "NETRAL"
		for x in data]

		return hasil


class Evaluator:
	def proses(self,data):
		hasil = {
		"positif":data.count("POSITIF"),
		"negatif":data.count("NEGATIF"),
		"netral":data.count("NETRAL")
		}
		return hasil

class Pipeline:
	def __init__(self,loader,preprocess,model,evaluator):
		self.loader = loader
		self.preprocess = preprocess
		self.model = model
		self.evaluator = evaluator

	def proses(self):
		data_mentah = self.loader.load()
		data_baru = self.preprocess.proses(data_mentah)
		hasil_model = self.model.prediksi(data_baru)
		hasil_final = self.evaluator.proses(hasil_model)

		return hasil_final
data = ["Data bagus","Data jelek","Data bagus","Data jelek","Data netral"]
pipeline = Pipeline(DataLoader(data),Preprocessor(),Model(),Evaluator())
output = pipeline.proses()
print ("Hasil final :\n",output)

class AkunBank:
  __BankName = " Loli Bank Nasional"

  def __init__(self,nama,nomer_rekening,pin:str,saldo): #Settingan 
    self.__nama = nama
    self.__pin =str(pin)
    self.__saldoAwal = 0
    self.__saldo =int(saldo)
    self.__rekening = nomer_rekening

  def __str__(self):
    return f"Akun ini milik {self.__nama} nomer rekeningnya {self.__rekening}"

  def __repr__(self):
    return f"AkunBank( \nnama\t : {self.__nama} \npin\t : {self.__pin} \nsaldo\t : {self.__saldo} \nno.rek\t : {self.__rekening})"
 
  @staticmethod
  def pin_validation(pin): #Validasi pin harus 4 angka
    """pin harus 4 digit angka"""
    return isinstance(pin,str) and pin.isdigit() and len(pin)==4

  @property
  def saldo(self): #property yang mengembalikan saldo
    return self.__saldo
  @property
  def nama(self):
    return self.__nama
  
  @saldo.setter
  def saldo(self, nominal):
    if nominal < 0:
        raise ValueError("Saldo tidak boleh negatif")
    self.__saldo = nominal

  def setor(self,jumlah): # Fungsi untuk setor uang
    if jumlah > 0:
      self.__saldo += jumlah
      return (f'Saldo Rp.{jumlah} sudah disetor')
    else:
      print ("Input tidak boleh 0 dan minus")

  def tarik(self,jumlah): # Fungsi untuk tarik uang
    if jumlah > 0 and self.__saldo >= jumlah:
      self.__saldo -= jumlah
    else:
      print ('Saldo Tidak Cukup')

  def transfer(self,nama,nominal): #Fungsi untuk Transfer uang
    if nominal <= 0  :
      print ('Tidak bisa mengirim 0')
      return

    if nominal > self.__saldo:
      print ('Saldo anda tidak cukup')
      return

    if not isinstance(nama,AkunBank):
      print('penerima tidak terdaftar')
      return

    self.__saldo -= nominal
    nama.__saldo += nominal

    print (f'Transfer {nominal} ke {nama.nama} berhasil dilakukan.')
  @classmethod
  def dari_string(cls,line): #membuat akun dari string
    nama,nomer_rekening,pin,saldo = line.split("|")
    return cls(nama.strip(),nomer_rekening.strip(),pin.strip(),int(saldo.strip()))



haikal = AkunBank('Haikal',176545,"1707",0) # membuat akun biasa dengan __init__
hutao = AkunBank('HuTao',175455,"7071",1)
string = "Nahida|175645|'7887'|2" #membuat akun dari string
nahida = AkunBank.dari_string(string)
print (nahida)

print ('Sisa saldo haikal :',haikal.saldo) # pengecekan saldo
try:
  haikal.saldo =-2000 # set saldo dengan saldo.setter
except ValueError as e:
  print ("Errror Terdeteksi : ",e) # 
print ('Jumlah saldo haikal setelah di set  :',haikal.saldo) #pengecekan saldo dengan saldo.getter
haikal.saldo = 20000 # set saldo normal
print ('Jumlah saldo haikal setelah di set :',haikal.saldo) #pengecekan saldo normal
haikal.pin_validation("1707")
print ('Validasi pin 1707 :',AkunBank.pin_validation(1707)) #validasi pin
print ('Validasi pin 894a :',AkunBank.pin_validation("894a"))
print ('Validasi pin "1707" :',AkunBank.pin_validation("1707"))

haikal.setor(25000)
print ('Jumlah saldo haikal setelah melakukan penyetoran :',haikal.saldo) #instance method setor
try:
  haikal.setor(-78)
except ValueErrror as e:
  print ("Errror Terdeteksi : ",e)
haikal.tarik(25000) #instance method tarik
print ('Sisa saldo haikal setelah melakukan penarikan :',haikal.saldo)
haikal.tarik(80000)
hutao.transfer(haikal,70)
print (haikal)
print (repr(haikal))




'''CLI(Command Line Interface'''
#CLI : cara berinteraksi dengan sistem menggunakan teks
#Di Termux:
#User bicara ke shell (biasanya bash).(shell = penghubung antara user dengan sistem)
#Shell meneruskan perintah ke OS.
#OS menjalankan program.
'''urutannya
user -> shell -> sistem -> program
'''
#contoh:
# kamu punya file hello.py yang berisi print("hello"),kamu ketik di shell,python hello.py dan keluarlah hello
# itu tidak instan,yang sebenarnya terjadi adalah:
'''
Shell cari program bernama python

Python dijalankan

Python membaca hello.py

Python mengeksekusi baris demi baris
'''
# ada command pwd,cd,ls
#pwd untuk menampilkan di folder mana kamu sekarang
# cd untuk berpindah posisi folder
# ls untuk menampilkan isi folder
# cd /data/data/com.termux/files/home/..... -> tambahkan nama folder untuk langsung pindah antar folder

'''GIT & Version Control
git : sistem pencatat sejarah perubahan code
version control : sistem yang:
Menyimpan snapshot perubahan

Bukan menyimpan ulang seluruh file

Bisa kembali ke masa lalu

Bisa membandingkan perubahan

Bisa bercabang tanpa rusak
'''

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

command git:
•git init : untuk membuat repo di folder yang ditandai dengan .git saat kita mengeceknya dengan ls -a di folder tersebut

•git status : mengecek kondisi repo saat ini,apakah ada yang berubah,ditambah,dihapus,atau ada file baru yang ditambahkan

•git add . / git add nama_file : menentukan file mana yang mau dicatat

•git commit : menyimpan snapshot, commit = checkpoint



•git log : melihat sejarah perubahan pada file

•git checkout : untuk kembali ke masa lalu,caranya:
1.git log --oneline : untuk melihat kode commit

2.git checkout <kode_commit> :  kembali ke kode yang dulu
jika kamu kembali ke kode dulu dan melakukan perbaikan dan kamu ingin menyimpannya menjadi sebuah branch baru kamu bisa mengetik git checkout -b nama-branch-baru

3.git checkout main: kembali ke masa sekarang


•git diff : untuk melihat perbedaan atau perubahan yang terjadi pada file di dalam repositori kamu. 

Jika git status hanya memberi tahu file mana yang berubah, git diff menunjukkan baris mana yang ditambah, dihapus, atau dimodifikasi secara mendetail.

•git diff --staged : Untuk melihat perubahan yang sudah masuk ke area "staging" (siap untuk di-commit)

git diff <kode_commit1> <kode_commit2> : memlihat apa saja yang berubahdi kedua checkpoint itu


•git restore : untuk membatalkan perubahan pada file di folder kerjamu yang belum di-commit. caranya git restore <nama_file>


•git revert : digunakan untuk membatalkan efek dari sebuah commit lama dengan cara membuat commit baru yang isinya adalah kebalikan dari commit tersebut. caranya git revert <kode_commit>'''


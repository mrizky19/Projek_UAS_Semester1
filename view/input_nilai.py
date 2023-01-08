from model import daftarNilai

class inputNilai():
    def input_data(loop):
            print ("\n================Masukkan Data Mahasiswa================")
            while(loop == "y"):
                nama = input("Nama   : ")
                nim = int(input("NIM    : "))
                tugas = int(input("Tugas  : "))
                uts = int(input("UTS    : "))
                uas = int(input("UAS    : "))
                nilaiAkhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
                KEY = nim
                daftarNilai.tambah_data(KEY, nama, nim, tugas, uts, uas, nilaiAkhir)
                loop = input("Lanjut input data? (y/t) = ")
            while(loop == "t"):
                break
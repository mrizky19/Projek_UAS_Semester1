import view
class daftarNilai():
    def __init__(self):
        self.mahasiswa = {}

    def tambah_data(KEY, nama, nim, tugas, uts, uas, nilaiAkhir):
        data = dict.fromkeys(mydict.mahasiswa.keys())
        data["nama"] = nama
        data["nim"] = nim
        data["tugas"] = tugas
        data["uts"] = uts
        data["uas"] = uas
        data["nilaiAkhir"] = nilaiAkhir
        mydict.mahasiswa.update({KEY:data})

    def ubah_data():
        nims = int(input("Masukkan NIM :"))
        if nims in (mydict.mahasiswa.keys()):
            print("pilih data yang ingin di ubah")
            ubah = int(input("[(1)Nama, (2)Tugas, (3)Nilai UTS (4)Nilai UAS] Ketikan angkanya : "))
            if ubah == 1:
                newNama = input("Masukkan Nama Baru : ")
                mydict.mahasiswa[nims]["nama"] = newNama
            elif ubah == 2:
                newTugas = int(input("Masukkan nilai Tugas yang baru : "))
                mydict.mahasiswa[nims]["tugas"] = newTugas
                newNilaiAkhir = (mydict.mahasiswa[nims]["tugas"] * 30/100) + (mydict.mahasiswa[nims]["uts"] * 35/100) + (mydict.mahasiswa[nims]["uas"] * 35/100) 
                mydict.mahasiswa[nims]["nilaiAkhir"] = newNilaiAkhir
            elif ubah == 3:
                newUts = int(input("Masukkan nilai UTS yang baru : "))
                mydict.mahasiswa[nims]["uts"] = newUts
                newNilaiAkhir = (mydict.mahasiswa[nims]["tugas"] * 30/100) + (mydict.mahasiswa[nims]["uts"] * 35/100) + (mydict.mahasiswa[nims]["uas"] * 35/100) 
                mydict.mahasiswa[nims]["nilaiAkhir"] = newNilaiAkhir
            elif ubah == 4:
                newUas = int(input("Masukkan nilai UAS yang baru : "))
                mydict.mahasiswa[nims]["uas"] = newUas
                newNilaiAkhir = (mydict.mahasiswa[nims]["tugas"] * 30/100) + (mydict.mahasiswa[nims]["uts"] * 35/100) + (mydict.mahasiswa[nims]["uas"] * 35/100) 
                mydict.mahasiswa[nims]["nilaiAkhir"] = newNilaiAkhir
        else:
            print("NIM yang anda masukkan belum ada")



    def hapus_data():
        nims = int(input("Masukkan NIM : "))
        if nims in (mydict.mahasiswa.keys()):
            delet = input("Yakin data akan di hapus? (y/t) : ")
            if delet == "y":
                del mydict.mahasiswa[nims]
            else:
                print("Data tidak jadi dihapus")
        else:
            print("NIM yang anda masukkan belum ada")
    
    def cari_data():
        nims = int(input("Masukkan NIM : "))
        if nims in (mydict.mahasiswa.keys()):
            view.cetak_hasil_pencarian(nims)
        else:
            print("NIM yang anda masukkan belum ada")


mydict = daftarNilai()
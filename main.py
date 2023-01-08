from view import view_nilai, input_nilai
from model.daftar_nilai import daftarNilai

while True:
    print('{0:^46}'.format("PROGRAM INPUT DATA MAHASISWA"))
    print('{0:^46}'.format("="*46))
    print("[(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar]")
    pilihan = input("\n Pilih Opsi = ")

    if pilihan.lower() == "t":
        input_nilai.inputNilai.input_data("y")
    elif pilihan.lower() == "u":
        daftarNilai.ubah_data()
    elif pilihan.lower() == "h":
        daftarNilai.hapus_data()
    elif pilihan.lower() == "c":
        daftarNilai.cari_data()
    elif pilihan.lower() == "l":
        view_nilai.cetak_daftar_nilai()
    elif pilihan.lower() == "k":
        break
    else:
        print("Opsi yang anda inputkan tidak ada di menu")

    
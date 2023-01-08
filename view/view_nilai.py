from model import daftar_nilai

def cetak_daftar_nilai():
    no = 0
    print("\n")
    print(f"{'TABEL DATA MAHASISWA':^75}")
    print("╭────┬──────────────────┬─────────┬───────┬───────┬───────┬───────────────╮")
    print(f"│{'NO':^4}│{'Nama':^18}│{'NIM':^9}│{'Tugas':^7}│{'UTS':^7}│{'UAS':^7}│{'Nilai Akhir':^15}│")
    print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

    for nim in mydict.mahasiswa:
        no += 1 
        KEY = nim 

        NAMA = mydict.mahasiswa[KEY]["nama"]
        NIM = mydict.mahasiswa[KEY]["nim"]
        TUGAS = mydict.mahasiswa[KEY]["tugas"]
        UTS = mydict.mahasiswa[KEY]["uts"]
        UAS = mydict.mahasiswa[KEY]["uas"]
        AKHIR = mydict.mahasiswa[KEY]["nilaiAkhir"]

        print(f"│{no:^4}│{NAMA:^18}│{NIM:^9}│{TUGAS:^7}│{UTS:^7}│{UAS:^7}│{AKHIR:^15}│")
        print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")
    
    print("╰────┴──────────────────┴─────────┴───────┴───────┴───────┴───────────────╯")
    print("\n")

def cetak_hasil_pencarian(nims):
    print(f"{'TABEL PENCARIAN DATA MAHASISWA':^75}")
    print("╭────┬──────────────────┬─────────┬───────┬───────┬───────┬───────────────╮")
    print(f"│{'NO':^4}│{'Nama':^18}│{'NIM':^9}│{'Tugas':^7}│{'UTS':^7}│{'UAS':^7}│{'Nilai Akhir':^15}│")
    print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

    no = 1
    KEY = nims

    NAMA = mydict.mahasiswa[KEY]["nama"]
    NIM = mydict.mahasiswa[KEY]["nim"]
    TUGAS = mydict.mahasiswa[KEY]["tugas"]
    UTS = mydict.mahasiswa[KEY]["uts"]
    UAS = mydict.mahasiswa[KEY]["uas"]
    AKHIR = mydict.mahasiswa[KEY]["nilaiAkhir"]

    print(f"│{no:^4}│{NAMA:^18}│{NIM:^9}│{TUGAS:^7}│{UTS:^7}│{UAS:^7}│{AKHIR:^15}│")
    print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")  
    print("╰────┴──────────────────┴─────────┴───────┴───────┴───────┴───────────────╯")
    print("\n")


mydict = daftar_nilai.mydict
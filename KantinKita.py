import os
from datetime import datetime
import functools
from DataStructure import *
from MenuKantinKita import *

def clear():
    os.system('cls')

def createPesanan():
    clear()
    pesanan = []
    nama = input("Masukkan Nama Pemesan: ").lower()
    pesanan.append(nama)
    menu = []
    lagi = 'y'
    while lagi == 'y':
        print("[1] Makanan")
        print("[2] Minuman")
        pil = int(input("Pilih disini >>> "))
        print()
        if pil == 1:
            for i, j in zip(Makanan.keys(), Makanan.values()):
                print(f"[{i}] {j[0]:<13}: Rp. {j[1]:,}") 
            pilMakanan = int(input("Pilih disini >>> "))
            print()
            menu.append(Makanan[pilMakanan])
            lagi = input("pilih menu lagi? [y/n]: ").lower()
        elif pil == 2:
            for i, j in zip(Minuman.keys(), Minuman.values()):
                print(f"[{i}] {j[0]:<13}: Rp. {j[1]:,}") 
            pilMinuman = int(input("Pilih disini >>> "))
            print()
            menu.append(Minuman[pilMinuman])
            lagi = input("pilih menu lagi? [y/n]: ").lower()
    pesanan.append(menu)
    queue.enqueue(pesanan)
    bst.insert(pesanan)
    print("[1] Cetak Nota")
    print("[2] Buat Pesanan Lain")
    print("[3] Kembali ke Menu Utama")
    pill = int(input("Pilih disini >>> "))
    if pill == 1:
        biaya = functools.reduce(lambda a,b: a + b, [x[1] for x in menu])
        print()
        print("="*50)
        print(" "*19,"NOTA DIGITAL") 
        print("="*50)
        print("Pesanan: ")
        for i in menu:
            print(f"- {i[0]:<13}: Rp {i[1]:,}")
        print("="*50)
        print("NOMOR ANTRIAN :")
        queue.check_order(nama)
        print()
        print(f"{'Tanggal Pembelian' :<20}:", datetime.now().strftime('%d-%m-%Y, %H:%M'))
        print(f"{'Nama Pelanggan' :<20}:", nama)
        print(f"{'Total Harga' :<20}: Rp", f"{biaya:,}")
        print("="*50)
        print()
        input("Tekan Enter Untuk Kembali Ke Menu Utama")
        mainPage()
    elif pill == 2: 
        createPesanan()
    elif pill == 3:
        mainPage()

def lihatAntrian():
    clear()
    daftarAntrian = queue.getAll()
    print("[1] Lihat Semua Antrian")
    print("[2] Cek Antrian Kamu")
    pil = int(input("Pilih Disini >>> "))
    if pil == 1:
        if daftarAntrian != []:
            nomor = 1
            for i in daftarAntrian:
                print()
                print(f"{nomor}. {i[0]}: ")
                for j in i[1]:
                    print(f"   - {j[0]}")
                nomor += 1
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
            mainPage()
        else:
            print("Maaf, Daftar Antrian Kosong")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
            mainPage()
    elif pil == 2:
        if daftarAntrian != []:
            # daftarNama = [x[0] for x in daftarAntrian]
            nama = input("Masukkan nama kamu: ").lower()
            hasilCari = bst.exists(nama)
            if hasilCari != []:
                print()
                print(f"> {hasilCari[0]}: ")
                for i in hasilCari[1]:
                    print(f"   - {i[0]}")
                print()
                print("NOMOR ANTRIAN KAMU: ")
                queue.check_order(nama)
                print()
                input("Tekan Enter Untuk Kembali Ke Menu Utama")
                mainPage()
            else:
                print("Maaf, nama anda tidak ditemukan dalam antrian!")
                print()
                input("Tekan Enter Untuk Kembali Ke Menu Utama")
                mainPage()
        else:
            print("Maaf, Daftar Antrian Kosong")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
            mainPage()

# HOMEPAGE
def mainPage():
    os.system("cls")
    print("-------------------------------------------------------------------")
    print("|                  SELAMAT DATANG DI KANTIN KITA                  |")
    print("|                Sistem Informasi Pelayanan Kantin                |")
    print("-------------------------------------------------------------------")
    print()    
    print("[1] Buat Pesanan")
    print("[2] Lihat Antrian")
    print("[3] Hapus Antrian Pesanan")
    print("[4] Exit")
    pil = int(input("Pilih menu >>> "))
    if pil == 1:
        createPesanan()
    elif pil == 2:
        lihatAntrian()
    elif pil == 3:
        daftarAntrian = queue.getAll()
        if daftarAntrian != []:
            queue.dequeue()
            bst.delete(daftarAntrian[0])
            print()
            print("Antrian berhasil dihapus!")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
            mainPage()
        else:
            print()
            print("Tidak ada antrian!")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
            mainPage()
    elif pil == 4:
        clear()
        exit

global queue
global bst
queue = Queue()
bst = BSTNode()
mainPage()


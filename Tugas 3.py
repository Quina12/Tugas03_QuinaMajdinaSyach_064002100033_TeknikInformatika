# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:10:07 2021

@author: Quina
"""

print("Nama : Quina Majdina Syach")
print("NIM : 064002100033")
print("TUGAS 3")

import sys
def main():
    print('''
                    ==============
                    JABODETABEK
                    Di Dalam Pulau Jawa
                    Di Luar Pulau Jawa''')
    Tujuan = tujuan_pengiriman("                    Tujuan pengiriman(q-quit): ")
    Berat =  berat_barang('''                    ==============
                    Berat barang(kg): ''')
def judul():
    print("             PROGRAM MENGHITUNG BIAYA PENGIRIMAN PT.CEPATSAMPAI")
def tujuan_pengiriman(s):
    while True:
        global tujuan
        global price_tujuan
        tujuan = input(s)
        if tujuan == 'q':
            sys.exit(0)  
        jenis = ['JABODETABEK','Di Dalam Pulau Jawa','Di Luar Pulau Jawa']
        if tujuan == 'JABODETABEK':
            price_tujuan = 10000
            break
        elif tujuan == 'Di Dalam Pulau Jawa':
            price_tujuan = 25000
            break
        else:
            price_tujuan = 50000 
            break
    return price_tujuan
def berat_barang(s):
    while True:
        global berat
        global price_berat
        berat = int(input(s))
        jenis = ['berat <= 20','berat > 20','berat <=0']
        if berat <= 20:
            price_berat = 15000
            break
        elif berat > 20:
            price_berat =  15000 + (((berat) - 20)*1500)  
            break
        while berat <=0:
            print("Invalid input")
            berat = int(input('''
                        ==============
                        Berat barang(kg): '''))
    return price_berat, berat
def PPN():
    global pajak
    global Total
    pajak = (price_tujuan + price_berat) * (10/100)
    Total = price_tujuan + price_berat + pajak
def rincian():
    print(f'''
                    ===============================
                    RINCIAN BIAYA             
                    ===============================
                    Tujuan: {tujuan}              \t\tRp.{int(price_tujuan)}
                    Berat barang (kg): {berat}kg                    \tRp.{int(price_berat)}
                    PPN (10 %)              :            \t\t\tRp.{int(pajak)}
                    Total Biaya             :            \t\t\tRp.{int(Total)}
                    ==============================''')

if __name__ == '__main__':
    judul()
    main()
    PPN()
    rincian()          

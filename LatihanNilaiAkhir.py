# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 16:17:35 2022

@author: chris
"""

nilai_akhir >80 >100	    --> A
nilai_akhir > 70 <79		--> B
nilai_akhir > 60 <69		--> C
nilai_akhir > 50 <59		--> D
	    0 < 49		--> E

nilai_absen * 10%
nilai_tugas * 20%
nilai_uts * 30%
nilai_uas * 40%

nilai_total = akumulasi semua nilai



absen = int(input("masukan nilai absen = "))
tugas = int(input("masukan nilai tugas = "))
uts = int(input("masukan nilai uts = "))
uas = int(input("masukan nilai uas = "))

nilai_akhir = int((absen*0.1)) + int((tugas*0.2)) + int((uts*0.4)) + int((uas*0.4))
print("nilai_akhir adalah =", nilai_akhir)

if nilai_akhir >=80 <=100 :
    print('A')
elif nilai_akhir >=70 <=79 :
    print('B')
elif nilai_akhir >=60 <=69 :
    print('C')
elif nilai_akhir >=50 <=59 :
    print('D')
else:  
  print('E')
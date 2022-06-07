# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:26:35 2022

@author: chris
"""

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy #nol tidak ada nilainya diartikan sprt itu
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
    
    
if 'foo' in ['bar', 'baz', 'qux' 'foo']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')


if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x

#slama tidak ada else akan tercetak end/after of outer condition


x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

x = 40

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")


if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

#tidak menggunakan else, krn sudah memenuhi di statement pertama

if 'f' in 'foo': print('1'); print('2'); print('3')

x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


hargaBuku = 2000
jumlahBeli = 3
TotalBeli = hargaBuku*jumlahBeli
uang = 10000

print(TotalBeli)
if uang > TotalBeli:
    print("bonus pensil")
elif uang == TotalBeli :
    print("no bonus")
else:
    print("tidak beli")


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
tugas = int(input("masukan nilai absen = "))
uts = int(input("masukan nilai absen = "))
uas = int(input("masukan nilai absen = "))

nilai_akhir = (absen*0.1) + (tugas*0.2) + (uts*0.4) + (uas*0.4)
print("nilai_akhir adalah =", akhir)

if nilai_akhir >=80 <=100 :
    print('A')
elif nilai_akhir >=70 <=79 :
    print('B')
elif nilai_akhir >=60 <=69 :
    print('C')
elif nilai_akhir >=50 <=59 :
    print('D')
elif nilai_akhir >=80 <=100 :
else  
  print('E')
















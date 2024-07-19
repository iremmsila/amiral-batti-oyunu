#21100011030
#İREM SILA SARIKAYA

import sys
import random
from random import randint

while True:
    secenek=0
    if secenek<2:
        print("1-gizli mod")
        print("2-açik mod")
        secim = int(input("oynamak istediğiniz modu seciniz"))
        if secim==1:
            savasAlani = [[" "] * 10 for k in range(10)]
            gizlimod = [["?"] * 10 for j in range(10)]

            acikmod = savasAlani.copy()


            def oyun_alani(alan):
                print("0 1 2 3 4 5 6 7 8 9 ")
                sutun_Sayisi = 0
                for sutun in alan:
                    print("|".join(sutun), sutun_Sayisi)
                    sutun_Sayisi += 1


            def gemi_konumlandir(alan):
                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 3 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"
                            alan[satir][sutun + 2] = "X"
                            alan[satir][sutun + 3] = "X"
                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"
                            alan[satir][sutun - 2] = "X"
                            alan[satir][sutun - 3] = "X"

                    else:
                        if satir + 3 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"
                            alan[satir + 2][sutun] = "X"
                            alan[satir + 3][sutun] = "X"
                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"
                            alan[satir - 2][sutun] = "X"
                            alan[satir - 3][sutun] = "X"

                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 2 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"
                            alan[satir][sutun + 2] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"
                            alan[satir][sutun - 2] = "X"

                    else:
                        if satir + 2 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"
                            alan[satir + 2][sutun] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"
                            alan[satir - 2][sutun] = "X"

                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 1 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"

                    else:
                        if satir + 1 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"

                for gemi in range(1):
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    while alan[satir][sutun] == "X":
                        satir, sutun = hamle()
                    alan[satir][sutun] = "X"


            def batan_gemi(alan):
                sayac = 0
                for satir in alan:
                    for sutun in satir:
                        if sutun == "X":
                            sayac += 1
                return sayac


            def hamle():
                sutun_numarasi = input("oynamak istediğiniz sutun sayisini giriniz: ")
                satir_numarasi = input("oynamak istediğiniz satir sayisini giriniz: ")
                if satir_numarasi not in "0123456789":
                    satir_numarasi = input("yanlış seçim yaptınız lütfen oynamak istediğiniz sayıyı tekrar giriniz: ")
                if sutun_numarasi not in "0123456789":
                    sutun_numarasi = input("yanlış seçim yaptınız lütfen oynamak istediğiniz sayiyi tekrar giriniz: ")
                return int(satir_numarasi), int(sutun_numarasi)


            gemi_konumlandir(savasAlani)

            hak = 33
            while hak > 0:
                oyun_alani(gizlimod)
                satir, sutun = hamle()
                if gizlimod[satir][sutun] == "*":
                    print("daha önce işlem yapıldı")
                elif gizlimod[satir][sutun] == "X":
                    print("daha önce işlem yapıldı")
                elif savasAlani[satir][sutun] == "X":
                    print("doğru tahmin")
                    print(f'kalan hak {hak}')
                    gizlimod[satir][sutun] = "X"
                    hak -= 1
                    if batan_gemi(gizlimod) == 4:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 3:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 2:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 1:
                        print("1 gemi batırdınız")
                else:
                    print("yanlış tahmin")
                    gizlimod[satir][sutun] = "*"
                    hak -= 1
                    print(f'kalan hak {hak}')
                if batan_gemi(gizlimod) == 10:
                    puan = hak * 12  # ödev listesindeki açıklamadan son hak ile oyun tamamlandığında 12 puan kazandığını düşünerek her hakka 12 puan verdim
                    print(f'tüm gemiler battı tebrikler!, toplam puan = {puan}')
                    secenek = int(input("yeni oyun için 1'e çıkmak için 2'ye basınız"))
                    if secenek == 2:
                        print("oyun bitti")
                        sys.exit(oyun_alani)

            if hak == 0:
                print("tahmin hakkınız bitti")
                secenek = int(input("yeni oyun için 1'e çıkmak için 2'ye basınız"))
                if secenek == 2:
                    print("oyun bitti")
                    break

                print(f'kalan hak {hak}')

        if secim ==2:
            savasAlani = [[" "] * 10 for k in range(10)]
            gizlimod = [[" "] * 10 for j in range(10)]
            acikmod = savasAlani.copy()


            def oyun_alani(alan):
                print("0 1 2 3 4 5 6 7 8 9 ")
                sutun_Sayisi = 0
                for sutun in alan:
                    print("|".join(sutun), sutun_Sayisi)
                    sutun_Sayisi += 1


            def gemi_konumlandir(alan):
                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 3 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"
                            alan[satir][sutun + 2] = "X"
                            alan[satir][sutun + 3] = "X"
                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"
                            alan[satir][sutun - 2] = "X"
                            alan[satir][sutun - 3] = "X"

                    else:
                        if satir + 3 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"
                            alan[satir + 2][sutun] = "X"
                            alan[satir + 3][sutun] = "X"
                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"
                            alan[satir - 2][sutun] = "X"
                            alan[satir - 3][sutun] = "X"

                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 2 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"
                            alan[satir][sutun + 2] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"
                            alan[satir][sutun - 2] = "X"

                    else:
                        if satir + 2 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"
                            alan[satir + 2][sutun] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"
                            alan[satir - 2][sutun] = "X"

                for gemi in range(1):
                    yatay_dikey = random.randint(1, 2)  # 1 yatay,2 dikey
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    if yatay_dikey == 1:
                        if sutun + 1 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun + 1] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir][sutun - 1] = "X"

                    else:
                        if satir + 1 <= 9:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir + 1][sutun] = "X"

                        else:
                            while alan[satir][sutun] == "X":
                                satir, sutun = hamle()
                            alan[satir][sutun] = "X"
                            alan[satir - 1][sutun] = "X"

                for gemi in range(1):
                    satir = random.randint(0, 9)
                    sutun = random.randint(0, 9)
                    while alan[satir][sutun] == "X":
                        satir, sutun = hamle()
                    alan[satir][sutun] = "X"


            def batan_gemi(alan):
                sayac = 0
                for satir in alan:
                    for sutun in satir:
                        if sutun == "X":
                            sayac += 1
                return sayac


            def hamle():
                sutun_numarasi = input("oynamak istediğiniz sutun sayisini giriniz: ")
                satir_numarasi = input("oynamak istediğiniz satir sayisini giriniz: ")
                if satir_numarasi not in "0123456789":
                    satir_numarasi = input("yanlış seçim yaptınız lütfen oynamak istediğiniz sayıyı tekrar giriniz: ")
                if sutun_numarasi not in "0123456789":
                    sutun_numarasi = input("yanlış seçim yaptınız lütfen oynamak istediğiniz sayiyi tekrar giriniz: ")
                return int(satir_numarasi), int(sutun_numarasi)


            gemi_konumlandir(savasAlani)

            hak = 33
            while hak > 0:
                oyun_alani(acikmod)
                print()
                oyun_alani(gizlimod)
                satir, sutun = hamle()
                if gizlimod[satir][sutun] == "*":
                    print("daha önce işlem yapıldı")
                elif gizlimod[satir][sutun] == "X":
                    print("daha önce işlem yapıldı")
                elif savasAlani[satir][sutun] == "X":
                    print("doğru tahmin")
                    gizlimod[satir][sutun] = "X"
                    hak -= 1
                    print(f'kalan hak {hak}')
                    if batan_gemi(gizlimod) == 4:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 3:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 2:
                        print("1 gemi batırdınız")
                    elif batan_gemi(gizlimod) == 1:
                        print("1 gemi batırdınız")

                else:
                    print("yanlış tahmin")
                    gizlimod[satir][sutun] = "*"
                    hak -= 1
                    print(f'kalan hak {hak}')

                if batan_gemi(gizlimod) == 10:
                    puan = hak * 12  # ödev listesindeki açıklamadan son hak ile oyun tamamlandığında 12 puan kazandığını düşünerek her hakka 12 puan verdim
                    print(f'tüm gemiler battı tebrikler!, toplam puan = {puan}')
                    secenek = int(input("yeni oyun için 1'e çıkmak için 2'ye basınız"))
                    if secenek == 2:
                        print("oyun bitti")
                        sys.exit(oyun_alani)

            if hak == 0:
                print("tahmin hakkınız bitti")
                secenek = int(input("yeni oyun için 1'e çıkmak için 2'ye basınız"))
                if secenek == 2:
                    print("oyun bitti")
                    break

                print(f'kalan hak {hak}')















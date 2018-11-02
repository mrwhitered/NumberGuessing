#
# 02.11.2018 friday
#
# coded by mrwhitered
#
# licensed by gnu-general-license
#

from random import randint

x = randint(1, 100)

tahmin = False

while not tahmin:
    try:
        Sayı = int(input("1 ile 100 arasında bir sayı girin: "))

    except ValueError:
        print("Geçerli bir sayı girin: ")

        continue

    if Sayı> x + 20 :
        print("Çok büyük")

    elif  Sayı>x:
        print("Büyük")

    elif Sayı  < x - 20  :
        print("Çok küçük")

    elif Sayı<x:
        print("Küçük")

    else:
        tahmin = True

print("Tebrikler")

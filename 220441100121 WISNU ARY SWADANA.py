print("penghitung bangun ruang")


def menu():
    print("pilih bangun ruang")
    print("Masukkan angka 1-2")
    print("1. Balok")
    print("2. Kubus")

def Balok():
    tinggi = int(input("masukkan tinggi: "))
    panjang = int(input("masukkan panjang: "))
    lebar = int(input ("masukkan lebar: "))
    volume = (panjang*lebar*tinggi)
    print("volume Balok= ",volume)
    
def Kubus():
    sisi = int(input("masukkan sisi: "))
    volume = (sisi*sisi*sisi)
    print("volume Kubus= ",volume)


print("++++++++++++++++++++++")
menu()
pilih = int(input("masukkan piliihan: "))
if pilih == 1:
    Balok()
elif pilih == 2:
    Kubus()
else:
    print("imputan salah")

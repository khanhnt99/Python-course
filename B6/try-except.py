sbc = input("so bi chia: ")
sc = input("so chia: ")
try:
    kq = int(sbc)/int(sc)
    print("Ket qua la: ", kq)
except ZeroDivisionError:
    print("Mau so phai khac 0")

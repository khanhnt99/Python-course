sbc = input("So bi chia: ")
sc = input("So chia: ")
try:
    kq = int(sbc)/int(sc)
    print("Ket qua la: ", kq)
except ZeroDivisionError:
    print("Mau so phai khac 0")
else:
    print("Khong co exception")
finally:
    print("Luon luon chay du try hay except")

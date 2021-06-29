import pyotp
code = pyotp.random_base32()
print(code)
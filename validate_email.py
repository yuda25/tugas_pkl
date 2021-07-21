import re
regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def validasi(email):
    if(re.match(regex, email)):
        print("email ini valid")
    else:
        print("email ini tidak valid")
if __name__=='__main__':
    email=input("masukkan email:")
print('data yang telah anda masukan: ', email)
validasi(email)
import string

text = string.printable

def enkripsi(content):
    global text

    key = int(input('masukan kunci :... '))
    cipher = ''
    for i in content:
        if i in content:
            a = text.find(i)
            a = (a + key)%100
            cipher = cipher + text[a]
        else:
            cipher = cipher + i
    
    return cipher

def dekripsi(cipher):
    global text
    key = int(input('masukan Kunci :... '))
    content = ''
    for i in cipher:
        if i in text:
            a = text.find(i)
            a = (a - key)%100
            content = content + text[a]
        else:
            content = content + i

    return content

if __name__ == '__main__':
    print('======================================================')
    mode = int(input('1.Enkripsi\n2.Dekripsi\nPilih Mode:'))

    if mode == 1:
        content = input('masukan isi :... ')
        print(enkripsi(content))
    elif mode == 2:
        cipher = input('Masukan isi :... ')
        print(dekripsi(cipher))
    else:
        print('Tolong pilih 1 atau 2')
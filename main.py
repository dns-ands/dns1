
def tambah(angka1,angka2):
    return int(angka1)+int(angka2)

def rupiahkan(rp):
    return rp * 15000


def main():
    while(input("mulai Program? :") == "ya"):
        nilai1 = input("Masukkan angka pertama: ")
        nilai2 = input("Masukkan angka kedua: ")
        operator = input("masukan Operator(+ - / * r) ")
        try:
            int(nilai1)
            int(nilai2)
        except:
            print("anda tidak memasukan angka!")
            continue

        if(operator == "+"):
            print("hasil = "+ str(tambah(nilai1,nilai2)))

        elif(operator == "-"):
            print("hasil = "+ str(int(nilai1) - int(nilai2)))

        elif(operator == "*"):
            print("hasil = "+ str(int(nilai1) * int(nilai2)))

        elif(operator == "/"):
            print("hasil = "+ str(int(nilai1) / int(nilai2)))

        elif(operator == "r"):
            print("rupiah = "+ str(rupiahkan(int(nilai1))))

        else:
            print('operator tidak ada!')
    
            





main()
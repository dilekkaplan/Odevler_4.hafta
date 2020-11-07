"Bu program dört işlem yapabilen bir hesap makinesi olarak yazılmıştır."

while True:
    sayi_bir=input("Lutfen ilk sayıyı giriniz: ")

    while sayi_bir.isnumeric()!=True:
        print("HATA!Lutfen bir 'sayı' giriniz!\n")
        sayi_bir=input("Lutfen ilk sayıyı giriniz: ")

    sayi_iki=input("Lufen ikinci sayıyı giriniz: ")

    while sayi_iki.isnumeric()!=True:

        print("HATA!Lutfen bir 'sayı' giriniz!\n")
        sayi_iki=input("Lutfen ikinci sayıyı giriniz: ")
    

    operatör=input("Lufen bir operatör giriniz: ")

    if operatör=="+":
        print("Sayıların toplamı: ",int(sayi_bir)+int(sayi_iki))

    elif operatör=="-":
        print("Sayıların farkı: ",int(sayi_bir)-int(sayi_iki))

    elif operatör=="*" or operatör=="x":
        print("Sayıların çarpımı: ",int(sayi_bir)*int(sayi_iki))

    elif operatör=="/" :
        print("Sayıların bölümü: ",int(sayi_bir)/int(sayi_iki))
    


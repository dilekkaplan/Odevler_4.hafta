"Bu program dört haneli bir şifre oluşturmak için yazılmıştır."

sifre=str(input("Lutfen dort haneli bir sifre giriniz: "))

while sifre.isnumeric()!=True:
    print ("HATA! Lutfen rakamlardan olusan bir şifre giriniz!\n")
    sifre=str(input("Lutfen dort haneli bir sifre giriniz: "))

while len(sifre)!=4:
    print ("HATA!", len(sifre) ," haneli bir sifre girdiniz!\n")
    sifre=str(input("Lutfen dort haneli bir sifre giriniz: "))
    
else:
    print("\nSifre olusturuldu.\nSifreniz:", sifre)
    

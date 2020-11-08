"Bu program, bilgileri girilen 5 futbolcu arasında, Barcelona takımında oynayan futbolcuların bilgilerini iç içe liste şeklinde yazdırır."

liste= []
for i in range(5):

    isim=input("Lutfen bir isim giriniz: ")
    soyisim=input("Lutfen bir soyisim giriniz: ")
    takım=input("Lutfen bir takım giriniz: ")
    futbolcu=[isim,soyisim,takım]

    if takım=="Barcelona" or takım=="Barselona" or takım=="barselona" or takım=="barcelona":
        liste.append(futbolcu)

print(liste)

      

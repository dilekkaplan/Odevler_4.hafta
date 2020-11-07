"Bu program, bilgileri girilen personeller içerisinde, Çankaya şehrinde yaşayanların ismini çıktı olarak verir."

personel_sayisi=int(input("Lutfen bilgilerini gireceğiniz personel sayısını giriniz:"))
personeller={}

for n in range(personel_sayisi):
    personel=input("Lutfen personelin ismini giriniz: ")
    yasadigi_sehir=input("Lutfen personelin yasadigi sehri giriniz: ")
    personeller[personel]=yasadigi_sehir



for i in personeller:
    if (personeller[i])=="Çankaya" or (personeller[i])=="çankaya":
        print ("\n",i)

       

"Bu fonksiyon girdi olarak gönderilen listenin içindeki sayıları toplayıp ekrana yazdırır."
Liste=[3,4,6,7,10,1,50]
toplam=0  

for i in range(len(Liste)):
    if type(Liste[i])==int or type(Liste[i])==float:
        toplam=toplam+ int(Liste[i])

    elif type(Liste[i])==str:
           break

if (type(Liste[i])==str)==True:
    print("HATA!Lütfen sayilardan oluşan bir liste yazınız.")

else:
    print("Liste içindeki sayıların toplamı",toplam,"dir.")
    
    
       
        











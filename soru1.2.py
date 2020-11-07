"Bu program girilen listenin içerisinde kaç tane 1 rakamı bulunduğunu ekrana yazar."
Liste=[12,1,1,10,20,13,53,19]
toplam=0

for i in range(len(Liste)):
    if Liste[i]==int(1):
        toplam+=1



if toplam==0:
    print("Listenin içinde 1 rakamı bulunmuyor.")
else:
    print("Listenin içinde",toplam,"tane 1 rakamı bulunuyor.")




      



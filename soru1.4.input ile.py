"Bu program bir liste içinde girilen sayıları tek ve çift sayıları gruplayarak\
iç içe liste şeklinde ekrana yazdırır."

x=int(input("Lutfen oluşturmak istediğiniz listenin eleman sayısını giriniz: "))
liste=[]
ciftler=[]
tekler=[]
for i in range(x):
   i=input("Lutfen bir sayı giriniz:")
   liste.append(i)
  

for j in(range(x)):

    if int(liste[j])%2==0:
        ciftler.append(liste[j])

    else:
        tekler.append(liste[j])

liste=[tekler]+[ciftler]

print(liste)


"Bu program kullanıcıdan bir liste oluşturmasını ister ve oluşturulan listenin elemanlarını\
küçükten büyüğe sıralar."
liste=[]
x=int(input("Lutfen olusturmak istediginiz listenin eleman sayısını giriniz:"))

for i in range(x):
    i=int(input("Lutfen sayı giriniz:"))
    liste.append(i)

for j in range(x):

    for k in range(j,x):
        if  liste[j]< liste[k]:
               liste[j]=liste[j]

        else:
            a=liste[j]
            liste[j]=liste[k]
            liste[k]=a
              
print(liste)


        

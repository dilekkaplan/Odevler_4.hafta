"Bu program liste içerisinde verilen sayıları küçükten büyüğe sıralamak için yazılmıştır."

liste=[-3,2,8,-12,20,6,100,-47,45,1000,0]

for i in range(0,len(liste)):

     for j in range(i,len(liste)):
          
          if liste[i]< liste[j]:
               liste[i]=liste[i]

          else:
               a=liste[i]
               liste[i]=liste[j]
               liste[j]=a
              
print(liste)

liste=[1,2,3,4,5,6,7,8,9,10]
ciftler=[]
tekler=[]

for i in range(len(liste)):
    if int(liste[i])%2==0:
        ciftler.append(liste[i])

    else:
        tekler.append(liste[i])

liste=[tekler]+[ciftler]

print(liste)

   

  

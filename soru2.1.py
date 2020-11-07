"Bu program içinde aynı elemandan birden fazla bulunan\
bir demet içerisinde bulunan elemanları,elemanların herbiri birer kez \
bulunacak şekilde başka bir listeye atar ve bu listeyi yazdırır."

demet=(1,2,1,2,3,4,5,9,6,7,0,8,12,12,"kemal","atatürk","kemal",0,0,0,0)
liste=[]

for i in range(len(demet)):
    liste.append(demet[i])

    if liste.count(demet[i])>1:
        liste.remove(demet[i])
            
print(liste)
        
    
            


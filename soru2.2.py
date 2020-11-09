"Bu program, içerisinde str, int, float değerleri bulunan bir demette\
yalnızca string değerlerini bastırır."

demet=(2,3,4,3.14,"bir tek",123,"DİLEĞİM",5,"var","mutlu ol", "yeter","https://open.spotify.com/track/2FBoxlXWATApoFs6489Apn?si=_6T_kkvXRFuMxhyRmpqczg")

for i in range(len(demet)):
    if type(demet[i])==str:
        print(demet[i])
        


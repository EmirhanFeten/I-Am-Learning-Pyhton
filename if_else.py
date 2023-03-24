vize=float(input('Vize notunu giriniz: '))
final=float(input('Final notunu giriniz: '))

sonuc= vize*0.4+final*0.6

if sonuc>=90 and sonuc<=100:
    print("AA")
elif sonuc>=85 and sonuc<90:
    print("BA")
elif sonuc>=75 and sonuc<85:
    print("BB")
elif sonuc>=65 and sonuc<75:
    print("CA")
elif sonuc>=60 and sonuc<65:
    print("CC")    
elif sonuc>=55 and sonuc<60:
    print("DC")
elif sonuc>=50 and sonuc<55:
    print("DD")
elif sonuc>=45 and sonuc<50:
    print("FD")
else:
    print("FF")

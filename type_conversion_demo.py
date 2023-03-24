'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr

    Yarı çapı verilen bir dairenin alan ve 
    çevresini hesaplayınız (π: 3.14)
'''
r= float(input('Yarı Çapı Giriniz: '))
pi=3.14
alan=pi*(r**2)
cevre=2*pi*r

print("Alan: "+ str(alan)+ " " + "Çevre: " + str(cevre))

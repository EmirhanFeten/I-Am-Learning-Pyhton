# numbers=[x**2 for x in range(int(input('Sayı Giriniz: '))) if x%2==0]
# print(numbers)

# myString="Hello"
# list=[]

# list=[letter for letter in myString]

# print(list)


# years=[1989,2001,1889,1999]
# age=[2019-year for year in years ]
# print(age)

# result=[x if x%2==0 else "TEK" for x in range(1,10)]
# print(result)

# result=[(x,y) for x in range(3) for y in range(3)]
# print(result)


import random

# sayi=random.randint(1,100)
# hak=5
# sayac=0
# puan=100
# print(sayi)
# while hak!=0:
#     sayac+=1
#     tahmin=int(input("Sayi Tahmin Ediniz: "))
#     if sayi==tahmin:
#         print(f"Doğru Tahmin {sayac}. Tahminde bildiniz\n Puanınız {puan}...")
#         break
#     else:
#         print("Yanlış Tahmin")
#         hak-=1
#         puan-=20        
#         print(f'Kalan Puanınız {puan} \nKalan Tahmin Hakkınız {hak}')
#         if hak==0:
#             print("Tahmin Hakkınız Bitti")   

# tahmin sayısı kullanıcıdan aldırdık ve tahmin sayısına göre puan yüzdesini hesapladık
# sayi=random.randint(1,10)
# can=int(input("Seçim Hak Sayısı Yazınız: "))
# hak=can
# sayac=0
# print(sayi)
# while hak>0:
#     hak-=1
#     sayac+=1
#     tahmin=int(input("Sayi Tahmin Ediniz: "))
#     if sayi==tahmin:
#         print(f"Doğru Tahmin {sayac}. Tahminde bildiniz\n Puanınız {int(100-(100/can)*(sayac-1))}...")
#         break
#     elif sayi>tahmin:
#         print("Yukarı")
#     else:
#         print("Aşağı")
        
#     if hak==0:
#         print(f"Tahmin Hakkınız Bitti. Tutulan sayı: {sayi}")   


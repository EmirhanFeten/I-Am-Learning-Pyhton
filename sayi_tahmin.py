import random

# sayi=random.randint(1,100)
# hak=5
# sayac=0
# puan=100
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
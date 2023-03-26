# 1'den 100'e kadar

# x=1
# while x<=100:
#     if x%2==0:
#         print(f'Sayı Çift: {x}')
#     else:
#         print(f'Sayı Tek: {x}')
#     x+=1
# print('Bitti')



# x=1
# y=int(input('Döngünün Bitiş Değerini Giriniz: '))
# while x<=y:
#     if x%2==0:
#         print(f'Sayı Çift: {x}')
#     else:
#         print(f'Sayı Tek: {x}')
#     x+=1
# print('Bitti')

# name='' # False

# while not name.strip():
#     name=input('İsminizi Giriniz: ')
# print(f'Merhaba, {name}')

# sayilar=[1,3,5,7,9,12,19,21]
# i =0
# while (i< len(sayilar)):
#     print(sayilar[i])
#     i+=1

# Kullanıcıdan alınan 5 sayıyı sıralı bir şekilde yazdıran komut satır

# numbers=[]
# i=0
# while i<5:
#     sayi=int(input('Sayı Giriniz: '))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)

urunler=[]
adet=int(input('Kaç ürün girişi olacak: '))
i=0

while i<adet:
    name=input('Ürün Adı: ')
    price=input('Ürün Fiyatı: ')
    urunler.append({
        'name':name,
        'price':price
    }) 
    i+=1
for urun in urunler:
    print(f'Urun Adı: {urun["name"]} \n Urun Fiyatı: {urun["price"]}')
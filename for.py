# numbers=[1,2,3,4,5]

# for a in numbers:
#     print('Hello')

# names=['Emir','yunus','tolga']

# for n in names:
#     print(f'my name is {n}')

# name='Emirhan Feten'
# for nam in name:
#     print(nam)

# tuple = [(1,2),(1,3),(3,5),(5,7)]

# for t,a in tuple:
#     print(t,a)

# d = {'k1':1,'k2':2,'k3':3}
# for key,value in d.items():
#     print(key,value)


# sayilar=[1,3,5,7,9,12,19,21]

#sayilar listesindeki hangi sayılar 3'ün katıdır?
# for sayi in sayilar:
#     if sayi%3==0:
#         print(sayi)

#sayilar listesindeki sayıların toplamı kaçtır?
# toplam=0
# for sayi in sayilar:
#     toplam+=sayi
# print(toplam)

#Sayılar listesindeki tek sayıların karesini alınız
# for sayi in sayilar:
#     if sayi%2!=0:
#         print(sayi**2)

# sehirler = ['kocaeli','istanbul','ankara','izmir','bursa']
# Şehirlerden hangileri en fazla 5 karakterlidir?
# for sehir in sehirler:
#     if len(sehir)<=5:
#         print(sehir)

# urunler=[
#     {'name':'samsung S6','price':'3000'},
#     {'name':'samsung S7','price':'4000'},
#     {'name':'samsung S8','price':'5000'},
#     {'name':'samsung S9','price':'6000'},
#     {'name':'samsung S10','price':'7000'}
# ]
#Ürünlerin fiyatları toplamı nedir?
# toplam=0
# for urun in urunler:
#     toplam+=int(urun['price'])
# print(toplam)

#Ürün fiyatı en fazla 5000 olan ürünleri listeletiniz
# for urun in urunler:
#     if (int(urun['price'])<=5000):
#         print(urun['name'])
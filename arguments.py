# def nameChanges(n):
#     n[0]="İstanbul"

# sehir=["Bursa","Kocaeli","İzmir"]
# nameChanges(sehir)
# print(sehir)

# def add(*params):
#     return sum(params)

# print(add(10,20,30))
# print(add(10,20,30,40,50,60))

# def displayUser(**args):
#     for key,values in args.items():
#         print('{} is {}'.format(key,values))

# displayUser(name="Emir",age="22",city="Bursa")
# displayUser(name="Yunus",age="23",city="Germany",mail="yunus@gmail.com")

# def myFunc(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# myFunc(10,20,30,40,50,name="Emir",age=22)

# def listeyeCevir(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
#     return liste

# result=listeyeCevir(10,20,30,"Emir")
# print(result)

# def asalSayiBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
#             else:
#                 print(sayi)

# sayi1=int(input("1. Sayıyı Girin: "))
# sayi2=int(input("2. Sayıyı Girin: "))

# asalSayiBul(sayi1,sayi2)

#Tam Bölen Bulma
def tamBolenBul(sayi):
    tamBolen=[]
    for i in range(2,sayi):
        if sayi%i==0:
            tamBolen.append(i)
    return tamBolen

sayilar=int(input("Bir Sayı Giriniz: "))
print(tamBolenBul(sayilar))
# plakalar = {41:'kocaeli',34:'İstanbul'}
# plakalar[6]= 'Ankara'

# print(plakalar[int(input('Plaka Numarası Giriniz: '))])

# user={
#     'Emir':{
#         'age':22,
#         'role':['user'],
#         'email':'emir@gmail.com',
#         'addres':'Bursa',
#         'phone':'12123'
#     },
#     'Yunus':{
#         'age':23,
#         'role':['user','admin'],
#         'email':'yunus@gmail.com',
#         'addres':'Almanya',
#         'phone':'516554'
#     }
# }
# print(user[input('Ad Bilgisi Giriniz: ')]['role'][1])

ogrenciler={}

number=input("Öğrenci No: ")
name=input("Öğrenci Adı: ")
surname=input("Öğrenci Soyad: ")
phone=input("Öğrenci Telefon: ")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }

ogrenciler.update(
    {
        number:{
            'ad':name,
            'soyad':surname,
            'telefon':phone
        }
    }
)
print(ogrenciler)

ogrNo=input("Öğrenci No: ")
ogrenci=ogrenciler[number]

print(ogrenci)
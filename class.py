# class Person:
    # class attributes
    # addres="no information"

    # constructor (Yapıcı Metod)
    # def __init__(self, name, age):
        # object attributes
        # self.name=name
        # self.age=age
        # print("init metodu çalıştı.")

    # instance methods
    # def intro(self):
    #     print("Hello There"+ self.name)
    # def calculateAge(clc):
    #     return 2023-clc.age

# object (instance)
# p1=Person(name="Emir",age=2001)
# p2=Person(name="Yunus",age=2000)

# p1.intro()
# p2.intro()
# print(f'Adım {p1.name} ve yaşım {p1.calculateAge()}')
# print(f'Adım {p2.name} ve yaşım {p2.calculateAge()}')

# # updating
# p1.name="Feten"

# # accessing object attributes
# print(f'p1: name:{p1.name} age:{p1.age} address:{p1.addres}')
# print(f'p1: name:{p2.name} age:{p2.age} address:{p2.addres}')

# print(p1)
# print(p2)


class Circle:
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap= yaricap

    def cevreHesapla(sefl):
        return 2*sefl.pi*sefl.yaricap
    
    def alanHesapla(sefl):  
        return sefl.pi *(sefl.yaricap**2)

c1=Circle()
c2=Circle(int(input("Dairenin Yarı Çapını Giriniz:")))

print(f'Dairenin Alanı {c1.alanHesapla()}. Çevresi {c1.cevreHesapla()}')
print(f'Dairenin Alanı {c2.alanHesapla()}. Çevresi {c2.cevreHesapla()}')


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

result=[(x,y) for x in range(3) for y in range(3)]
print(result)

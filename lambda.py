# def square(num): return num **2

# number=[1,2,4,5,6]

# result=list(map(square,number))

# for item in map(square,number):
#     print(item)

# print(result)

# square = lambda num: num**2
# number=[1,2,4,5,6]
# result=list(map(square,number))
# cevap=square(2)
# print(result)
# print(cevap)

number=[1,2,4,5,6,10]
# result=list(map(lambda num: num**2,number))
# print(result)


# def check_even(num): return num%2==0
check_even=lambda num:num%2==0
# result=list(filter(check_even,number))
# result=list(filter(lambda num:num%2==0,number))

result=check_even(number[2])
print(result)
# def print_lyrics():
#     print('Hey Jude, Dont make it bad.')
#     print("Take a sad song and make it better.")

# def repeat_lyrics():
#     print_lyrics()
#     print('Na - na - na - na')
#     print_lyrics

# repeat_lyrics()

# def print_twice(whatever):
#     print('first time:')
#     print(whatever)
#     print('the second time:')
#     print(whatever)

# print_twice('Babson')

# name = input('please enter your name:')

# print_twice(name)
# def my_abs(n):
#     if n < 0:
#         print(-n)
#     else:
#         print(n)

# my_abs(-5)
# my_abs(4)

# def give_a_break():
#     return "break"

# print(give_a_break())
# def give_another_break():
#     str1 = "break"
#     print('another break')
#     return str1
    
# print(give_another_break())
def quadratic(a, b, c):
    import math
    a= int(input("enter a:"))
    b= int(input("enter b:"))
    c= int(input("enter c:"))
    print()
    discriminant= (b**2)-(4*a*c)
    if discriminant<0 :
        print("no real solution")
    else:
        discriminant
        x_1= (-b + mth.sqrt(discriminant) / 2 * a)
        x_2= (-b - mth.sqrt(discriminant) / 2 * a)
        return x_1, x_2
        

    
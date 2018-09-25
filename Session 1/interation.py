result = 0



for i in range(1, 1001):
    if(i%2!=0):
        print(i)
        result = result + i

print(result)

result = 1

# for i in range(1, 11):
#     result = result * i

# print(result)

# import time
# def countdown(n):
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n = n-1
#     print("Blastoff!")

# countdown(100)

# counter = 0
# while counter < 10:
#     print(r"heres jhonny!")
#     counter = counter + 1

# while True:
#     print('press "q" to quit')
#     line = input("> ")
#     if line == "done":
#         break
#     print(line)

# print('done!')


# a = 49
# x = 9
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# import math

# def mysqrt(a):
#     x = a/5
#     y = (x + a/x) / 2
#     while True:
#         y = (x + a/x) / 2
#         if y == x:
#              print(x)
#              break
#         x = y


# def test_square_root(a):
#     list(print(a), mysqrt(a),  print(math.sqrt(a)), print(abs(math.sqrt(a)-mysqrt(a))))

# titles = ['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff']
#     data = [titles] + list(zip(a_data, mysqrt_data, mathsqrt_data, diff_data))
#     for i, d in enumerate(data):
#         line = '|'.join(str(x).ljust(14) for x in d)
#         print(line)
#         if i == 0:
#             print('-' * len(line))

# test_square_root(49)
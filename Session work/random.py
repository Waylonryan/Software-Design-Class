# import random
# print(random)
# print('I\'m \"ok\".')
# age = int(input('please enter your age:'))
# if age > 21:
#     print('yes, you can.')
# else:
#     print('sorry, you cannot.')
import time
print(time.time())
current = time.time()
seconds = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 60
days = current // 60 // 60 //24
print("current time: {:d} days, {:d} hours, {:d} minutes and {:.2f} seconds from epoch." .format(
    int(days), int(hours), int(minutes), seconds))




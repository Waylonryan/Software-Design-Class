# print(8 + 30 + 2018)
# print((42*60)+42)
# print(10/1.61)
# print(((42*60)+42)/(10/1.61))
# print((((42*60)+42)/(10/1.61))/60)
# print(60/((((42*60)+42)/(10/1.61))/60))
# import math
# print("The volume of a sphere with radius 5 is", 3.14*(5**3)*(4/3))
# print("60 wholesale copies costs the book store", (24.95*.6)*60 + 3 + (.75*59), "dollars")
# print("If you leave your house at 6:52 AM you will run for", (2*8.25) + (3*7.2), "minutes and arrive home at 7:30AM")
# print("by going from 82% to 89%, my grade had a", ((89-82)/82)*100,"% increase")

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
print(x)
print(t)
x = t.pop()
# If you don’t provide an index, 
# it deletes and returns the last element.
print(x)
print(t)
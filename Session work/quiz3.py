# Upload quiz3.py file to Blackboard - Session 12


# def get_middle(a, b):
#     for c in a:
#         if len(a) % 2 != 0:
#             ((len(a)-1)/2) + 1 = j
#             k = a[j]
#         else:
#             len(a)/2 = p
#             y = a[p:p+2]
    

    # '''
    # Given 2 lists, a and b, return a new list containing their middle elements.
    # '''
    # pass

# Uncomment the following lines to test
# a = [1, 2, 3]
# b = [4, 5, 6, 7]
# c = [8, 9, 10, 11, 12]
# print(get_middle(a, b))
# print(get_middle(a, c))

# Expected output:
# [2, 5, 6]
# [2, 10]

# import math
# def replace_even(data):
#     a = data[:]
#     for n in data:
#         if data[n] % 2 == 0:
#             a[n] == math.sqrt(n)
#         else:
#             a[n] == data[n]

 
    # Replace all elements at an even index in the list with its square root. If the element at an even index is negative, replace it with 0.
    # No return is required.
    # data: the list of values to process
 

    # pass

# Uncomment the following lines to test
# a = [4, 1, 0, 2, -2, 3, 23]
# replace_even(a)
# print(a)

# Expected output:
# [2.0, 1, 0, 2, 0, 3, 4.795831523312719]


# def is_increasing(data):
#     a = data[:]
#     for c in data in range[0, len(data)-1]:
#         if a[c] <= a[c+1]:
#             True
#         else:
#             False
    
    # '''
    # Return True if the list is currently sorted in increasing order.
    # # '''
    # pass

# Uncomment the following lines to test
# data_1 = [10, 11, 2018]
# data_2 = [11, 10, 2018]
# data_3 = [10, 10, 2018]
# print(is_increasing(data_1))
# print(is_increasing(data_2))
# print(is_increasing(data_3))

# # Expected output:
# True
# False
# False


def print_hist(data):
    #  a = data.keys
    #  a.sort()
    #  print(a)
    for c in data:
        print(c)
        print(data[c] * "*")
        # a = data.keys
        # a.sort()
   
    # given a dictionary of letter: positive integer pairs, 
    # print rows with the letter and a number of asterisks equal
    # to the positive integer. The rows should be printed in key order.
    # No return is required.
    # data: a dictionary of letter: positive integer pairs
    # Example:
letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)
    # Expected output:
    # A: ***
    # B: **********
    # C: ******
    # Z: ********
    # '''
    # pass
fin = open('session9/words.txt')
line = fin.readline()
# # print(line)

# # line = fin.readingline()
# # word = line.strip()
# # print(line)
# # counter = 0
# # for line in fin:
# #     word = line.strip()
# #     counter += 1
# #     # print(word)
# # print(counter)

# def read_long_words():
#     for line in fin:
#         word = line.strip()
#         if len(word) >= 20:
#             print(word)


# read_long_words()

# count = 0
# def has_no_e(word):
#     for letter in word:
#         if letter == 'e' or letter == "E":
#             return False
#     return True

# print(has_no_e(fin))

# def avoids(word, forbidden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

# print(is_abecedarian("acez"))

# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         if c > previous
#             is_abecedarian(word)
#         previous = c
#     return True

# print(is_abecedarian("bacez"))

# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         while c >= previous:
#             return True
#         if c < previous
#             return false
#         previous = c

# def has_no_e_2():
#     counter = 0
#     for line in fin:
#         word = line.strip()
#         if has_no_e(word):
#             print(word)
#             counter += 1

#     print(counter)
#     print('{:.4f}% of words have no "e".'.format((counter/total_words) * 100

# def uses_all(word, required):
#     for letters in required:
#         if letters not in word:
#             return False
#     return True

# def uses_vowels():
    # fin = open('session9/words.txt')
    # counter = 0
    # for line in fin:
    #     word = line.strip()
    #     if uses_all(word, 'aeiou'):
    #         print(word)
    #         counter += 1 

#     return counter 

# print(uses_vowels())

def find_abecedarian():
    fin = open('session9/words.txt')
    counter = 0
    current_longest_word = ""
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            counter += 1 
            if len(word) > len(current_longest_word):
                    word = current_longest_word
                    print(current_longest_word)
    return counter, current_longest_word

print(find_abecedarian())
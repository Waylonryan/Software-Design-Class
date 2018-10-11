# def find_abecedarian():
#     fin = open('session9/words.txt')
#     counter = 0
#     current_longest_word = ""
#     for line in fin:
#         word = line.strip()
#         if is_abecedarian(word):
#             print(word)
#             counter += 1 
#             if len(word) > len(current_longest_word):
#                     word = current_longest_word
#                     print(current_longest_word)
#     return counter, current_longest_word

# print(find_abecedarian())

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    ]

t = ['a', 'b', 'c']
t.append('d')

print(t)

t.extend('a')
print(t)

t.sort()
print(t)

total = 0
def nested_sum(t):
    for nested in t:
        total = 
    print total

total = 0
def cumsum(t):



def middle(t):
   return t[1:-1]


def chop(t):
    for item in t:
        t.delete(t[0])
        t.delete(t[-1])
        print(t)

def is_sorted(t):
    t.sort() = r
    if r = t:
        print("is sorted")
    else:
        print('is not sorted')

def has_duplicates(s):
    if len(s) > 1:
        for range in s
        if s[0] == s[range]:
            return False
        else: 
            return True



def is_anagram(word1, word2):
    return sorted.word1 == sorted.word2

def has_duplicates(s):
    for x in s:
        if s.count(x)>1:
            return True
    return False

def has_adjacent_duplicates(s):
    for x in range(len(s)-1):
        if s[1] == s[1+x]:
            return True
     return False

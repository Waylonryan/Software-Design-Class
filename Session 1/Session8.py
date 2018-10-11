team = 'New England Patriots'
letter = team[1]
print(letter)

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index = index + 1

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

team = 'New England Patriots'
print(team[11:4])
print(team[12:20])

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))

def count(s, letter):
    c = 0
    for each in s:
        if each == letter:
            c+=1
    return c


print(count(team, 'a'))

team.split()
team = "new england patriots"
team.split("a")
print(team)
print('waylon'.rstrip("lon"))

a = 1
b = 2
c = 3
d = 4
e = 5 
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

print(count("bananas", 'a'))

def wacky(x):
    print(x)
    print('${:,.2f}'.format(count(x, "a") * 1 + count(x, "b") * 2 + count(x, "c") * 3 + count(x, "d") * 4 + count(x, "e") * 5 + count(x, "f") * 6 + count(x, "g") * 7 + count(x, "h") * 8 + count(x, "i") * 9 + count(x, "j") * 10 + count(x, "k") * 11 + count(x, "l") * 12 + count(x, "m") * 13 + count(x, "n") * 14 + count(x, "o") * 15 + count(x, "p") * 16 + count(x, "q") * 17 + count(x, "r") * 18 + count(x, "s") * 19 + count(x, "t") * 20 + count(x, "u") * 21 + count(x, "v") * 22 + count(x, "w") * 23 + count(x, "x") * 24 + count(x, "y") * 25 + count(x, "z") * 26))
    

wacky("bananas")

# def counta(*args, letter):
#     c = 0
#     for each in *args:
#         if each == letter:
#             c+=1
#     return c

# def total(*args):
#     print(*args)
#     print('${:,.2f}'.format(counta(*args, "a") * 1 + counta(*args, "b") * 2 + counta(*args, "c") * 3 + counta(*args, "d") * 4 + counta(*args, "e") * 5 + counta(*args, "f") * 6 + counta(*args, "g") * 7 + counta(*args, "h") * 8 + counta(*args, "i") * 9 + counta(*args, "j") * 10 + counta(*args, "k") * 11 + counta(*args, "l") * 12 + counta(*args, "m") * 13 + counta(*args, "n") * 14 + counta(*args, "o") * 15 + counta(*args, "p") * 16 + counta(*args, "q") * 17 + counta(*args, "r") * 18 + counta(*args, "s") * 19 + counta(*args, "t") * 20 + counta(*args, "u") * 21 + counta(*args, "v") * 22 + counta(*args, "w") * 23 + counta(*args, "x") * 24 + counta(*args, "y") * 25 + counta(*args, "z") * 26))

# total("bananas", "apples")
# DIDNT WORK. TRYING TO PUT A VARIABLE NUMBER OF STINGS INTO THE FUNCTION
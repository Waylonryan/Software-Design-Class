import os
print(os.getcwd())

fout = open("Session work/output.txt", "a")

line1 = "how many roads must a man walk down\n"
fout.write(line1)
line2 = "before you call him a man?\n"
fout.write(line2)

fout.close()

print(os.path.abspath('session work/output.txt'))

print(os.path.exists('session work/output.txt'))

print(os.path.exists('session work/input.txt'))

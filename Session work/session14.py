# import os
# print(os.getcwd())

# fout = open("Session work/output.txt", "a")

# line1 = "how many roads must a man walk down\n"
# fout.write(line1)
# line2 = "before you call him a man?\n"
# fout.write(line2)

# fout.close()

# print(os.path.abspath('session work/output.txt'))

# print(os.path.exists('session work/output.txt'))

# print(os.path.exists('session work/input.txt'))

# import dbm
# import random

# ROSTER = ('Aaron Wendell',
#           'Alden Pexton',
#           'Allison Fernandez',
#           'Angela Tsung',
#           'Christian Thompson',
#           'Christine Lee',
#           'Connie Li',
#           'Defne Ikiz',
#           'Dong Hyun Kim',
#           'Ha Min Ko',
#           'Ho Wang Alastair Ng',
#           'Jingyu He',
#           'Jonathan Beltran',
#           'Jonghyun Park',
#           'Kyle Lawson',
#           'Matthew Michalke',
#           'Pranjal Joshi',
#           'Qinyi Li',
#           'Sarah Zazyczny',
#           'Shiyue (Shirley) Zong',
#           'Shriya Rathi',
#           'Siddhanth Goyal',
#           'Waylon Ryan',
#           'Zirui Jiao')

# GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']

# db = dbm.open('db_student', 'c')

# for student in ROSTER:
#     db[student] = random.choice(GRADES)

# for key in db:
#     print(key, db[key])


# db.close()

# import sqlite3
# db = sqlite3.connect('stocks.db')
# c = db.cursor()
# c.execute('create table portfolio (symbol text, shares integer, price real)')
# db.commit()

# stocks = [
#     ('GOOG', 100, 1093.05),
#     ('AAPL', 50, 217.68),
#     ('FB', 150, 155.42),
#     ('MSFT', 100, 109.03),
#     ('SNAP', 75, 6.88)
# ]
# c.executemany('insert into portfolio values (?,?,?)', stocks)
# db.commit()

# for row in db.execute('select * from portfolio'):
#     print(row)


# min_price = 150

# print('\nExpensive Stocks:')
# for row in db.execute('select * from portfolio where price > ?',
#                       (min_price,)):
#     print(row)

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':  
print(linecount('wc.py'))
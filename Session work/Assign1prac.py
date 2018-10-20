
import math
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n) 

primeFactors(150)


# # function which return reverse of a string 
# # def reverse(s): 
# #     return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    backward = s[::-1] 
  
    # Checking if both string are equal or not 
    if (s == backward): 
        return True
    return False
  
inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")

import turtle
import random

def go_right(step):
     turtle.setheading(0)
     turtle.forward(step)

def go_up(step):
     turtle.setheading(90)
     turtle.forward(step)


def go_left(step):
     turtle.setheading(180)
     turtle.forward(step)

def go_down(step):
     turtle.setheading(270)
     turtle.forward(step)

def DrunkardWalk(x, y, n):
    start = abs(x) + abs(y)
    # print(start)
    direction = {1: go_up, 2: go_right, 3: go_left, 4: go_down}
    for step in range(n):
        outcome = random.randint(1, 4)
        Walk = direction[outcome]
        Walk(10)
        if outcome == 1:
            y = y + 1
        elif outcome == 2:
            x = x + 1
        elif outcome == 3:
            x = x - 1
        elif outcome == 4:
            y = y - 1
            # print(y)
        # turtle.mainloop()
    # print(x)
    # print(y)
    end = abs(x) + abs(y)
    # print(end)
    distance = int(end) - int(start)
    # print(distance)
    net_distance = abs(distance)
    print("after", n, "steps, we are", net_distance, "intersections away")
    turtle.mainloop()

DrunkardWalk(26, 8, 100)




# def display_board(board):
#     print("\n----------------------------------------------------------------------------")
#     print("      ",*board, sep="   ")
#     print("----------------------------------------------------------------------------\n")

# def who_starts(question):
#     choice = None
#     while choice not in ("F", "S","f","s"):
#         choice = input(question)
#         if choice.upper() == "F":
#             f_player = "USER"
#             s_player = "USER"
#         elif choice.upper() == "S":
#             f_player = "CMP"
#             s_player  = "CMP"
#         else:
#             print("\nInvalid choice. Please re-enter your choice.")

#     return f_player, s_player

# def users_pick(question,minStick,maxStick,userIn,board):
#     print("\n--USER'S TURN--")
#     while userIn not in range(minStick, maxStick) or userIn >= len(board):
#         try:
#             userIn = int(input(question))
#             if userIn not in range(minStick, maxStick) or userIn >= len(board):
#                 print("\nYou can cannot choose that many sticks!")
#                 userIn = int(input(question))

#         except Exception as e:
#             print("\nAn error has occured.\nError: " + str(e) + "\nPlease re-enter your choice.")

#     f_player = "CMP"

#     return userIn, f_player

# def update_board(board,move):
#     valid_moves = (1,2)
#     if len(board) > move:
#         for i in  range(move):
#             board.remove("/")
#         return board
#     elif len(board) <= move:
#         if move in valid_moves:
#             for i in range(move):
#                 board.remove("/")
#             return board
#         else:
#             print("\n" + str(move) + " sticks cannot be taken.\nThe move you made was inavalid. Please  re-enter.")
#             return board

# def computers_move(board,userIn,s_player,winning_position,earlier_move):
#     best_move = 1
#     print("\n--COMPUTER'S TURN--")

#     if s_player == "CMP" and winning_position == False:
#         if len(board) % 4 ==1:
#             best_move = 0
#             while best_move not in range(1,len(board)+1):
#                 best_move = random.randint(1,3)
#         else:
#             if userIn + earlier_move < 4:
#                 best_move = 4 - (userIn + earlier_move)
#                 winning_position = True
#             elif userIn + earlier_move > 4:
#                 best_move = 8 - (userIn + earlier_move)
#                 winning_position = True

#     elif s_player == "USER" or winning_position == True:
#         best_move = 4 - userIn

#     earlier_move = best_move

#     print("\nThe computer chooses to remove...")
#     time.sleep(1)
#     print(": " + str(best_move) + " stick(s).")
#     for sticks in range(best_move):
#         board.remove("/")

#     f_player = "USER"
#     return board, f_player, winning_position, earlier_move

# def game_over(board,f_player):
#     if len(board) == 1 and f_player == "USER":
#         winner = "COMPUTER"
#         loser = "USER"
#     elif len(board) == 1 and f_player == "CMP":
#         winner = "USER"
#         loser = "COMPUTER"
#     else:
#         winner = None

#     return winner, loser

# def keepPlaying():
#     while True:
#         another_go = input("\nDo you want to play again?[Y/N]: ")
#         if another_go in ("y","Y"):
#             return True
#         elif another_go in ("n","N"):
#             return False
#         else:
#             print("\nInavlid choice. Please re-enter.")

# def main():
#     anotherGo = True
#     welcome_message()
#     while anotherGo == True:
#         earlier_move = 0
#         winning_position = False
#         nimBoard = ["/","/","/","/","/","/","/","/","/","/","/","/","/","/","/","/","/"]
#         winner = None
#         userIn = 0
#         print("----------------------------------------------------------------------------")
#         display_board(nimBoard)
#         print("\nWe begin with " + str(len(nimBoard)) + " sticks.")
#         f_player, s_player = who_starts("\nDo you want to start first or second? [F for fisrt/S for second]: ")
#         while len(nimBoard) != 1:
#             if f_player == "USER":
#                 time.sleep(0.5)
#                 userIn,f_player = users_pick("\nEnter your choice [1, 2 or 3]: ", 1, 4, 20,nimBoard)
#                 nimBoard = update_board(nimBoard,userIn)
#                 display_board(nimBoard)
#                 print("\nThere are " + str(len(nimBoard)) + " stick(s) remaining.")
#             else:
#                 time.sleep(1)
#                 nimBoard, f_player,winning_position, earlier_move = computers_move(nimBoard,userIn,s_player,winning_position,earlier_move)
#                 time.sleep(1)
#                 display_board(nimBoard)
#                 print("\nThere are " + str(len(nimBoard)) + " stick(s) remaining.")
#         time.sleep(1)
#         print("\nFinally...\nOnly one stick remains...")
#         game_winner, game_loser = game_over(nimBoard,f_player)
#         time.sleep(1)
#         print("\nThe " + game_loser + " is left with the last stick and so he is the loser...")
#         print("\nThe winner of the game is...\n: " + str(game_winner))
#         anotherGo = keepPlaying()
#         time.sleep(1)
#     print("\nThank you for playing!")
#     print("\n--GAME OVER--")

# if __name__ ==  "__main__":
#     main()
import random
def nim():
    player = random.randint(1, 2)
    if player == 1:
        print("player", player, "starts")
    else:
        print("Computer Starts")
    # decides who starts
    difficulty = random.randint(0, 1)
    if int(difficulty) == 0:
        print("Computer is smart")
    else:
        print("computer is dumb")
    # decides the computer difficulty
    number_of_marbles= random.randint(10, 100)
    # decides the number of marbles
    half_way = number_of_marbles/2
    print("starting with", number_of_marbles, "marbles")
    while True:
        half_way = number_of_marbles/2
        if player==2:
            print('Computer\'s turn')
            # how the computer will act if dumb or smart
            if int(difficulty) == 0:
            # how the computer reacts based on how many marbles are left
                if int(number_of_marbles) > 63:
                    turn = int(number_of_marbles) - 63
                    number_of_marbles = 63
                elif int(number_of_marbles) == 63:
                    turn = random.randint(1, int(half_way))
                    number_of_marbles = int(number_of_marbles) - int(turn)
                elif int(number_of_marbles) > 31 and int(number_of_marbles) < 63:
                    turn = int(number_of_marbles) - 31
                    number_of_marbles = 31
                elif int(number_of_marbles) == 31:
                    turn = random.randint(1, int(half_way))
                    number_of_marbles = int(number_of_marbles) - int(turn)
                elif int(number_of_marbles) > 15 and int(number_of_marbles) < 31:
                    turn = int(number_of_marbles) - 15
                    number_of_marbles = 15
                elif int(number_of_marbles) == 15:
                    turn = random.randint(1, int(half_way))
                    number_of_marbles = int(number_of_marbles) - int(turn)
                elif int(number_of_marbles) > 7 and int(number_of_marbles) < 15:
                    turn = int(number_of_marbles) - 7
                    number_of_marbles = 7
                elif int(number_of_marbles) == 7:
                    turn = random.randint(1, int(half_way))
                    number_of_marbles = int(number_of_marbles) - int(turn)
                elif int(number_of_marbles) > 3 and int(number_of_marbles) < 7:
                    turn = int(number_of_marbles) - 3
                    number_of_marbles = 3
                else:
                    turn = 1
                    number_of_marbles = int(number_of_marbles) - int(turn)
            else:
                turn = random.randint(1, int(half_way))
                number_of_marbles = int(number_of_marbles) - int(turn)
            # the print outs the user sees that communciates the computer move
            print("Computer Takes", turn, "Marbles")
            print(number_of_marbles, "marbles Left")
            if number_of_marbles==1:
                if player == 1:
                    print("player", player,"wins!")
                else:
                    print("Computer wins")
                break
            if player==1:
                player=2
            else:
                player=1
        if player==1:
        # how the player interacts
            print("Player", player, "turn")
            while True:
                turn=input('number of marbles to take')
                # sets the perameters for the turn
                if int(turn) >= 1 and int(turn) <= (int(half_way)):
                    break
                else:
                    print("illegal move")
                    # if the user takes more or less than the amount allowed
            number_of_marbles = int(number_of_marbles) - int(turn)
            print(number_of_marbles, "marbles left" )
            # dictate who wins
            if number_of_marbles==1:
                if player == 1:
                    print("player", player,"wins!")
                else:
                    print("Computer wins")
                break
            # switch between players
            if player==1:
                player=2
            else:
                player=1
    print('Game Over')

nim()
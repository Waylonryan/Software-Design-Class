import random
player = random.randint(1, 2)
if player == 1:
    print("player", player, "starts")
else:
    print("Computer Starts")
difficulty = random.randint(0, 1)
if int(difficulty) == 0:
    print("Computer is smart")
else:
    print("computer is dumb")
number_of_marbles= random.randint(10, 100)
half_way = number_of_marbles/2
print("starting with", number_of_marbles, "marbles")
while True:
    half_way = number_of_marbles/2
    if player==2:
        print('Computer\'s turn')
        if int(difficulty) == 0:
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
        print("Player", player, "turn")
        while True:
            turn=input('number of marbles to take')
            if int(turn) >= 1 and int(turn) <= (int(half_way)):
                break
            else:
                print("illegal move")
        number_of_marbles = int(number_of_marbles) - int(turn)
        print(number_of_marbles, "marbles left" )
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
print('Game Over')

import random

x=1
y=1
while True :
    input("press enter to role the dice")
    dice =random.randint(1,6)
    print ("Player 1 rolled a "+str(dice))
    x=x+dice
    if x<100:
        print ("Player 1 landed on "+str(x))
    if x>100:
        x=x-dice
        print("Player 1:You can't move forward unless you get a " + str(100 - x) + " on your dice")
    elif x==100:
        print("Congratulations! Player 1 you have won the game")
        quit()
    input("press enter to role the dice")
    dice = random.randint(1, 6)
    print("Player 2 rolled a " + str(dice))
    y = y + dice
    if y< 100:
        print("Player 2 has landed on " + str(y))
    if y > 100:
        y = y - dice
        print("Player 2:You can't move forward unless you get a " + str(100 - y) + " on your dice")
    elif y == 100:
        print("Congratulations! Player 2 you have won the game")
        quit()





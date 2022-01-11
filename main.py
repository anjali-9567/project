import random 

def gameWin(computer,you):
    if computer==you:
        return None
    elif computer=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif computer=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif computer=="g":
        if you=="g":
            return True
        elif you=="s":
            return True

print("computer turn: snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3)
#print(randNo)
if randNo==1:
    computer="s"
elif randNo==2:
    computer="w"
elif randNo==3:
    computer="g"

you=input("Your turn: snake(s) water(w) or gun(g)?")
a=gameWin(computer,you)

print(f"computer chose {computer}")
print(f"you chose {you}")
if a==None:
    print("The game is a tie")
elif a:
    print("you win")
else:
    print("you lose!")

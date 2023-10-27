import random

def Game(c,y):
    if c==y:
        return None
    elif c == "s":
        if y == "w":
            return False
        elif y == "g":
            return True
    elif c == "w":
        if y == "s":
            return True
        elif y == "g":
            return False
    elif c == "g":
        if y == "w":
            return True
        elif y == "s":
            return False        
            
i=1
f=True
while (i<=2):
    print("Press 1 to play")
    print("Press 2 to exit")
    v=int(input("Enter your choice : "))
    if v==1:
        f=True        
    elif v==2:
        f=False
    else:
        print("Wrong Choice..")
        exit()
    if f:
        c=print("Computer's Turn to choose between Snake(s), Water(w) and Gun(g)")
        r=random.randint(1,3)
        if r==1:
            c="s"
        elif r==2:
            c="w"
        elif r==3:
            c="g"
        print("Computer chooses it's option. ")
        y=input("Your Turn to choose between Snake(s), Water(w) and Gun(g) : ")
        a=Game(c,y)

        print(f"Computer chooses : {c}")
        print(f"You choose : {y}")

        if a == None:
            print("Tie !")
        elif a:
            print("You win !") 
        else:
            print("You lose !")
    else:
        print("Thanks for playing. See you next time..")
        exit()

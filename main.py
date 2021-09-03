import random
number=random.randint(1,100)
count=1
Guess=int(input("Guess the number: "))
while(True):
    if(Guess>number):
        Guess=int(input("Guess another number.This one is too big: "))
        count += 1
    elif(Guess<number):
        Guess=int(input("Guess another number.This one is too less: "))
        count +=1
    else:
        print(f"Yeah thats the number!,You guessed it right in {count} attempts.")
        break        



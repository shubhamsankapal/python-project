import random

randomNumber = random.randint(2,2000)

guess = int(input("enter a number between 2 and 2000 : "))
while randomNumber != guess :


    if guess < randomNumber :
        print("Your guess is to low please try again ")
        guess = int(input("enter a number between 2 and 2000 :"))

    elif guess > randomNumber :
        print("Your guess is to high please try again ")
        guess = int(input("enter a number between 2 and 2000 :"))


print("You guess it. congratulations !!! ")

# import random module
import random
# print multiline instruction
print('winning rules of the game ROCK PAPER SCISSORS are :\n'
    +  "Rock vs Paper -> Paper wins \n"
    +  "Rock vs Scissors -> Rock wins \n"
    +  "Paper vs Scissors -> scissors wins \n" )
while True:
    print ("Enter your choice \n 1 - Rock \n 2 - Paper \n - 3 - Scissors \n")

    # take the input from user

    choice=int(input("Enter your choice: "))
      # OR is the short - circuit operator
    # if any one of the condition is true
    # then it return True value

    # looping until user enter invalid input\
    while choice > 3 or choice <1:
        choice=int(input('Enter a valid choice please '))

           # initialize value of the choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name= 'Rock'
        elif choice == 2:
            choice_name= 'Paper'
        else:
            choice_name= 'scissors'

            # print user choice
        print('user choice is \n',choice_name)
        print('now its computers Turn....')
        #computers chooses randomly any numbers
        # among 1 , 2 and 3. using randint method
        # of random module
        comp_choice = random.randint(1,3)
        # looping until comp_choice value
        # is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1,3)
         # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'rocK'
        elif comp_choice == 2:
            comp_choice_name = 'papeR'
        else:
            comp_choice_name = 'scissoR'
        print("computer choice is \n", comp_choice_name)
        print(choice_name, 'vs',comp_choice_name)
        # we need to check of draw
        if choice == comp_choice:
            print('Its a Draw', end=" ")
            result="DRAW"
        # condition for winning
        if (choice==1 and comp_choice==2):
            print('paper wins =>', end=" ")
            result='papeR'
        elif (choice==2 and comp_choice==1):
            print('paper wins =>',end=" ")
            result='Paper'

        if (choice==2 and comp_choice==3):
            print('Rock wins =>\n',end=" ")
            result='rock'
        elif (choice==3 and comp_choice==1):
            print('Rock wins =>\n',end=" ")
            result='rocK'
        if (choice==2 and comp_choice==3):
            print('Scissors wins =>',end=" ")
            result='scissoR'
        elif (choice==3 and comp_choice==2):
            print('Scissors win =>',end=" ")
            result='Rock'
        # printing either user or computer wins draw
        if result == 'DRAW':
            print("<== Its a tie ==>")
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== computer wins ==>")
        print("Do you want to play again? (Y/N)")
        # if user input n or N then condition is True
        ans = input().lower()
        if ans =='n':
            break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")



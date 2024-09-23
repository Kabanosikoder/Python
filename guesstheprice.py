from random import randint

game_on = True
attempts = 10

while game_on == True:
    difficulty = input("Choose your difficulty: easy, medium, hard, impossible").lower()
    if difficulty == "easy":
        winning_number = randint(1, 500)
        user_num = int(input("Choose a number between 1 and 500"))
    elif difficulty == "medium":
        winning_number = randint(1, 1000)
        user_num = int(input("Choose a number between 1 and 1000"))
    elif difficulty == "hard":
        winning_number = randint(1, 2000)
        user_num = int(input("Choose a number between 1 and 2000"))
    elif difficulty == "impossible":
        winning_number = randint(1, 1000000)
        user_num = int(input("Choose a number between 1 and 1000000"))

    if game_on == False:
        break
    elif user_num == winning_number:
        print("You win! Congratulations !!!")
        print("You did it in {} attempts".format(attempts))

        if attempts < 5:
            print("Wow you are very good at this!")
        elif attempts == 1:
            print("You guessed in 1 attempt well played!")

    elif user_num < winning_number:
        print("Higher!")
        attempts -= 1
        if attempts == 0:
            print("You used all 10 attempts :/")
        else:
            print("You have {} attempts left".format(attempts))
            continue

    elif user_num > winning_number:
        print("Lower!")
        attempts -= 1
        if attempts == 0:
            print("You used all 10 attempts :/")
        else:
            print("You have {} attempts left".format(attempts))
            continue


    play_again = input("Do you want to play again? yes or no").lower()
    if play_again != "yes":
        print("Thanks for playing, goodbye")
        break
    else:
        attempts = 10
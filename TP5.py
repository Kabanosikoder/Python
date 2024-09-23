from random import randint

game_on = True
winning_number = randint(1, 1000)

while game_on == True:
    user_num = int(input("Choisir un nombre entre 1 et 1000"))
    if user_num == winning_number:
        print("C'est gaqné")
        break
    elif user_num < winning_number:
        print("C'est plus")
        continue
    elif user_num > winning_number:
        print("C'est moins")
        continue

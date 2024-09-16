
def main():
    # creation d'une variable 'username' ayant pour valeur le mot Graven
    username = "Graven"
    print(username)
    username = "Youtube"
    print(username)
    # creation d'une variable 'age' ayant pour valeur 19
    age = 19
    # affiche username et age
    print(username, age)
    # change la valeur par 25
    age = 25  # this overrides the previous value of age after
    # affiche la nouvelle valeur 25
    print(age)
    # age = age * age
    # print(age)

    print("Salut " + username +", vous avez " + str(age) +" ans !") # str() casts age to a string

    # recolter une 1ere note
   # note1 = float(input("Entrer la 1ere note"))
    # recolter une 2eme note
   # note2 = float(input("Entrer la 2eme note"))
    # recolter une 3eme note
   # note3 = float(input("Entrer la 3eme note"))
   # result = (note1 + note2 +note3) / 3
   # print("La moyenne de l'élève est de " + str(result))

    # recolter une valeur porte monnaie
    # creer un produit qui auro pour valeur 50
    # afficher la nvelle valeur du porte monnaie, apres son achat


    wallet = float(input("How much money do you have?"))
    print(wallet)

    product = 50

    purchase_result = wallet - product

    print("You have " + str(purchase_result) + " left in your wallet")


    # le porte monnaie d'une personne ayant pour valeur 125.7
    # wallet = 125.7
    #...
    # is_happy = True

    # simple quotes: '
    # double quotes: "
    # pas d'espace, pas de maj, pas de char speciaux, pas de chiffres devant
    # print("Hello World")
    # print("Hello Graven")
    # print("Hey bien salut à tous!")


if __name__ == '__main__':
    main()
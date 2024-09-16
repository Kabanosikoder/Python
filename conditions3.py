
wallet = 5000
computer_price = 1000

# print(computer_price < 1000)  prints True

if computer_price <= wallet or computer_price > 1000: # 'and', 'or' operators can be used in if statements
    print("L'achat est possible")
    wallet = wallet - computer_price
else:
    # print("Tu n'as pas l'argent pour acheter ce produit" + str(wallet))
    print("Tu n'as pas l'argent pour acheter ce produit, {} euros".format(wallet))

# text = ("L'achat est possible","L'achat est impossible") [computer_price <= 1000]   # conditions ternaires
# print(text)

print(wallet)

# Systeme de verification de mot de passe
password = input("Enter your password: ")
password_length = len(password)

# verifier si le mot de passe <
if password_length <= 8:
    print("Mot de passe trop court !")
elif password_length > 8 and password_length <= 12:
    print("Mot de passe moyen !")
else:
    print("Mot de passe parfait !!!")
print(password_length)

# place de cinema
# recolter l'age de la personne "Quel est votre age?"
# si mineur --> 7 euros
# si majeur --> 12 euros
# acheter popcorn???
# si oui -> +5 euros
# afficher ce prix total à payer

price = 0
age = int(input("Quel est votre age?"))

if age < 18:
    price = 7

else:
    price = 12

popcorn_yes_no = input("Acheter du popcorn?").lower()

if popcorn_yes_no == "oui":
    price = price + 5
else:
    print("No popcorn")
print("Le prix est: " + str(price)+" euros")
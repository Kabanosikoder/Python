age = int(input("Entrer votre age: "))  # input pour age

admitted = False  # par défaut c'est False

if age >= 18:
    moyenne = float(input("Entrer votre note moyenne: "))
    if moyenne < 10:
        print("Non admissible")

    elif 10 <= moyenne < 12:
        print("Admissible sous condition...")
        admitted = True

    else:
        print("Admissible")
        admitted = True

        if admitted == True:
            yes_or_no = input("Est ce que tu souhaites participer à un atelier optionnel?")
            # input pour voir si on s'inscrit pour l'atelier
            if yes_or_no == "oui" or yes_or_no == "yes":
                print("Tu es inscrit à l'atelier")
            else:
                print("Ok merci, tu n'es pas inscrit")
        else:
            print("Tu n'est pas admis")
else:
    print("Non admissible, inférieure à 18 ans")

    # test inputs :
    # age = 12; age = 18
    # moyenne = 7; moyenne = 11; moyenne = 12; moyenne = 17
    # "oui" ou "non"

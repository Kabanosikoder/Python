from random import shuffle

# Participants evenement
participants = []

# ajouter des participants
participants.append("Alice")
participants.append("Bob")
participants.append("Charlie")

print("Liste des participants: ", participants)
participants.remove("Bob")  # removes bob
print("Suppression de ’Bob’")
print(participants)
print("Liste des participants: ", participants)
# shuffles the participants
print("Mélange de la liste des participants")
shuffle(participants)
print("print(participants)", participants)
print("Tri de la liste des participants")
participants = sorted(participants)     # sorts alphabetically
print("Liste triée:",participants)
print("Nombre total de participants: ", len(participants))
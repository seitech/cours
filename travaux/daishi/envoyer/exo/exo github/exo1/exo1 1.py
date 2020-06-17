# exo 1.1 : Alice et Bob veulent jouer a pile ou face.
# - si la variable "number" vaut 0, cela equivaut a pile
# - si elle vaut 1, cela equivaut a face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Redigez le code qui indique le nom du gagnant.



import random
head_or_tail = random.randint(0, 1)
number = head_or_tail
if number == 0:
    print("Alice a gagner")
else:
    print("Bob a gagner")
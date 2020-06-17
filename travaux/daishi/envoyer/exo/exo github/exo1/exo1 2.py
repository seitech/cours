# exo 1.2 : Alice et Bob veulent jouer aux des.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Redigez le code qui indique le nom du gagnant.

import random
dice = random.randint(1, 6)

print("le chiffre" + (" ") + str(dice) + (" ") + "est sortie.")

if dice >= 4:
    print("Alice a gagner.")
else:
    print("Bob a gagner.")


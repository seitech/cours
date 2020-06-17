# exo 1.3 : Alice et Bob jouent a pierre papier ciseaux.
# - 1 equivaut a pierre
# - 2 equivaut a papier
# - 3 equivaut a ciseaux
# Redigez le code qui indique qui gagne.
import random
alice = random.randint(1, 3)
bob = random.randint(1, 3)


if (alice == 1) and (bob == 1):
    print("match nul car ils ont tous les deux joue pierre.")
elif (alice == 1) and (bob == 2):
    print("bob a gagner car le papier envelloppe la pierre.")
elif (alice == 1) and (bob == 3):
    print("alice a gagner car la pierre casse les ciseaux.")
elif (alice == 2) and (bob == 1):
    print("alice a gagner car le papier envelloppe la pierre.") 
elif (alice == 2) and (bob == 2):
    print("match nul car ils ont tous les deux joue papier.")       
elif (alice == 2) and (bob == 3):
    print("bob a gagner car les ciseaux coupent le papier.")
elif (alice == 3) and (bob == 1):
    print("bob a gagner car la pierre casse les ciseaux.")
elif (alice == 3) and (bob == 2):
    print("alice a gagner car les ciseaux coupent le papier.")   
else:
    print("match nul car ils ont tous les deux joue ciseaux.")

if alice == 1:
    alice = "pierre"
elif alice == 2:
    alice = "papier"
else:
    alice = "ciseaux"

if bob == 1:
    bob = "pierre"
elif bob == 2:
    bob = "papier"
else:
    bob = "ciseaux"

print ("alice a joue" + (" ") + alice + (" ") + "et bob a joue" + (" ") + bob)
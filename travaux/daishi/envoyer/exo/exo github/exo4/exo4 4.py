import random
cards = []
alice = []
bob = []
xalice = 0
ybob = 0
tour = 1
for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'coeur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))
while tour <= 3:
  # mélange des cartes
  random.shuffle(cards)

  # alice prend 3 cartes
  card = random.choice(cards)
  cards.remove(card)
  alice.append(card)
  card = random.choice(cards)
  cards.remove(card)
  alice.append(card)
  card = random.choice(cards)
  cards.remove(card)
  alice.append(card)

  # est ce que alice à un 3 ou 2 coeur dans ses cartes ?
  for card in alice:
    if ((alice[0][2] == 3 or alice[1][2] == 3  or alice[2][2] == 3) or ((alice[0][0] == 'cœur' and alice[1][0] == 'cœur') or (alice[1][0] == 'cœur' and alice[2][0] == 'cœur') or (alice[2][0] == 'cœur' and alice[0][0] == 'cœur'))):
      xalice += 1
    else:
      xalice += 0
  
  # alice remet ces cartes
  cards.extend(alice)
  alice.clear()

  # mélange des cartes
  random.shuffle(cards)

  # bob tires 3 cartes
  card = random.choice(cards)
  cards.remove(card)
  bob.append(card)
  card = random.choice(cards)
  cards.remove(card)
  bob.append(card)
  card = random.choice(cards)
  cards.remove(card)
  bob.append(card)

  # est ce que bob à un 7 ou 2 pique dans ses cartes ?
  for card in bob:
    if ((bob[0][2] == 3 or bob[1][2] == 3  or bob[2][2] == 3) or ((bob[0][0] == 'pique' and bob[1][0] == 'pique') or (bob[1][0] == 'pique' and bob[2][0] == 'pique') or (bob[2][0] == 'pique' and bob[0][0] == 'pique'))):
      ybob += 1
    else:
      ybob += 0

  # bob remet ces cartes
  cards.extend(bob)
  bob.clear()

  #rés 3 tour
  
  if xalice < ybob:
    print ("bob a gagné le tour " + (str(tour)) )
  elif xalice > ybob:
    print ("alice à gagné le tour " + (str(tour)))
  else:
    print ("alice et bob sont ex aequo au tour " + (str(tour)))
  tour +=1
#
if xalice < ybob:
  print ("bob a gagné plus de manche")
elif xalice > ybob:
  print ("alice à gagné plus de manche")
else:
  print ("alice et bob sont ex aequo")
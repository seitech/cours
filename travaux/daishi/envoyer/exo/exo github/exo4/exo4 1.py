import random
cards = []
alice = []
bob = []
for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
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


for card in cards:
  print ((card [1])+(str(card [2])))
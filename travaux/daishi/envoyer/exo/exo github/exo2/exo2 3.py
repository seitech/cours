
counter = 0
for i in range(0,6):
    for j in range(0,6):
        counter += 1
        if i == 1:
            print("le dé à fait un 1", end='')       
        elif i == 2:
            print("le dé à fait un 2", end='')
        elif i == 3:
            print("le dé à fait un 3", end='')
        elif i == 4:
            print("le dé à fait un 4", end='')
        elif i == 5:
            print("le dé à fait un 5", end='')
        else:
            print("le dé à fait un 6", end='')
        
        if j == 1:
            print("& le second dé à fait un 1")
        elif j == 2:
            print("& le second dé à fait un 2")
        elif j == 3:
            print("& le second dé à fait un 3")
        elif j == 4:
            print("& le second dé à fait un 4")
        elif j == 5:
            print("& le second dé à fait un 5")
        else:
            print("& le second dé à fait un 6")
print (f"il y a {counter} issues en tout")
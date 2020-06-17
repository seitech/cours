
counter = 0

for i in range(1, 7):
    counter += 1

    if i == 1:
        print("le dé à fait un 1")
    elif i == 2:
        print("le dé à fait un 2")
    elif i == 3:
        print("le dé à fait un 3")
    elif i == 4:
        print("le dé à fait un 4")
    elif i == 5:
        print("le dé à fait un 5")
    else:            
        print("le dé à fait un 6")

print(f"il y a {counter} issues en tout")
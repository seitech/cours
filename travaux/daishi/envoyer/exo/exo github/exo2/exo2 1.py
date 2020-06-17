
counter = 0
for i in range(0,2):
    for j in range(0,2):
        counter += 1
        if i == 0:
            print("pile", end='')       
        else:
            print("face", end='')
        if j == 0:
            print(" & pile")
        else:
            print(" & face")
print (f"il y a {counter} issues en tout")
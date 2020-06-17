
issues = 0
counter = 0
for i in range(0, 2):
    for j in range(0, 2):
        issues += 1
        if i == 0 or j == 0:
            counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile avec deux lancers")
counter = 0 
issues = 0 
for i in range(0, 2):
  for j in range(0, 2):
    for k in range(0,2): 
      issues +=1 

      if i == 0:
          print("pile", end='')
      else:
          print("face", end='')
      if j == 0:
          print(" & pile", end='')
      else:
          print(" & face", end='')
      if k == 0:
            print(" & pile")
      else:
          print(" & face")

      if (i == 0 and (j == 0 or k == 0)) or (k == 0 and (j == 0 or i == 0)):
        counter +=1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir 2 fois pile avec trois lancers")           
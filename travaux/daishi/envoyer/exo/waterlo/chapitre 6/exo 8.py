age = int(input())
if age > 17:
   print("You can vote")
elif (age >= 0) and (age < 18):
   print("Too young to vote")
else: 
   print("You are a time traveller")
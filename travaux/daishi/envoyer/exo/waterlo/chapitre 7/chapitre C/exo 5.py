n = (int(input()))
x = 0
while (x <= (n + 1)):
  x += 1
  if ((n % x) == 0):
    y = n / x
    y = int (y)
    print((str(x)) + " times " + (str(y)) + " equals " + (str(n)))
  else:
    continue
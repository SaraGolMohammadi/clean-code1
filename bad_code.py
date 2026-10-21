# bad_code.py
def calculate_stuff(x, y, z):
  area1 = 3.14159 * (x * x)
  area2 = 3.14159 * (y * y)
  total = area1 + area2
  print("Total area is: ", total)

  unused_variable = 100  # متغیر بدون استفاده

  if z == True:
    print("Z is true")
  else:
    print("Z is false")
  return total


a = 5
b = 10
c = True
calculate_stuff(a, b, c)
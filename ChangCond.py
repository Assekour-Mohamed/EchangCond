n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 * n2 > 0:
  temp = n1
  n1 = n2
  n2 = temp

  print("After swap first input = ", n1, "Second = ", n2)

else:
  print("Addition = ", n1 + n2)
  print("Multiplication", n1 * n2)
Use code with caution. Learn more

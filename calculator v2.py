print("====================")
print("  calculator  ")
print("====================")

print("1- start")

print("2- Exit")

choice = int(input("choice: "))

if choice == 2:
 print("finished")
 
elif choice == 1:
  print("====================")

  num1 = int(input("enter first number: "))

  sign = input("enter the sign (* , + , - , /): ")

  num2 = int(input("enter second number: "))

  print("====== result ======")

  if sign ==("+"):
   a = num1 + num2
   print(f"Result: {a}")
  
  elif sign ==("*"):
   a = num1 * num2
   print(f"Result: {a}")
  
  elif sign ==("-"):
   a = num1 - num2
   print(f"Result: {a}")
  
  elif sign == "/":

    if num2 == 0:

        print("Cannot divide by zero")

    else:

            result = num1 / num2

            print(f"Result: {result}")

  else:

        print("Invalid Operation")

else:

    print("Invalid Choice")

  
print("=======================")
# try:
#   x = int(input("What's is x? "))
# except ValueError:
#   print("x is not an integer")
# else:
#   print(f"x is {x}")
  

# while True:
#   try:
#     x = int(input("What's x? "))
#   except ValueError:
#     print("x is not an integer")
#   else:
#     break
  
# print(f"x is {x}")

# Summary of the code above,
# While True, if x is an int, the program breaks out of the loop. --The else statement is associated with
# try block. if there's an error, it prints "x is not an integer" and asks "What's x?".
# The code below can also be a representation of the code above

# while True:  # While "True" is true
#   try:  # Try the code below and if there's no error, break out of the loop
#     x = int(input("What's x? "))
#     break
#   except ValueError:  # Except if there's an error, print "x is not an integer" and return to line 1
#     print("x is not an integer")
  
# print(f"x is {x}")


def main():
  x = get_int("What's x? ")
  print(f"x is {x}")

def get_int(promt):
  while True:
    try:
      x = int(input(promt))
    except ValueError:
      print("x is not an integer")
    else:
      return x  # Return not only breaks out of the function but also returns the value of x and the code will still work

main()
# def main():
#   m = int(input("Enter an expression: "))
#   print(playback(m))
  
# def playback(m):
#   E = m * 300000000 ** 2
#   return E

# main()


""" def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d.removeprefix("$")
    return float(d)


def percent_to_float(p):
    # TODO
    p = p.removesuffix("%")
    return float(p) / 100


main() """

""" def main():
    message = bool(input("Enter True or False: "))
    print(dosomething(message))
    
def dosomething(message):
    if message == True:
        return "That's true"
    else:
        return "That's false"
    
main() """

""" x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y") """
    
    
# print(True and "This is true")



""" def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(number):
    return  number % 2 == 0 
    
main() """

# def main():
    # answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # question(answer)

# def question(res):
#     match res:
#         case "42":
#             print("Yes")
#         case "forty-two":
#             print("Yes")
#         case "forty two":
#             print("Yes")
#         case _:
#             print("No")
            
# main()

# def main():
#     greeting = input("Greeting: ")
#     greeting = greeting.lower()
#     say_greeting(greeting)
    
# def say_greeting(greet):
#     if greet.startswith("hello"):
#         print("$0")
#     elif greet.startswith("h"):
#         print("$20")
#     else:
#         print("$100")
        
# main()

# def main():
#     file_name = input("File name: ")
#     file_name = file_name.lower()
#     get_extension(file_name)
    
# def get_extension(name):
#     if name.endswith(".gif"):
#         print("image/gif") 
#     elif name.endswith(".jpg"):
#         print("image/jpg") 
#     elif name.endswith(".jpeg"):
#         print("image/jpeg") 
#     elif name.endswith(".png"):
#         print("image/png") 
#     elif name.endswith(".pdf"):
#         print("application/pdf") 
#     elif name.endswith(".txt"):
#         print("text/plain") 
#     elif name.endswith(".zip"):
#         print("application/zip") 
#     else:
#         print("application/octet-stream")


# main()


# def main():
#     expression = input("Expression: ")
#     expression = expression.strip()
#     interpret(expression)
    
# def interpret(expression):
#     x, y, z = expression.split(" ")
#     x = float(x)
#     z = float(z)
#     if y == "+":
#         print((x + z))
#     elif y == "-":
#         print(x - z)
#     elif y == "*":
#         print(x * z)
#     else:
#         print(x / z)
    
    
# main()

# def main():
#     time = input("What time is it? ")
#     time = convert(time)
#     if time >= 7 and time <= 8:
#         print("breakfast time")
#     elif time >= 12 and time <= 13:
#         print("Lunch time")
#     elif time >= 18 and time <= 19:
#         print("Dinner time")
#     else:
#         print("")


# def convert(time):
#     hours, minutes = time.split(":")
#     minutes = int((int(minutes) / 60) * 100)
#     return float(f"{hours}.{minutes}")


# if __name__ == "__main__":
#     main()

# i = 1
# name = "Abayomi"

# while i <= name.__len__:
#     print(i)
#     i = i + 1


# def main():
#     variable = input("Enter a CamelCase: ")
#     print("snake_case:", convert(variable))
    

# def convert(string):
#     snake_case = ""
#     for c in string:
#         if c.isupper():
#             snake_case += "_" + c.lower()
#         else:
#             snake_case += c
#     return snake_case
        
# main()


# def coke(amount, amount_due):
#     while amount_due > 0:
#         amount_due = amount_due - amount
#     return amount_due
        
# main()

# for denomination in denominations:
#         if amount == denomination:
#             while amount_due > 0:
#                 amount_due = amount_due - amount
#                 print(amount_due)
#                 amount = int(input("Insert Coin: "))
#             # print(coke(amount, amount_due))
#             # return        
#         else:
#             print(amount_due)
#             # amount = int(input("Insert Coin: "))


# def coke():
#     amount_due = 50
#     # amount = 0
    
#     while amount_due > 0:
#         print(amount_due)
#         amount = int(input("Insert Coin: "))
#         for amount in [25, 10, 5]:
#             amount_due -= amount
#             amount = int(input("Insert Coin: "))
#             print(amount_due)
    
# coke()

# Whilr Loop
# number = 0
# while (number < 5):
#     print("meow!")
#     number += 1

# For Loop
# for i in [1, 2, 3]:
#     print("meow")
    
    ## The Problem with this is: in the extreme case, if we want to meow a million times, we will have to update
    ## the list from number 1 to 1,000,000. Thus, the problem with this approach 
    
## A better approach is using a function already made available by some other person: range()
# for _ in range(10):
#     print("meow")

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
    
# for _ in range(n):
#     print("meow")
    
    
# def main():
#     number = get_number()
#     meow(number)
    
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if(n > 0):
#             break
#     return n
    
# def meow(n):
#     for _ in range(n):
#         print("meow")
        
# main()

# def main():
#     total = 50
#     print("Amount Due: ", total)
#     amount_due(total)

# def amount_due(total):
#     while (total != 0):
#         number = get_coin()
#         total = total - number
#         if(total > 0):
#             print(f"Amount Due: {total}")
#         else:    
#             print(f"Change Owed: {-total}", )
#             break
    
# def get_coin():
#     while True:
#         coin = int(input("Insert Coin: "))
#         if(coin == 25 or coin == 10 or coin == 5):
#             break
#         else:
#             print("Amount Due: ", 50)
#             continue
#     return coin

# main()

# students = [
#   {"name": "Abayomi", "level": "200 level", "cgpa": 4.5},
#   {"name": "Abayomi", "level": "200 level", "cgpa": 4.5},
#   {"name": "Abayomi", "level": "200 level", "cgpa": 4.5},
# ]

# for student in students:
#   print(student["level"])

# def is_valid():
#     s = "ab02omi"
#     for a in s[2:len(s)]:
#         if(a.isnumeric() and int(a) == 0):
#             return False
#         else:
#             return True

# is_valid()



# def main():
#     print_bricks(3)
    
    
# def print_bricks(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")    
#         print()

# main()


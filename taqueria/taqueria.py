menu = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}

def main():
  item = get_price("Item: ")
  print(item)

def get_price(item):
  total = 0.00
  while True:
    try:
      question = input(item)
      for entree in menu:
        if(question.lower() == entree.lower()):
          total = total + menu[question.title()]
          print(f"${total:.2f}")
        else:
          continue
    except EOFError:
      return ""

main()
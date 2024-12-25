def main():
  get_grocery("")
  
def get_grocery(item):
  groceries = {}
  while True:
    try:
        item = input("")
        fruit = groceries.get(item)
        if fruit is None:
            groceries[item] = 1
        else:
            groceries[item] = groceries[item] + 1
        groceries = dict(sorted(groceries.items()))
    except EOFError:
        for item in groceries:
          print(f"{groceries[item]} {item.upper()}")
        break
main()
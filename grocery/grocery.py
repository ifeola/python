
def main():
  item = get_grocery("")
  print(item)
  
def get_grocery(item):
  grocery = []
  
  while True:
    try:
      grocery_item = input(item)
      grocery.append(grocery_item)
      continue
    except EOFError:
      grocery = sorted(grocery)
      for i in grocery:
        
      return grocery
    
  
main()
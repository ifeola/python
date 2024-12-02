# students = [
#   {"name": "Abayomi", "level": "200level", "cgpa": 4.5},
#   {"name": "Abayomi", "level": "200level", "cgpa": 4.5},
#   {"name": "Abayomi", "level": "200level", "cgpa": 4.5},
# ]

# for student in students:
#   print(student)

def main():
  total = 50
  print("Amount Due: ", total)
  amount_due(total)

def get_coin():
  while True:  # While "True" is true
    coin = int(input("Insert Coin: "))  # Do the code on this line
    if(coin == 25 or coin == 10 or coin == 5):  # If coin is either 25, 10 or 5,
      break  # break the loop and return coin
    else:  # else, print "Amount Due: 50" and continue the loop While "True" is true
      print("Amount Due: ", 50)
      continue
  return coin

def amount_due(total):
  while (total != 0):
    number = get_coin()
    total = total - number
    if(total > 0):
      print(f"Amount Due: {total}")
    else:    
      print(f"Change Owed: {-total}", )
      break


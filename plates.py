def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):

  
  if(len(s) >= 2 and len(s) <= 8 and s[0:2].isalpha() and s[-1].isnumeric() and s.isalnum()):
    return True
  else: 
    return False

main()
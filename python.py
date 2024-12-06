# def main():
#   name = "Ife021"
#   if get(name):
#     print("true")
#   else:
#     print("false")

# def get(name):
#   for n in name:
#     if (n.isdigit() and n != "0"):
#       return True
      
# main()

# name = "ab221"
# for n in name:
#   if (n.isnumeric()):
#     if(name[name.index(n):len(name) - 1].isdigit()):
#       print(True)
#     else:
#       print(False)
# for n in name:
#   if (n.isnumeric()):
#     print(name.index(n, len(name) - 1))

# names = "ab012"
# for name in range(len(names)):
#   if names[name].isdigit():
#     print(name)

number = 20.98
numb = int(number)
numb_two = str(number).split(".")
if (int(numb_two[1][0]) > 5):
  numb += 1
  print(numb)
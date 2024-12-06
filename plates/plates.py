def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(plate):
  if not (len(plate) >= 2 and len(plate) <= 6):
    return False
  for p in range(len(plate)):
    if plate[p].isnumeric():
      if (int(plate[p]) != 0):
        if not plate[p: len(plate) - 1].isnumeric():
          return False
      else:
        return False
      break
  if not (plate.isalnum()):
    return False
  if not (plate[0].isalpha() and plate[1].isalpha()):
    return False
  return True


main()


# def is_valid(plate):
#   if(len(plate) >= 2 and len(plate) <= 6):
#     if(plate.isalnum()):
#       if(plate[0].isalpha() and plate[1].isalpha()):
#         if(plate[-1].isalnum() or plate.isalpha()):
          # for p in plate:
          #   if (p.isnumeric()):
          #     if(int(p) == 0):
          #       return False
#               else:
#                 return True
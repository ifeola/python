def main():
  gauge = get_gauge("Enter fraction: ")
  if(gauge < 1):
    print("E")
  elif (gauge > 99):
    print("F")
  else:
    print(str(gauge)  + "%")

def get_gauge(fraction):
  while True:
    try:
      gauge = (input(fraction)).split("/")
      x = int(gauge[0])
      y = int(gauge[1])
      return int(x/y * 100)
  
    except ValueError:
      print("Either x or y is not an integer")
    except ZeroDivisionError:
      print("x cannot be divided by 0")
      
main()

# numb = "1/2"
# gauge = numb.split("/")
# x = int(gauge[0])
# y = int(gauge[1])


# print(x/y)
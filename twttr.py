def main():
    name = input("what's your name? ")
    shorten(name)

    
def shorten(name):
    new_name = ""
    for n in name:
        n = n.lower()
        if(not(n == "a" or n == "e" or n == "i" or n == "o" or n == "u")):
            new_name += n
    print(new_name.capitalize())
            
main()
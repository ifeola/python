def main():
    name = input("what's your name? ")
    shorten(name)

    
def shorten(name):
    new_name = ""
    for n in name:
        if not n.lower() in ["a", "e", "i", "o", "u"]:
            new_name += n
    print(new_name)
            
main()
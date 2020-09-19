input("Hello, hit enter when you are ready.")
name = input("what is your name?")
computer = input("what would you like to call me?")

def main():
    import interfase
    interfase.words(input("How can I help you today?"))

def newif():
    file = open("interfase.py")
    thelist = len(file.readlines)
    for item in thelist:
        
        file.write("%s\n" % item)
    
newif()

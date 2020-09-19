def readEmotions():
    file = open("emotions.py", "r")
    calm = file.readline()
    angry = file.readline()
    sad = file.readline()
    file.close()
    return(calm,angry,sad)

def emotions():
    x, y, z = readEmotions()
    x = int(x)
    y = int(y)
    z = int(z)
    
    if(x > y and x > z):
        return ("calm")
    elif(y>x and y >z):
        return ("angry")
    elif(z > x and z > y):
        return("sad")
    elif(x == z):
        return("calm")
    elif(y == x ):
        return("angry")
    elif(z == y):
        return("sad")

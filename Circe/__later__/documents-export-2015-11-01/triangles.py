def main():
    x = input("what are the three sides?")
    a,b,c = x.split(" ")
    a = float(a)
    b = float(b)
    c = float(c)
    area = trianglearea(a,b,c)
    print(area)
def trianglearea(a,b,c):
    #coppyed code
    s = 0.0
    s = (a + b + c)/2
    import math
    area = math.sqrt(s*(s - a) * (s - b) * (s - c))
    return(area)

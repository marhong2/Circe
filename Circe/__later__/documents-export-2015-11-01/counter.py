def main1():
    numbers = eval(input("enter a number you want to get the sum of all of the numbers up till"))
    x = sumN(numbers)
    print(x)

    
def main2():
    numbers = eval(input("enter a number you want to get the sum of all of the cubes up till your number"))
    y = sumNCubes(numbers)
    print(y)

    
def sumN(n):
    x = 0
    for i in range(n):
        x = x + (i + 1)
    return(x)
def sumNCubes(n):
    x = 0
    for i in range(n):
        x = x +(i + 1) ** 3
    return(x)



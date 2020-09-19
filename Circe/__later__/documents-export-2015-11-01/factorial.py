def factorial():
    life = 1
    value = 1
    x = eval(input("what is your num"))
    y = input("whould you like to know where the program is while its calculating the factorial")
    while(life<= x):
        value = value *life
        if(y == "yes"):
            print(life)
        life = life+1
    print(value)

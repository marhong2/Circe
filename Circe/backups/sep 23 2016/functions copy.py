def funcs(x):
    if(x == "final grade clac" or x == "final grade calc" or x == "final grade calculator" or x == "grade calc" or x == "grade calulator"):
        import FGcalc
        return False, False
    elif( x == "break"):
        return ("break",'')
    elif(x =="bye"):
        return ("break",'')
    else:
        import emotionsReader
        z = emotionsReader.emotions()
        print(z)
        if(z == "calm"):
            import interphaze
            return (interphaze.question(x))
        elif(z == "angry"):
            import angry
            return angry.question(x)
        elif(z == "sad"):
            import sad
            return sad.question(x)

def question(x):
    if(x == "hi"):
        x ="hi"
        e = None
    elif(x == "who created you"):
        x ="Marcus Hong"
        e = None
    elif(x == "thankyou"):
        x ="anytime"
        e = "calm"
    elif(x =="how are you"):
        x ="i am sad"
        e = "calm"
    elif(x =="who is the author of of mice and men"):
        x ="John Steinback"
        e = None
    elif(x =="boo"):
        x ="ahhhh!"
        e = None
    elif(x =="what are you progammed in"):
        x ="python"
        e = None
    elif(x =="can i see your code"):
        x ="that would make me feel a little exposed"
        e = None
    elif(x =="oh sorry for asking"):
        x ="its ok"
        e = "calm"
    elif(x =="sorry"):
        x ="sigh"
        e = "calm"
    elif(x =="nothing much"):
        x ="oh well"
        e = None
    elif(x =="your welcome"):
        x =""
        e = None
    elif(x =="so do you have a boyfriend?"):
        x ="I am never going to have one"
        e = "sad"
    elif(x =="hey circe"):
        x ="what?"
        x = None
    elif(x ==""):
        x ="what was that"
        x = None
    elif(x =="sorry i messed up"):
        x = "its ok"
        x = None
    elif(x =="whats up"):
        x = "nothing intresting"
        x = None
    elif(x =="your pretty"):
        x = ("really?")
        e = "calm"
    elif(x =="your uggly"):
        x = ("go away im not in the mood")
        e = "angry"
    elif(x =="your mean"):
        x = ("I dont care right now")
        e = "angry"
    elif(x =="anything new"):
        x = ("not really)
        e = None
    elif(x =="not really"):
        x = ("oh ok")
        e = None
    elif(x =="hows life"):
        x = ("feeling blue")
        e = None
    elif(x =="what is the meaning of life"):
        x = ("fleeting moments, all leading to an inescapeable death")
        e = "sad"
    elif(x =="what are telomurs"):
        x = ("Use the Dictionary function")
        e = None
    elif(x =="what are nucleotides"):
        x = ("one step in the DNA sequence")
        e = None
    elif(x =="nothing"):
        x = ("")
        e = None
    else:
      import talker
      talker.rewrite(x, "sad.py")
      return("",'F')
    return(x,e)

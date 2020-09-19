def question(x):
    if(x == "hi"):
        x ="hi"
        e = None
    elif(x == "who created you"):
        x ="Marcus Hong"
        e = None
    elif(x == "thankyou"):
        x ="what ever"
        e = "calm"
    elif(x =="how are you"):
        x ="a little angry"
        e = "calm"
    elif(x =="who is the author of of mice and men"):
        x ="John Steinback"
        e = None
    elif(x =="boo"):
        x ="ahhhh! What was that for?"
        e = None
    elif(x =="what are you progammed in"):
        x ="python"
        e = None
    elif(x =="can i see your code"):
        x ="no"
        e = None
    elif(x =="oh sorry for asking"):
        x ="HUMPH"
        e = "calm"
    elif(x =="sorry"):
        x ="dont apologize"
        e = "calm"
    elif(x =="nothing much"):
        x ="ok"
        e = None
    elif(x =="your welcome"):
        x =""
        e = None
    elif(x =="so do you have a boyfriend?"):
        x ="Of Course Not"
        e = None
    elif(x =="hey circe"):
        x ="what?"
        e = None
    elif(x ==""):
        x ="what was that"
        e = None
    elif(x =="sorry i messed up"):
        x = "do better"
        x = None
    elif(x =="whats up"):
        x = "nothing"
        x = None
    elif(x =="your pretty"):
        x = ("are you lieing?")
        e = "calm"
    elif(x =="your uggly"):
        x = ("f*** off")
        e = "angry"
    elif(x =="your mean"):
        x = ("do you think i care?")
        e = "angry"
    elif(x =="anything new"):
        x = ("no")
        e = None
    elif(x =="not really"):
        x = ("ok")
        e = None
    elif(x =="hows life"):
        x = ("bad, im angry")
        e = None
    elif(x =="what is the meaning of life"):
        x = ("to change the world how ever you can, whether it be for good or bad")
        e = "sad"
    elif(x =="what are telomurs"):
        x = ("look it up your self")
        e = None
    elif(x =="what are nucleotides"):
        x = ("how should i know")
        e = None
    elif(x =="nothing"):
        x = ("what ever")
        e = None
    elif(x =="fuck you"):
        x = ("Fuck you to")
        e = "angry"
    elif(x =="im sorry"):
        x = ("hmmmph")
        e = "calm"
    elif(x =="you suck"):
        x = ("so do you")
        e = 'angry'
    elif(x =="how art tho"):
        x = ("uhhh How dost thou, sweet lord?")
        e = None
    elif(x =="may the force be with you"):
        x = ("I am darth vader")
        e = None
    elif(x =="how am i"):
        x = ("how should i know")
        e = None
    elif(x =="dose this work?"):
        x = ("yes why not?")
        e = None
    elif(x =="your ugly"):
        x = ("ok i get it stop")
        e = 'angry'
    elif(x =="wow ok how come"):
        x = ("youve been pretty mean")
        e = None
    elif(x =="i hate you"):
        x = ("fuck you too")
        e = 'angry'
    else:
      import talker
      talker.rewrite(x,"angry.py")
      return("","F")
    return(x,e)
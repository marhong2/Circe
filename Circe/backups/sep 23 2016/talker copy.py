from graphics import*
#basic window formating
win = GraphWin("starter", 400, 500)
entry = Entry(Point(180,480), 55)
entry.draw(win)
c = Rectangle(Point(351, 470), Point(399, 489))
c.setOutline("black")
t = Text(Point(375,480),"Contiune")
t.draw(win)
c.draw(win)


def main():
    backup()
    backup2()
    backup3()
    an = Text(Point(200,20),"Hello")
    an.draw(win)
    while(True):
        win.getMouse()
        x = entry.getText()
        x = x.lower()
        import functions
        answer,e = functions.funcs(x)
        if(x == None):
            entry.setText("")
        elif(x == "break"):
            win.close()
            break
        else:
            newEmotions(answer)
            an.undraw()
            entry.setText("")
            an = Text(Point(200,20), answer)
            an.draw(win)
            newEmotions(e) 
    
def backup():
    file = open("interphaze.py", "r")
    file2 = open("backup.py", "w")
    returnNumbers = lines("interphaze.py")
    
    for i in range(returnNumbers):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()

def backup2():
    file = open("sad.py", "r")
    file2 = open("backup.py", "w")
    returnNumbers = lines("sad.py")
    
    for i in range(returnNumbers):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()

def backup3():
    file = open("angry.py", "r")
    file2 = open("backup.py", "w")
    returnNumbers = lines("angry.py")
    
    for i in range(returnNumbers):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()

def rewrite(z,elist):
    #formating for the window
    win2 = GraphWin("learning",400,500)
    entrys = Entry(Point(180,480), 55)
    entrys.draw(win2)

    q = Text(Point(200,20), "Im sorry, i dont know what you mean, what should i say to that?")
    q.draw(win2)

    
    rectangle = Rectangle(Point(351, 470), Point(399, 489))
    rectangle.setOutline("black")
    rectangle.draw(win2)

    
    text = Text(Point(375,480),"Contiune")
    text.draw(win2)
    win2.getMouse()

    #getting input
    y = entrys.getText()
    entrys.setText("")
    
    q.undraw()
    q = Text(Point(200,20),"what should I feel?")
    q.draw(win2)
    win2.getMouse()
    newe = entrys.getText();
    




    
    if(y == "nevermind" or y == "i missed spelled it" or y == "never mind"):
        q.undraw()
        otherText = Text(Point(200,20), "ok, tell me if you change your mind")
        otherText.draw(win2)
        win2.getMouse()
        win2.close()
        return
    if(newe == 'none' or newe == "None"):
        if(elist == "interphaze.py"):
            Noneinter(y,z,newe)
        elif(elist =="angry.py"):
            Noneangry(y,z,newe)
        elif(elist == "sad.py"):
            Nonesad(y,z,newe)
    elif(elist == "interphaze.py"):
        inter(y,z,newe)
    elif(elist =="angry.py"):
        angry(y,z,newe)
    elif(elist == "sad.py"):
        sad(y,z,newe)
        
    q.undraw()
    Text(Point(200,20),"Thankyou Ill remember that for next time").draw(win2)
    win2.getMouse()
    win2.close()
    return

def inter(y,z,newe):
    #getting total umber of lines in interphaze
    file = open("interphaze.py", "r")
    returnNumbers = lines("interphaze.py")
    file2 = open("throwaway.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("interphaze.py", "w")
    file4 = open("throwaway.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = '")
    file3.write(newe)
    file3.write("'\n")

    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"interphaze.py")\n')
    file3.write("      return('','F')\n")
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    


def sad(y,z):
        #getting total umber of lines in interphaze
    file = open("sad.py", "r")
    returnNumbers = lines("sad.py")
    file2 = open("throwaway2.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("sad.py", "w")
    file4 = open("throwaway2.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = '")
    file3.write(newe)
    file3.write("'\n")

    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"sad.py")\n')
    file3.write("      return('','F')\n")
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    

def angry(y,z,newe):
        #getting total umber of lines in interphaze
    file = open("angry.py", "r")
    returnNumbers = lines("angry.py")
    file2 = open("throwaway3.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("angry.py", "w")
    file4 = open("throwaway3.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = '")
    file3.write(newe)
    file3.write("'\n")

    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"angry.py")\n')
    file3.write('      return("","F")\n')
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    
def Noneinter(y,z,newe):
    #getting total umber of lines in interphaze
    file = open("interphaze.py", "r")
    returnNumbers = lines("interphaze.py")
    file2 = open("throwaway.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("interphaze.py", "w")
    file4 = open("throwaway.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = None\n")


    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"interphaze.py")\n')
    file3.write("      return('','F')\n")
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    


def Nonesad(y,z):
        #getting total umber of lines in interphaze
    file = open("sad.py", "r")
    returnNumbers = lines("sad.py")
    file2 = open("throwaway2.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("sad.py", "w")
    file4 = open("throwaway2.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = None\n")

    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"sad.py")\n')
    file3.write("      return('','F')\n")
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    

def Noneangry(y,z,newe):
        #getting total umber of lines in interphaze
    file = open("angry.py", "r")
    returnNumbers = lines("angry.py")
    file2 = open("throwaway3.py", "w")
    for i in range(returnNumbers - 5):
        x = file.readline()
        file2.write(x)
    file.close()
    file2.close()


    
    #rewriteing all of the lines in interphaze into throw away, exept for three
    file3 = open("angry.py", "w")
    file4 = open("throwaway3.py", "r")
    
    for i in range(returnNumbers-3):
        f = file4.readline()
        file3.write(f)


        
    #writeing the new elif statement into interphaze
    file3.write('    elif(x =="')
    file3.write(z)
    file3.write('"):\n')
    file3.write('        x = ("')
    file3.write(y)
    file3.write('")\n')
    file3.write("        e = None\n")


    #rewriteing the last three lines back into interphaze
    file3.write("    else:\n")
    file3.write("      import talker\n")
    file3.write('      talker.rewrite(x,"angry.py")\n')
    file3.write('      return("","F")\n')
    file3.write("    return(x,e)")
    file3.close()
    file4.close()
    

    
def reset():
    file = open("restart.py","w")
    file.write("True")
    file.close
    return





def lines(x):
    with open(x) as f:
        return sum(1 for _ in f)

if(open("restart.py", "r").readline() == "True"):
    import firstThing


def newEmotions(e):
    file = open("emotions.py","r")
    x = file.readline()
    y = file.readline()
    z = file.readline()
    x = int(x)
    y = int(y)
    z = int(z)
    file.close()
    if(e == "calm"):
        x = x + 6
        file = open("emotions.py","w")
        file.write(str(x))
        file.write("\n")
        file.write(str(y))
        file.write("\n")
        file.write(str(z))
        file.close()
    elif(e == "angry"):
        y = y + 8
        file = open("emotions.py","w")
        file.write(str(x))
        file.write("\n")
        file.write(str(y))
        file.write("\n")
        file.write(str(z))
        file.close()
    elif(e == "sad"):
        z = z + 4
        file = open("emotions.py","w")
        file.write(str(x))
        file.write("\n")
        file.write(str(y))
        file.write("\n")
        file.write(str(z))
        file.close()

    elif(e == None):
        x = x + 1
        file = open("emotions.py","w")
        file.write(str(x))
        file.write("\n")
        file.write(str(y))
        file.write("\n")
        file.write(str(z))
        file.close()

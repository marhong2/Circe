from graphics import*
def Grade():
    win = GraphWin("starter", 400, 500)
    entry = Entry(Point(180,480), 55)
    entry.draw(win)
    c = Rectangle(Point(351, 470), Point(399, 489))
    c.setOutline("black")
    b = Text(Point(375,480),"Continue")
    t = Text(Point(200,20),"What was it out of")
    t.draw(win)
    b.draw(win)
    c.draw(win)


    
    file = open("Apush C Grade.py", "r")
    current_Points = file.readline()
    current_Points = int(current_Points)
    total_Points = file.readline()
    total_Points = int(total_Points)
    file.close()
    win.getMouse()


    
    Answer = entry.getText()
    Answer = int(Answer)
    total_Points = total_Points + Answer
    t.undraw()
    t = Text(Point(200,20),"What did you get?")
    t.draw(win)
    win.getMouse()
    t.undraw()
    


    PointGot = entry.getText()
    PointGot = int(PointGot)
    current_Points = current_Points + PointGot
    theText = current_Points/total_Points
    theText=str(theText)

    t = Text(Point(200,20),theText)
    t.draw(win)

    current_Points = str(current_Points)
    total_Points = str(total_Points)
    
    file = open("Apush C Grade.py","w")
    file.write(current_Points)
    file.write("\n")
    file.write(total_Points)
    file.close()
    win.getMouse()
Grade()
    
    
    
    
    

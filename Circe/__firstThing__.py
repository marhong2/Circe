from graphics import*
def starter():
    win = GraphWin("starter", 400, 500)
    entry = Entry(Point(180,480), 55)
    entry.draw(win)
    c = Rectangle(Point(351, 470), Point(399, 489))
    c.setOutline("black")
    t = Text(Point(375,480),"Contiune")
    t.draw(win)
    c.draw(win)
    
    q = "hi"
    while(True):
        win.getMouse()
        q = entry.getText()
        if(q == "hey circe" or q == "hi circe"):
            break
        entry.setText("")
    win.close()
    import talker
    talker.main()
starter()

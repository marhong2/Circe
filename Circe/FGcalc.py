from graphics import*
def finalGrade():
    win = GraphWin()
    entry = Entry(Point(200,20), 10)
    entry2 = Entry(Point(200, 40), 10)
    entry3 = Entry(Point(200, 60), 10)
    txt = Text(Point(100, 20), "Current Grade")
    txt2 = Text(Point(100, 40), "Aceptible grade")
    txt3 = Text(Point(100, 60), "final weight/%")
    txt4 = Text(Point(325,30),"continue")
    box = Rectangle(Point(300,20), Point(350, 40))
    box.setOutline("black")
    txt4.draw(win)
    box.draw(win)
    entry.draw(win)
    entry2.draw(win)
    entry3.draw(win)
    txt.draw(win)
    txt2.draw(win)
    txt3.draw(win)
    win.getMouse()
    try:
        requiredGrade = eval(entry2.getText())
        currentGrade = eval(entry.getText())
        w = eval(entry3.getText())
    except ValueError:
        errortxt = Text(Point(150, 100), "This is not a valid input")
        errortxt.draw(win)
        return
    

    finalGrade = ( 100 * requiredGrade - (100 - w) * currentGrade ) / w
    fG = Text(Point(300, 200), "the lowest percent your final can be in order to get your desiered grade is")
    fG.draw(win)
    Text(Point(250, 250), finalGrade).draw(win)
    win.getMouse()
    win.close()
finalGrade()

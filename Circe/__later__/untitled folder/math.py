from graphics import*
win = GraphWin()
def main(textEntry):
    x = Entry(Point(350,100),50)
    x.setText(textEntry)
    z = Text(Point(350,60),"What is your equation?")
    f = Text(Point(300,100), "Enter")
    f.setFill("black")

    x.draw(win)
    z.draw(win)
    f.draw(win)

    
    win.getMouse()
    y = eval(x.getText())
    
    main(y)
main("0.0")

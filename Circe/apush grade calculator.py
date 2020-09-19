def graphics():
    from graphics import*
graphics()
window = GraphWin("Apush Calculator", 400, 500)
entry = Entry(Point(180,480), 55)
entry.draw(window)
c = Rectangle(Point(351, 470), Point(399, 489))
c.setOutline("black")
t = Text(Point(375,480),"Contiune")
t.draw(window)
c.draw(window)
def Grade():
    file = open("Apush C Grade", "r")
    current_Points = file.readline()
    Current_Points = int(current_Points)
    total_Points = file.readline()
    total_Points = int(total_Points)
    

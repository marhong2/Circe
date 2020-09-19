from graphics import*
win3 = GraphWin("apps", 400,500)
entry3 = Entry(Point(180,480), 55)
entry3.draw(win3)
c3 = Rectangle(Point(351, 470), Point(399, 489))
c3.setOutline("black")
t3 = Text(Point(375,480),"Contiune")
t3.draw(win3)
c3.draw(win3)
ask = Text(Point(200,20),"Whats up?")
ask.draw(win3)
win3.getMouse()
s = entry3.getText()

import os
os.system("open /Applications/"+s+".app")
win3.close()

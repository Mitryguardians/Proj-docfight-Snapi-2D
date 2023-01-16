def setup():
    size(400,400)
    background("#000000")
def draw():
    textSize(24)
    fill("#FF0000")
    text("Welcome", 155,30)
    
    bgrect = "#987F7F"
    colorfill = "#00E51C"
    fill(bgrect)
    stroke(colorfill)
    strokeWeight(2)
    rect(50,100,150,30)
    fill("#ffffff")
    text('Join game',60, 125)
    
    rect(50,150,150,30)
    fill("#000000")
    text('Exit',100, 175)

def mouseClicked():
    if((mouseX >50 and mouseX<200)and(mouseY >100 and mouseY <130)):
        print("You join game")
    if((mouseX >50 and mouseX<200)and(mouseY >150 and mouseY <170)):
        print("exit")
        exit()

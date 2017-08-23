'''Cloning Dave's Hexagons'''

sz = 60
t = 0.0
dt = 0.5

def setup():
    size(600,600)
    noFill()
    
def draw():
    global t,dt
    background(0)
    for x in range(10):
        for y in range(20):
            shift = 0.572 #map(mouseX,0,600,0.0,1.0)
            pushMatrix()
            if y % 2==0:
                translate(1.*sz + 2*sz*x,shift*sz*y)
            else: translate(2*sz*x,shift*sz*y)
            rotate(0.1*t)
            hexagon()
            popMatrix()
    t += dt
    textSize(24)
    #text(shift,40,40)
def hexagon():
    global sz
    strokeWeight(3)
    stroke(255,0,0)
    beginShape()
    for i in range(6):
        vertex(sz*cos(radians(60*i)),
               sz*sin(radians(60*i)))
    endShape(CLOSE)
        
    
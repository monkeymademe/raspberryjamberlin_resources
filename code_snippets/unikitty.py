import unicornhat as unicorn
import time

unicorn.brightness(0.2)

p = [204, 0, 204] # Pink
g = [0, 102, 102] # Gray
w = [200, 200, 200] # White
y = [204, 204, 0] # Yellow
e = [0, 0, 0] # Empty

pet1 = [
    [e, e, e, e, e, e, e, e],
    [p, e, e, e, e, e, e, e],
    [e, p, e, e, p, e, p, e],
    [e, p, g, g, p, w, w, e],
    [e, g, g, g, w, y, w, y],
    [e, g, g, g, g, w, w, e],
    [e, g, e, g, e, g, e, e],
    [e, e, e, e, e, e, e, e]
    ]

pet2 = [
    [e, e, e, e, e, e, e, e],
    [p, e, e, e, e, e, e, e],
    [e, p, e, e, p, e, p, e],
    [e, p, g, g, p, w, w, e],
    [e, g, g, g, w, y, w, y],
    [e, g, g, g, g, w, w, e],
    [e, e, g, e, g, e, e, e],
    [e, e, e, e, e, e, e, e]
    ]

def drawpet(pet):
	for y in range(8):
		for x in range(8):
			#set pixel with color
			unicorn.set_pixel(x,y,pet[x][y][0],pet[x][y][1],pet[x][y][2])
	unicorn.show()
while True:
	drawpet(pet1)
	time.sleep(0.5)
	drawpet(pet2)
	time.sleep(0.5)


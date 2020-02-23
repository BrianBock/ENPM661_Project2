import numpy as np


trialmaze=np.full((100,200)," ")


# Create the square
square_x=90
square_y=40 # Defined from the upper right corner

for x in range (square_x,square_x+20):
	for y in range(square_y,square_y+20):
		trialmaze[y][x]="#"


radius=15
circle_boundbox_x=160-radius
circle_boundbox_y=100-50-radius

for x in range (circle_boundbox_x,circle_boundbox_x+radius):
	for y in range(circle_boundbox_y,circle_boundbox_y+radius):
		if((x-160)^2+(y-50)^2<radius^2):
			trialmaze[y][x]="#"	


print(trialmaze)
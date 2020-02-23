import numpy as np

def mazeMaker(mazetype): #mazetype can be either "Trial" or "Final"

	if(mazetype.lower()=="trial"):
		print("Generating trial maze....")
		width=200
		height=100
		trialmaze=np.full((height,width)," ")


		# Create the square
		square_x=90
		square_y=40 # Defined from the upper right corner

		for x in range (square_x,square_x+20):
			for y in range(square_y,square_y+20):
				trialmaze[y][x]="#"


		radius=15
		circle_boundbox_x=160-radius #Upper left corner of the bounding box around the circle
		circle_boundbox_y=100-50-radius#Upper left corner of the bounding box around the circle

		for x in range (circle_boundbox_x,circle_boundbox_x+2*radius):
			for y in range(circle_boundbox_y,circle_boundbox_y+2*radius):
				if((x-160)^2+(y-50)^2<radius^2):
					trialmaze[y][x]="#"	


		print(trialmaze)
		return trialmaze








	if (mazetype.lower()=="final"):
		print("Generating final maze....")
		width=300
		height=200
		finalmaze=np.full((height,width)," ")


		# Generate circle obstacle
		radius=25
		circle_centerx=300-75
		circle_centery=50
		circle_boundbox_x=circle_centerx-radius#Upper left corner of the bounding box around the circle
		circle_boundbox_y=circle_centery-radius#Upper left corner of the bounding box around the circle


		for x in range (circle_boundbox_x,circle_boundbox_x+2*radius):
			for y in range(circle_boundbox_y,circle_boundbox_y+2*radius):
				if((x-circle_centerx)^2+(y-circle_centery)^2<radius^2):
					finalmaze[y][x]="#"	




		# Generate ellipse obstacle
		ellipse_centerx=150
		ellipse_centery=100
		ellipse_major=40
		ellipse_minor=20
		for x in range (circle_boundbox_x,circle_boundbox_x+2*radius):
		for y in range(circle_boundbox_y,circle_boundbox_y+2*radius):
			if(((x-ellipse_centerx)^2/ellipse_major^2)+((y-ellipse_centery)^2/ellipse_minor^2)<=1):
					finalmaze[y][x]="#"


		# Generate diamond obstacle


		# Generate rectangle obstacle



		# Generate 6-poly obstacle



		return finalmaze



mazeMaker(final)









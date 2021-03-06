import numpy as np
import cv2
import math
from functions import*

def mazeMaker(mazetype): #mazetype can be either "Trial" or "Final"

	if(mazetype.lower()=="trial"):
		print("Generating trial maze....")
		width=200
		height=100
		trialmaze=np.full((height,width),1)


		# Create the square
		square_x=90
		square_y=40 # Defined from the upper right corner

		for x in range (square_x,square_x+20):
			for y in range(square_y,square_y+20):
				trialmaze[y][x]=2


		radius=15
		circle_boundbox_x=160-radius #Upper left corner of the bounding box around the circle
		circle_boundbox_y=100-50-radius#Upper left corner of the bounding box around the circle

		for x in range (circle_boundbox_x,circle_boundbox_x+2*radius):
			for y in range(circle_boundbox_y,circle_boundbox_y+2*radius):
				if((x-160)**2+(y-50)**2<radius**2):
					trialmaze[y][x]=2


		#print(trialmaze)
		print("Trial Maze generated.")
		return trialmaze








	if (mazetype.lower()=="final"):
		print("Generating final maze....")
		width=300
		height=200
		finalmaze=np.zeros((height,width,3),np.uint8)
		# finalmaze=np.full((height,width),1)


		# Generate circle obstacle
		radius=25
		circle_centerx=300-75
		circle_centery=50
		circle_boundbox_x=circle_centerx-radius #Upper left corner of the bounding box around the circle
		circle_boundbox_y=circle_centery-radius#Upper left corner of the bounding box around the circle

		for x in range (circle_boundbox_x,circle_boundbox_x+2*radius):
			for y in range(circle_boundbox_y,circle_boundbox_y+2*radius):
				if((x-circle_centerx)**2+(y-circle_centery)**2<radius**2):
					finalmaze[y][x]=(255,255,255)

		

		# Generate ellipse obstacle
		ellipse_centerx=150
		ellipse_centery=100
		ellipse_major=40
		ellipse_minor=20
		ellipse_boundbox_x=110
		ellipse_boundbox_y=80
		for x in range (ellipse_boundbox_x,circle_boundbox_x+2*ellipse_major):
			for y in range(ellipse_boundbox_y,ellipse_boundbox_y+2*ellipse_minor):
				if(((x-ellipse_centerx)**2/ellipse_major**2)+((y-ellipse_centery)**2/ellipse_minor**2)<=1):
					# print("making ellipse")
					finalmaze[y][x]=(255,255,255)



		# Generate diamond obstacle
		diamondpts=np.array([[225,190],[250,175],[225,160],[200,175]])
		# print(diamondpts[0][0])
		diamond_slopes=[]
		diamond_slopes.append(getSlope(diamondpts[0][0],diamondpts[0][1],diamondpts[1][0],diamondpts[1][1]))
		diamond_slopes.append(getSlope(diamondpts[1][0],diamondpts[1][1],diamondpts[2][0],diamondpts[2][1]))
		diamond_slopes.append(getSlope(diamondpts[2][0],diamondpts[2][1],diamondpts[3][0],diamondpts[3][1]))
		diamond_slopes.append(getSlope(diamondpts[3][0],diamondpts[3][1],diamondpts[0][0],diamondpts[0][1]))

		diamond_b=[]
		diamond_b.append(getIntercept(diamondpts[0][0],diamondpts[0][1],diamondpts[1][0],diamondpts[1][1]))
		diamond_b.append(getIntercept(diamondpts[1][0],diamondpts[1][1],diamondpts[2][0],diamondpts[2][1]))
		diamond_b.append(getIntercept(diamondpts[2][0],diamondpts[2][1],diamondpts[3][0],diamondpts[3][1]))
		diamond_b.append(getIntercept(diamondpts[3][0],diamondpts[3][1],diamondpts[0][0],diamondpts[0][1]))

		# print("Done with diamond slopes and intercepts")
		# print(diamond_b1)
		# cv2.drawContours(finalmaze,[diamondpts],-1,(255,255,255),-1)

		# Half Planes for Diamond
		for x in range(200, 251):
			for y in range(160,191):
				y1=diamond_slopes[2]*x+diamond_b[2]
				y2=diamond_slopes[0]*x+diamond_b[0]
				y3=diamond_slopes[1]*x+diamond_b[1]
				y4=diamond_slopes[3]*x+diamond_b[3]
				# print(y1,y2,y3,y4)
				if (y>=y1) and (y>=y3) and (y<=y4) and (y<=y2):
					# print("making diamond")
					finalmaze[y][x]=(255,255,255)


		# Generate rectangle obstacle
		x1=95
		y1=170
		x2=x1-int(75*math.cos(math.radians(30)))
		y2=170-int(75*math.sin(math.radians(30)))
		x3=x2+int(10*math.cos(math.radians(60)))
		y3=y2-int(10*math.sin(math.radians(60)))
		x4=x3+int(75*math.cos(math.radians(30)))
		y4=y3+int(75*math.sin(math.radians(30)))
		rectpoints=np.array([[x1,y1], [x2,y2],[x3,y3], [x4,y4]])
		rect_slopes=[]
		rect_slopes.append(getSlope(x1,y1,x2,y2))
		rect_slopes.append(getSlope(x2,y2,x3,y3))
		rect_slopes.append(getSlope(x3,y3,x4,y4))
		rect_slopes.append(getSlope(x4,y4,x1,y1))

		rect_b=[]
		rect_b.append(getIntercept(x1,y1,x2,y2))
		rect_b.append(getIntercept(x2,y2,x3,y3))
		rect_b.append(getIntercept(x3,y3,x4,y4))
		rect_b.append(getIntercept(x4,y4,x1,y1))

		# print(x2,x4)
		# print(y3,y1)

		rect_y1=y1
		rect_y3=y3
		rect_x2=x2
		rect_x4=x4

		# Half Planes for Rectangle
		for x in range(int(rect_x2), int(rect_x4)):
			for y in range(int(rect_y3),int(rect_y1)):
				y1=rect_slopes[1]*x+rect_b[1]
				y2=rect_slopes[3]*x+rect_b[3]
				y3=rect_slopes[2]*x+rect_b[2]
				y4=rect_slopes[0]*x+rect_b[0]
				# print(y,y1,y2,y3,y4)

				if y>=y1 and y>=y3 and y<=y4 and y<=y2:
					finalmaze[y][x]=(255,255,255)



		# cv2.drawContours(finalmaze,[rectpoints],-1,(255,255,255),-1)
		#print("rect complt")

		# Generate 6-poly obstacle
		polypts=np.array([[25,15], [75,15], [100,50], [75,80], [50,50], [20,80]])
		poly_slopes1=[] # the triangle(ish) shape on the left half of the polygon
		poly_slopes1.append(getSlope(polypts[0][0],polypts[0][1],polypts[1][0],polypts[1][1]))
		poly_slopes1.append(getSlope(polypts[1][0],polypts[1][1],polypts[4][0],polypts[4][1]))
		poly_slopes1.append(getSlope(polypts[4][0],polypts[4][1],polypts[5][0],polypts[5][1]))
		poly_slopes1.append(getSlope(polypts[5][0],polypts[5][1],polypts[0][0],polypts[0][1]))

		poly1_b=[]
		poly1_b.append(getIntercept(polypts[0][0],polypts[0][1],polypts[1][0],polypts[1][1]))
		poly1_b.append(getIntercept(polypts[1][0],polypts[1][1],polypts[4][0],polypts[4][1]))
		poly1_b.append(getIntercept(polypts[4][0],polypts[4][1],polypts[5][0],polypts[5][1]))
		poly1_b.append(getIntercept(polypts[5][0],polypts[5][1],polypts[0][0],polypts[0][1]))


		# Half Planes for Left Half of polygon
		for x in range(20, 75):
			for y in range(15,80):
				y1=poly_slopes1[1]*x+poly1_b[1]
				y2=poly_slopes1[3]*x+poly1_b[3]
				y3=poly_slopes1[2]*x+poly1_b[2]
				y4=poly_slopes1[0]*x+poly1_b[0]

				if y<y1 and y<y3 and y>y4 and y>y2:
					finalmaze[y][x]=(255,255,255)


		poly_slopes2=[] # the diamond shape on the right half of the polygon
		poly_slopes2.append(getSlope(polypts[1][0],polypts[1][1],polypts[2][0],polypts[2][1]))
		poly_slopes2.append(getSlope(polypts[2][0],polypts[2][1],polypts[3][0],polypts[3][1]))
		poly_slopes2.append(getSlope(polypts[3][0],polypts[3][1],polypts[4][0],polypts[4][1]))
		poly_slopes2.append(getSlope(polypts[4][0],polypts[4][1],polypts[1][0],polypts[1][1]))

		poly2_b=[]
		poly2_b.append(getIntercept(polypts[1][0],polypts[1][1],polypts[2][0],polypts[2][1]))
		poly2_b.append(getIntercept(polypts[2][0],polypts[2][1],polypts[3][0],polypts[3][1]))
		poly2_b.append(getIntercept(polypts[3][0],polypts[3][1],polypts[4][0],polypts[4][1]))
		poly2_b.append(getIntercept(polypts[4][0],polypts[4][1],polypts[1][0],polypts[1][1]))


		# Half Planes for Right Half of polygon
		for x in range(50, 100):
			for y in range(15,80):
				y1=poly_slopes2[3]*x+poly2_b[3]
				y2=poly_slopes2[1]*x+poly2_b[1]
				y3=poly_slopes2[0]*x+poly2_b[0]
				y4=poly_slopes2[2]*x+poly2_b[2]

				if (y>=y1) and (y>=y3) and (y<=y4) and (y<=y2):
					finalmaze[y][x]=(255,255,255)


		# cv2.drawContours(finalmaze,[polypts],-1,(255,255,255),-1)
		cv2.imshow("The maze",finalmaze)
		cv2.waitKey(0)
        
        
		maze=np.empty((height,width),dtype='object')
        
		for row in range(width):
			for col in range(height):
                
                
				if finalmaze[col][row][0]==0:
					maze[col][row]=1
				elif finalmaze[col][row][0]==255:
					maze[col][row]=2
		


		print("Final Maze generated.")
		return maze


# mazeMaker("final")



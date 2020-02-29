import numpy as np
import cv2
import math

def mazeMakerTrial():
	print("Generating trial maze....")
	width=200
	height=100
	imagemaze=np.zeros((height,width),np.uint8)


	# Create the square
	corner1=(90,40)
	corner2=(110,60)
	# square_x=90
	# square_y=40 # Defined from the upper right corner
	cv2.rectangle(imagemaze, corner1,corner2, 255,-1)


	# Generate circle obstacle
	radius=15
	circle_centerx=160
	circle_centery=50
	cv2.circle(imagemaze,(circle_centerx,circle_centery),radius,(255),-1)

	# cv2.imshow("Maze",imagemaze)
	# cv2.waitKey(0)
	maze=np.empty((height,width),dtype='object')
	for row in range(0,width):
		for col in range(0,height):
			if (imagemaze[col][row]==0):
				maze[col][row]=" "
			elif(imagemaze[col][row]==255):
				maze[col][row]="#"
	# print(maze)


	#print(imagemaze)
	print("Trial Maze generated.")
	return maze


# mazeMakerTrial()



def mazeMakerFinal():
	print("Generating final maze....")
	width=300
	height=200
	imagemaze=np.zeros((height,width),np.uint8)



	# Generate circle obstacle
	radius=25
	circle_centerx=300-75
	circle_centery=50
	cv2.circle(imagemaze,(circle_centerx,circle_centery),radius,(255),-1)

	

	# Generate ellipse obstacle

	ellipse_center=(150,100) #x,y
	ellipse_axes=(40,20) #major, minor axis

	
	cv2.ellipse(imagemaze,ellipse_center,ellipse_axes,0,0,360,255,-1)

	# Generate diamond obstacle
	diamondpts=np.array([[225,190],[250,175],[225,160],[200,175]])
	cv2.drawContours(imagemaze,[diamondpts],-1,255,-1)


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
	cv2.drawContours(imagemaze,[rectpoints],-1,255,-1)
	

	# Generate 6-poly obstacle
	polypts=np.array([[25,15], [75,15], [100,50], [75,80], [50,50], [20,80]])
	cv2.drawContours(imagemaze,[polypts],-1,255,-1)
	# cv2.imshow("The maze",imagemaze)
	# cv2.waitKey(0)

	maze=np.empty((height,width),dtype='object')
	for row in range(0,width):
		for col in range(0,height):
			if (imagemaze[col][row]==0):
				maze[col][row]=" "
			elif(imagemaze[col][row]==255):
				maze[col][row]="#"
	#print(maze)


	print("Final Maze generated.")
	return maze



#mazeMakerFinal()

def mazeMaker(mazetype):
	if mazetype.lower()=="trial":
		return mazeMakerTrial()
	elif mazetype.lower()=="final":
		return mazeMakerFinal()
	else:
		print("Invalid maze type selected. Quitting")
		exit()








from functions import*
from djikstra import*

print("Welcome to our djikstra solver!")

type_needed=True

while type_needed==True:
	solver_type = input("Which solver would you like to run? \nFor a point robot, enter 'point'. For a rigid robot, enter 'rigid'.\n") 

	if solver_type.lower()=="point":
		print("Point robot selected")
		robot_type="point"
		type_needed=False
		diameter=0
		clearance=0

	elif solver_type.lower()=="rigid":
		print("Rigid robot selected.")
		robot_type="rigid"
		type_needed=False
		diameter,clearance=input("Enter the robot diameter and clearance 'd c':\n").split()
		diameter=int(diameter)
		clearance=int(clearance)

	else:
		print("Invalid robot type entered. Please try again.")
		type_needed=True


maze_needed=True
while maze_needed==True:
	maze_type = input("Which maze would you like to try? \nFor the trial maze, enter 'trial'. For the final maze, enter 'final'.\n") 

	if maze_type.lower()=="trial":
		print("Trial maze selected")
		mazetype="trial"
		maze_needed=False

	elif maze_type.lower()=="final":
		print("Final maze selected.")
		mazetype="final"
		maze_needed=False

	else:
		print("Invalid maze type entered. Please try again.")
		maze_needed=True

startx,starty=input("Enter the start position 'x y':\n").split()
startx=int(startx)
starty=int(starty)
goalx,goaly=input("Enter the goal position 'x y':\n").split()
goalx=int(goalx)
goaly=int(goaly)


djikstra(robot_type,mazetype,startx,starty,goalx,goaly,diameter,clearance)



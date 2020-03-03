
from functions import*
# from djikstra import*

print("Welcome to our djikstra solver!")

type_needed=True

while type_needed==True:
	solver_type = input("Which solver would you like to run? \nFor a point robot, enter 'point'. For a rigid robot, enter 'rigid'.\n") 

	if solver_type.lower()=="point":
		print("Point robot selected")
		type_needed=False

	elif solver_type.lower()=="rigid":
		print("Rigid robot selected.")
		type_needed=False

	else:
		print("Invalid robot type entered. Please try again.")
		type_needed=True


maze_needed=True
while maze_needed==True:
	maze_type = input("Which maze would you like to try? \nFor the trial maze, enter 'trial'. For the final maze, enter 'final'.\n") 

	if maze_type.lower()=="trial":
		print("Trial maze selected")
		maze_needed=False

	elif maze_type.lower()=="final":
		print("Final maze selected.")
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





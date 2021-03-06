# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:44:26 2020

@author: bbock and prana
"""
import numpy as np
import matplotlib.pyplot as plt
from mazemaker_halfplanes import*
from functions import*
import cv2
import datetime
from datetime import datetime as dtime
import imutils
import time




def robotInspace(x,y,d,maze):
    if maze[x][y]==2:
        return False
    if (d*d)-(x*x)>0:
        return False
    if (d*d)-(y*y)>0:
        return False
    if x+d+1>len(maze)    or   y+d+1>len(maze[0]):
        return False
    for i in range(12):
        x1=x+(d*np.cos(2*3.14159/12*(i)))
        y1=y+(d*np.sin(2*3.14159/12*(i)))
        if maze[int(x1)][int(y1)]==2:
            return False
    return True
        






def rigid_dijkstra(mazetype,start,goal,diameter,clearance):
    # write_to_video=True

    starttime = dtime.now()

    d=(diameter/2)+clearance
    robot_radius=diameter/2
    print("Sol of dijkstra")
    maze=mazeMaker(mazetype)
    if maze[goal[0]][goal[1]]==2    or   maze[start[0]][start[1]]==2:
        print("Cannot solve as start or goal is inside obstacle")
        return
    
    maze[start[0]][start[1]]=5
    maze[goal[0]][goal[1]]=6
    
    

    maze_size=[len(maze),len(maze[0])]
    maze_height=len(maze)
    maze_width=len(maze[0])

    my_maze=np.zeros((maze_size))



    # Define the codec and initialize the output file
    # if write_to_video:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    today = time.strftime("%m-%d__%H.%M.%S")
    videoname="Rigid"+str(mazetype)+"-s("+str(start[0])+","+str(start[0])+")g("+str(goal[0])+","+str(goal[1])+")"+str(today)+".avi"
    fps_out = 500
    video_out = cv2.VideoWriter(str(videoname), fourcc, fps_out, (maze_width, maze_height))
    # video_out=cv2.VideoWriter(str(videoname)+".avi",cv2.VideoWriter_fourcc('M','J','P','G'),100,(maze_height,maze_width))
    print("Writing to Video, Please Wait")


    my_maze=maze
    my_maze[start[0]][start[1]]=5
    my_maze[goal[0]][goal[1]]=6
    print(maze_size)



    output=np.zeros((maze_height, maze_width,3),np.uint8)
    for y in range (len(maze)):
        for x in range(len(maze[0])):
            if my_maze[y][x]==2:
                output[y][x]=(0,0,255)
    # cv2.imshow("Output", output)



    distance_from_start=np.zeros((maze_size))
    parent=np.zeros(([maze_size[0],maze_size[1],2]))
    

            
    distance_from_start=np.full((maze_size[0],maze_size[1]), np.inf)
    numExpanded=0
    distance_from_start[start[0]][start[1]]=0
    
    
    current=start
    expanded=[]
    expanded.append(start)

    if robotInspace(start[0],start[1],d,maze)==False     or  robotInspace(goal[0],goal[1],d,maze)==False   :
            print("Could not solve")
            return

    while 1:
        my_maze[start[0]][start[1]]=5
        my_maze[goal[0]][goal[1]]=6
        
        min_dist=float('inf')

                
        for c in expanded:
            if min_dist>distance_from_start[c[0]][c[1]]:
                min_dist=distance_from_start[c[0]][c[1]]
                current=c
                    
                
        #print(current)
        if current==goal  or min_dist==float('inf'):
            break
        my_maze[current[0]][current[1]]=3                           #node is visited
        output=addToVideo(output,current[0],current[1],3,video_out,[False,0])

        expanded.remove(current)
        distance_from_start[current[0]][current[1]]=float('inf')     #so that next node is explored
        
        if current[1]<maze_size[1]-1     and   robotInspace(current[0],current[1]+1,d,maze)==True:
            right1=[current[0],current[1]+1]
        else:
            right1=current                                  #right
            
        
        if current[1]>0      and   robotInspace(current[0],current[1]-1,d,maze)==True:
           left1=[current[0],current[1]-1]
        else:                                                  #left
            left1=current                
            
            
        if current[0]<maze_size[0]-1     and      robotInspace(current[0]+1,current[1],d,maze)==True:
            down1=[current[0]+1,current[1]]
        else:                                                   #down                       
            down1=current
        

        if current[0]>0      and   robotInspace(current[0]-1,current[1],d,maze)==True :
            up1=[current[0]-1,current[1]]
        else:                                                   #up                       
            up1=current
        
        
        if current[0]<maze_size[0]-1  and  current[1]<maze_size[1]-1    and   robotInspace(current[0]+1,current[1]+1,d,maze)==True :
            downright=[current[0]+1,current[1]+1]     # down   right
        else:                                                                          
            downright=current
            
            
        
        if current[0]<maze_size[0]-1  and  current[1]>0       and   robotInspace(current[0]+1,current[1]-1,d,maze)==True:
            downleft=[current[0]+1,current[1]-1]     # down   left
        else:                                                                          
            downleft=current


        if current[0]>0  and  current[1]>0     and   robotInspace(current[0]-1,current[1]-1,d,maze)==True :
            upleft=[current[0]-1,current[1]-1]     # up   left
        else:                                                                          
            upleft=current
            
            
        
        if current[0]>0  and  current[1]<maze_size[1]-1    and   robotInspace(current[0]-1,current[1]+1,d,maze)==True :
            upright=[current[0]-1,current[1]+1]     # up   right
        else:                                                                          
            upright=current


        adjacent=[]
        adjacent.append(up1)
        adjacent.append(down1)
        adjacent.append(left1)
        adjacent.append(right1)
        adjacent.append(upleft)
        adjacent.append(upright)
        adjacent.append(downleft)
        adjacent.append(downright)
        temp=0
        
        for n in range(len(adjacent)):
            #Node is either unvisited/empty     or      looked at     or     goal     that is should not be visited or should not be a obstacle
            if my_maze [int(adjacent[n][0])] [int(adjacent[n][1])] ==1    or  my_maze[adjacent[n][0]][adjacent[n][1]]==4   or  my_maze[adjacent[n][0]][adjacent[n][1]]==6 :
                if  distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])] > min_dist+dist(current,adjacent[n]):
                    distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])]=min_dist+dist(current,adjacent[n])
                    
                    parent[int(adjacent[n][0])] [int(adjacent[n][1])]=current
                    temp=n                #so that we know the node entered this loop
                my_maze[int(adjacent[n][0])] [int(adjacent[n][1])]=4                               #node is looked at
                output=addToVideo(output,int(adjacent[n][0]),int(adjacent[n][1]),4,video_out, [False,0])

                expanded.append(adjacent[n])
        
        numExpanded=numExpanded+1
        current=adjacent[temp]
        
        #print(distance_from_start)
        #time.sleep(1)
        #print(parent)
    route=[]
    if distance_from_start[goal[0]][goal[1]]==float('inf'):
        route=[]
    else:
        route=[goal]
        #print(([route[len(route)-1][0]][route[len(route)-1][1]][0]))
        #print(int(parent[route[len(route)-1][0]][route[len(route)-1][1]][1]))
        a=route[len(route)-1][0]
        b=route[len(route)-1][1]
        #print(parent[a][b][0])
        while parent[int(a)][int(b)][0]!=start[0]   or  parent[int(a)][int(b)][1]!=start[1]:
            a=route[len(route)-1][0]
            b=route[len(route)-1][1]
            c1=parent[int(a)][int(b)][0]
            c2=parent[int(a)][int(b)][1]
            route.append([c1,c2])

            
    #print(route)
    for i in route:
        maze[int(i[0])][int(i[1])]=0

        #Slow down path plotting at the end
        for j in range(100):
            output=addToVideo(output,int(i[0]),int(i[1]),0,video_out,[True,robot_radius])
        # print(i)
    maze[start[0]][start[1]]=5
    maze[goal[0]][goal[1]]=6

        # Pad some frames at the end of the video
    q=0
    while q<1000:
        video_out.write(output)
        q+=1

    endtime = dtime.now()
    runtime=endtime-starttime
    print("Finished in "+str(runtime)+" (hours:min:sec)")

    cv2.imshow("Final",output)
    cv2.waitKey(0)
    print("Done!")
    print("To view the animation of this run, please navigate to the directory this program was launched in and find "+str(videoname))









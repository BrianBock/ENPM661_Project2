# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:44:26 2020

@author: prana
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mazemaker import*
#from image_mazemaker import*
import datetime
from datetime import datetime as dtime
import imutils
import time

def dist(current,parent):
    dist=np.sqrt(np.square(current[0]-parent[0])+np.square(current[1]-parent[1]))
    return dist

def Write(file1,c1):                                                                        #function to write a list into a file
    for c in c1:
       file1.write(' '.join([str(elem) for elem in c])) 
       file1.write("\n") 

def listToString(s):  
 
    str1 = ""  
 
    for ele in s:  
        str1 += ele   

    return str1 


# def addToVideo(frame, x, y, status, video_out):#addToVideo(output,(x,y),3,video_out)
#     #print("Saving frame to video")
#     if status==3: # Visited
#         frame[x][y]=[0,255,255] #yellow

#     elif status==4: # Searched
#         frame[x][y]=[255,0,255] #pink

#     elif status==2: # Obstacle
#         frame[x][y]=[0,0,255] #red

#     elif status==0: # Path
#         frame[x][y]=[255,0,0] #blue

#     else:
#         print("Illegal status code")
#     video_out.write(frame)
#     #print("Frame saved")
#     #cv2.imshow("Frame",frame)
#     return frame


def addToVideo(frame, y, x, status, video_out):#addToVideo(output,(x,y),3,video_out)
    #print("Saving frame to video")
    if status==3: # Visited
        frame[y][x]=[0,255,255] #yellow

    elif status==4: # Searched
        frame[y][x]=[255,0,255] #pink

    elif status==2: # Obstacle
        frame[y][x]=[0,0,255] #red

    elif status==0: # Path
        frame[y][x]=[255,0,0] #blue

    else:
        print("Illegal status code")
    
    
    #print("Frame saved")
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)
   # video_out.write(frame)
    return frame





def maze_solver_dijkstra(start,goal):
    start_time = dtime.now()

    start_square=5
    goal_square=6
    obst_char=2
    free_space=0
    visited=3
    write_to_video=True
    mazetype="Trial"



    #print("Sol of dijkstra")
    maze=mazeMaker(mazetype)

    if maze[goal[0]][goal[1]]==obst_char     or   maze[start[0]][start[1]]==obst_char:
        print("Cannot solve as start or goal is inside obstacle")
        return
    
    maze[start[0]][start[1]]=start_square
    maze[goal[0]][goal[1]]=goal_square
    

    maze_width=len(maze[0])
    maze_height=len(maze)
    maze_size=[maze_height,maze_width]
    my_maze=np.zeros((maze_size))

    output=np.zeros((maze_height, maze_width,3),np.uint8)
    for y in range (len(maze)):
        for x in range(len(maze[0])):
            if my_maze[y][x]==2:
                output[y][x]=(0,0,255)
    cv2.imshow("Output", output)


    # Define the codec and initialize the output file
    if write_to_video:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        today = time.strftime("%m-%d__%H.%M.%S")
        videoname=str(mazetype)+str(today)
        fps_out = 500
        video_out = cv2.VideoWriter(str(videoname)+".avi", fourcc, fps_out, (maze_height, maze_width))
        print("Writing to Video, Please Wait")



    #output=mazeMaker("Trial")[0]

    print(maze_size)
    for i in range(maze_width):
        for j in range(maze_height):
            if maze[i][j]==start_square :
                my_maze[i][j]=5
            if maze[i][j]==goal_square :
                my_maze[i][j]=6                 #mark goal start and obstacles
            if maze[i][j]==" ":
                my_maze[i][j]=1
            if maze[i][j]==obst_char:
                my_maze[i][j]=2
    distance_from_start=np.zeros((maze_size))
    parent=np.zeros(([maze_size[0],maze_size[1],2]))
    
    for i in range(len(distance_from_start)):
        for j in range(len(distance_from_start[0])):
            distance_from_start[i][j]=float('inf');
    numExpanded=0
    distance_from_start[start[0]][start[1]]=0
    print("Done with this bit")
    
    current=start
    
    
    while 1:
        # my_maze[start[0]][start[1]]=5
        # my_maze[goal[0]][goal[1]]=6
        
        min_dist=float('inf')
        for i in range(len(distance_from_start)):
            for j in range(len(distance_from_start[0])):
                
                if min_dist>distance_from_start[i][j]:                  #stepping forward from the same min distance valued node in every iteration
                    #print([i,j])
                    min_dist=distance_from_start[i][j]
                    current[0]=i
                    current[1]=j
                    
                
        #print(current)
        if current==goal  or min_dist==float('inf'):
            break
        my_maze[current[0]][current[1]]=3                           #node is visited
        output=addToVideo(output,current[0],current[1],3,video_out)
        distance_from_start[current[0]][current[1]]=float('inf')     #so that next node is explored
        
        if current[1]<maze_size[1]-1:
            right1=[current[0],current[1]+1]
        else:
            right1=current                                  #right
            
        
        if current[1]>0:
           left1=[current[0],current[1]-1]
        else:                                                  #left
            left1=current                
            
            
        if current[0]<maze_size[0]-1:
            down1=[current[0]+1,current[1]]
        else:                                                   #down                       
            down1=current
        

        if current[0]>0:
            up1=[current[0]-1,current[1]]
        else:                                                   #up                       
            up1=current
        
        
        if current[0]<maze_size[0]-1  and  current[1]<maze_size[1]-1  :
            downright=[current[0]+1,current[1]+1]     # down   right
        else:                                                                          
            downright=current
            
        
        if current[0]<maze_size[0]-1  and  current[1]>0 :
            downleft=[current[0]+1,current[1]-1]     # down   left
        else:                                                                          
            downleft=current


        if current[0]>0  and  current[1]>0 :
            upleft=[current[0]-1,current[1]-1]     # up   left
        else:                                                                          
            upleft=current
            
            
        
        if current[0]>0  and  current[1]<maze_size[1]-1 :
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
            #Node is either unvisited/empty or looked at or goal that is should not be visited or should not be a obstacle
            if my_maze[int(adjacent[n][0])][int(adjacent[n][1])] ==1    or  my_maze[adjacent[n][0]][adjacent[n][1]]==4   or  my_maze[adjacent[n][0]][adjacent[n][1]]==6 and my_maze[adjacent[n][0]][adjacent[n][1]]!=2:
                if  distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])] > min_dist+dist(current,adjacent[n]):
                    distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])]=min_dist+dist(current,adjacent[n])
                    
                    parent[int(adjacent[n][0])] [int(adjacent[n][1])]=current
                    temp=n                #so that we know the node entered this loop
                my_maze[int(adjacent[n][0])] [int(adjacent[n][1])]=4  #node is looked at
                output=addToVideo(output,adjacent[n][0],adjacent[n][1],4,video_out)
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
    print("Done solving. Ready to plot")
    #output=np.zeros((maze_width,maze_height,3),np.uint8)
    for i in route:
        maze[int(i[0])][int(i[1])]="="
        output=addToVideo(output,int(i[0]),int(i[1]),"=",video_out)

        #print(i)

    # Pad some frames at the end of the video
    q=0
    while q<1000:
        video_out.write(output)
        q+=1


    maze[start[0]][start[1]]=start_square
    maze[goal[0]][goal[1]]=goal_square
    plt.axis([0,200,0,100])
    # for m in range(maze_width):
    #     for n in range(maze_height):
    #         if my_maze[m][n]==3: # Visited
    #             output[m][n]=[0,255,255] #yellow
    #             #plt.plot(n,m,'yo')
    #         if my_maze[m][n]==4: # Searched
    #             output[m][n]=[255,0,255] #pink
    #             #plt.plot(n,m,'mo')
    #         if maze[m][n]=="#": # Obstacle
    #             output[m][n]=[0,0,255] #red
    #             #plt.plot(n,m,'ro')
    #         if maze[m][n]=="=": # Path
    #             output[m][n]=[255,0,0] #blue
    #             #plt.plot(n,m,'bo')

    #output=imutils.resize(output,width=800)
    end_time=dtime.now()


    runtime=end_time-start_time
    print("Finished solve in "+str(runtime)+" (hours:min:sec)")

    cv2.imshow("Output",output)
    cv2.waitKey(0)
    #print(numExpanded)
    
      
       
        
        #print(maze)
    
    
    
maze_solver_dijkstra([0,0],[99,199])
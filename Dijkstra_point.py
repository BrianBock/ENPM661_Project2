import numpy as np
import matplotlib.pyplot as plt
import mazemaker
from functions import*
import cv2
import datetime
from datetime import datetime as dtime
import imutils
import time









def point_dijkstra(mazetype,start,goal):
    write_to_video=True
    # mazetype="trial"
    starttime = dtime.now()



    print("Sol of dijkstra")
    maze=mazemaker.mazeMaker(mazetype)
    # cv2.imshow("Orignal maze",output)
    #cv2.waitKey(0)
    if maze[goal[0]][goal[1]]==2    or   maze[start[0]][start[1]]==2:
        print("Cannot solve as start or goal is inside obstacle")
        return
    
    maze[start[0]][start[1]]=5
    maze[goal[0]][goal[1]]=6
    
    
  
    maze_size=[len(maze),len(maze[0])]
    maze_height=len(maze)
    maze_width=len(maze[0])


    # Define the codec and initialize the output file
    if write_to_video:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        today = time.strftime("%m-%d__%H.%M.%S")
        videoname="Point"+str(mazetype)+str(today)
        fps_out = 500
        video_out = cv2.VideoWriter(str(videoname)+".avi", fourcc, fps_out, (maze_width, maze_height))
        # video_out=cv2.VideoWriter(str(videoname)+".avi",cv2.VideoWriter_fourcc('M','J','P','G'),100,(maze_height,maze_width))
        print("Writing to Video, Please Wait")





    #my_maze=np.zeros((maze_size))
    my_maze=maze
    my_maze[start[0]][start[1]]=5
    my_maze[goal[0]][goal[1]]=6
    output=np.zeros((maze_height, maze_width,3),np.uint8)
    for y in range (len(maze)):
        for x in range(len(maze[0])):
            if my_maze[y][x]==2:
                output[y][x]=(0,0,255)
    # cv2.imshow("Output", output)
    print(len(output),len(output[0]))

    print(maze_size)
    #print(len(output),len(output[0]))

    distance_from_start=np.zeros((maze_size))
    parent=np.zeros(([maze_size[0],maze_size[1],2]))
    

            
    distance_from_start=np.full((maze_size[0],maze_size[1]), np.inf)
    numExpanded=0
    distance_from_start[start[0]][start[1]]=0
    
    
    current=start
    expanded=[]
    expanded.append(start)
    
    
    
    while 1:
        
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
        #print("current")
        #print(current)
        #print("expanded")
        #print(expanded)
        expanded.remove(current)
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
            #Node is either unvisited/empty     or      looked at     or     goal     that is should not be visited or should not be a obstacle
            if my_maze [int(adjacent[n][0])] [int(adjacent[n][1])] ==1    or  my_maze[adjacent[n][0]][adjacent[n][1]]==4   or  my_maze[adjacent[n][0]][adjacent[n][1]]==6 :
                if  distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])] > min_dist+dist(current,adjacent[n]):
                    distance_from_start[int(adjacent[n][0])] [int(adjacent[n][1])]=min_dist+dist(current,adjacent[n])
                    
                    parent[int(adjacent[n][0])] [int(adjacent[n][1])]=current
                    temp=n                #so that we know the node entered this loop
                    
                my_maze[int(adjacent[n][0])] [int(adjacent[n][1])]=4                               #node is looked at
                output=addToVideo(output,int(adjacent[n][0]),int(adjacent[n][1]),4,video_out,[False,0])
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
        my_maze[int(i[0])][int(i[1])]=0
        output=addToVideo(output,int(i[0]),int(i[1]),0,video_out,[False,0])
        #Slow down path plotting at the end
        for j in range(100):
            output=addToVideo(output,int(i[0]),int(i[1]),0,video_out,[False,0])
        #print(i)
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
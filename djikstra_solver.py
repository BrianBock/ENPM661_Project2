# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:44:26 2020

@author: prana
"""
import numpy as np
import matplotlib.pyplot as plt
import mazemaker
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










def maze_solver_dijkstra(start,goal):
    print("Sol of dijkstra")
    maze=mazemaker.mazeMaker("trial")
    if maze[goal[0]][goal[1]]==2    or   maze[start[0]][start[1]]==2:
        print("Cannot solve as start or goal is inside obstacle")
        return
    
    maze[start[0]][start[1]]=5
    maze[goal[0]][goal[1]]=6
    
    
  
    maze_size=[len(maze),len(maze[0])]
    #my_maze=np.zeros((maze_size))
    my_maze=maze
    my_maze[start[0]][start[1]]=5
    my_maze[goal[0]][goal[1]]=6
    print(maze_size)

    distance_from_start=np.zeros((maze_size))
    parent=np.zeros(([maze_size[0],maze_size[1],2]))
    

            
    distance_from_start=np.full((maze_size[0],maze_size[1]), np.inf)
    numExpanded=0
    distance_from_start[start[0]][start[1]]=0
    
    
    current=start
    expanded=[]
    expanded.append(start)
    
    
    
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
        print(i)
    maze[start[0]][start[1]]=5
    maze[goal[0]][goal[1]]=6
    plt.axis([0,200,0,100])
    for m in range(len(maze)):
        for n in range(len(maze[0])):
            #if my_maze[m][n]==3:
                #plt.plot(n,m,'yo')
            #if my_maze[m][n]==4:
                #plt.plot(n,m,'mo')
            if my_maze[m][n]==2:
                plt.plot(n,m,'ro')
            if maze[m][n]==0:
                plt.plot(n,m,'bo')
            
    print(numExpanded)            
    plt.show()
        
        
        #print(maze)
    
    
    
maze_solver_dijkstra([0,0],[40,40])
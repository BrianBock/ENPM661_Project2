import numpy as np
import cv2

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


def getSlope(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    return m


def getIntercept(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)

    b=y1-m*x1
    return b




def addToVideo(frame, y, x, status, video_out,show_robot):#addToVideo(output,(y,x),3,video_out,[True, radius])
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
    
    if show_robot[0]==True:
        circle_frame=cv2.circle(frame.copy(), (x,y), int(show_robot[1]), (0,255,0), 1)
        video_out.write(circle_frame)
    
    
    else:
        video_out.write(frame)
        #print("Frame saved")
        # cv2.imshow("Frame",frame)
        # cv2.waitKey(1)
    return frame

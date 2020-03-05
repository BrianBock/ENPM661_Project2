

import numpy as np


def checkCurves(point):
    x_dash=(1-np.square((point[0]-150)/40))
    if x_dash>0:
        y1=100-20*np.sqrt(x_dash)
        y2=100+20*np.sqrt(x_dash)
        if point[0]>=110   and   point[0]<=190   and point[1]>=y1   and point[1]<=y2:
            print()
            return "inside"
    
    
    #for circle
    x_dash=225-np.square(point[0]-225)
    if x_dash>0:
        y1=50-np.sqrt(x_dash)
        y2=50+np.sqrt(x_dash)
        if point[0]>=200  and  point[0]<=250 and   point[1]>=y1   and  point[1]<=y2:
            return "inside"
    return "outside"
def checkPoints(tri,point):
    
    if checkCurves(point)=="inside":
        return "inside"
    
    a=tri[0]
    b=tri[1]
    c=tri[2]
    X=[a[0],b[0],c[0]]
    Y=[a[1],b[1],c[1]]
    X.sort()
    Y.sort()
    print(X)
    print(Y)
    if point[0]<X[0]    or    point[0]>X[2]    or   point[1]<Y[0]    or    point[1]>Y[2]:
        return "outside"
    lists=[[a,b,c],[b,c,a],[a,c,b]]
    flag_counter=0
    for p in lists:
        
        p1=p[0]
        p2=p[1]
        p3=p[2]
        print([p1,p2,p3])
        if p1[0]==p2[0]:
            if p3[0]>p1[0]:
                print( ["x","greater",p1[0],"        ",p1[1],p2[1]])
                q=[p1[1],p2[1]]
                q.sort()
                if point[0]>= p1[0] :#  and    point[1]>= q[0]    and    point[1]<= q[1]:
                    flag_counter=flag_counter+1
                    print("hi")
                    continue
                    
            else:
                print(["x","lesser",p1[0]])
                q=[p1[1],p2[1]]
                q=q.sort()
                if point[0]<=p1[0] :#  and    point[1]>=q[0]    and    point[1]<=q[1]:
                    flag_counter=flag_counter+1
                    print("hi")
                    continue
        else:
            slope=(p2[1]-p1[1])/(p2[0]-p1[0])
            c1=p1[1]-(slope*p1[0])
            sign="lesser"
            if p3[1]>p1[1]    or   p3[1]>p2[1]:
                sign="greater"
            
            
            
            
            print(["y",sign,slope,c1,"     ",p1[0],p2[0]])
            
            if sign=="greater":
                var=(slope*point[0])+c1
                q=[p1[0],p2[0]]
                q.sort()
                print([var,q,point])
                if   point[1]>=var :#  and point[0]>=q[0]    and   point[0]<=q[1]:
                    flag_counter=flag_counter+1
                    print("hi")
                    continue
                
                
                
            else:
                var=(slope*point[0])+c1
                q=[p1[0],p2[0]]
                q.sort()
                print([var,q,point])
                if   point[1]<=var :#or (var<=p1[1]   and   var<=p2[1])  :#  and point[0]>=q[0]    and   point[0]<=q[1]:
                    flag_counter=flag_counter+1
                    print("hi")
                    continue
        
    print(flag_counter)
    
    if flag_counter==3:
        return "inside"
  
    return "outside" 
    #for ellipse
    
#print(checkPoints([[225,160],[225,190],[250,175]],[227,188]))
#print(checkPoints([[0,0],[10,0],[5,6]],[1,6/5+0.1]))

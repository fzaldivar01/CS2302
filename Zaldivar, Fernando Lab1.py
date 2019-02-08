'''
Created by: Fernando Zaldivar
Last Modified: Feb 08, 2019
CS 2302
Proffesor Dr. Olac Fuentes
'''



import numpy as np
import matplotlib.pyplot as plt
import math

'''
This method takes n, the amount of recursion, p, the original center of the squares
and rad, the radius of the square.
The method will compute the center for new squares and their coordinates
'''
def draw_squares(ax,n,p,rad):
    if n>0:
        q = np.array([[-rad*2,-rad*2],[-rad*2,rad*2],[rad*2,rad*2],[rad*2,-rad*2],[-rad*2,-rad*2]])
        q=q+p    
        ax.plot(q[:,0],q[:,1],color='k')
        draw_squares (ax, n-1,q[0],rad//2)
        draw_squares (ax, n-1,q[1],rad//2)
        draw_squares (ax, n-1,q[2],rad//2)
        draw_squares (ax, n-1,q[3],rad//2)

'''
This Method takes a center and the radius to construct a circle
'''
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

'''
Using circle method it will tak n, the amount of recursion, the center of the circle
the radius and w, the factor by which it shrinks/grow
'''
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        center = [center[0]*.5,center[1]]
        draw_circles(ax,n-1,center,radius*w,w)
 
    
''' 
using the circle method it takes n the amount of recursion the center and the radius
then it will compute the center for other circles and draw the circles within the circles
'''
def draw_circles_within(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        up_center = [center[0],(radius)-(center[1]+radius//3)]
        down_center = [center[0],(-radius)-(center[1]-radius//3)]
        right_center = [(center[0]-(radius-radius//3)),center[1]]
        left_center = [(center[0]+(radius-radius//3)),center[1]]
        draw_circles_within(ax,n-1,center,radius//3)
        draw_circles_within(ax,n-1,up_center,radius//3)
        draw_circles_within(ax,n-1,down_center,radius//3)
        draw_circles_within(ax,n-1,right_center,radius//3)
        draw_circles_within(ax,n-1,left_center,radius//3)

'''
this meth takes height of the tree the center which is the original plot
and the change in y and x corrdinate, whi is use to compute the corrdinate for
the next level of recursion
'''

def draw_figure(ax,height, center, xchange, ychange):
    if height>0:
        plot2 = np.array([center[0],center[1]])
        #this plot is good
        
        plot1 = np.array([(center[0]-xchange//2) , center[1]-ychange])
        plot3 = np.array([center[0]+xchange,center[1]-ychange])
        
        
        plots = np.array([[plot1[0],plot1[1]],[plot2[0],plot2[1]],[plot3[0],plot3[1]]])
        #print (plots)
        ax.plot(plots[:,0],plots[:,1],color='k')
        draw_figure(ax,height-1,plot1,5,5)
        draw_figure(ax,height-1,plot3,5,5)
      

#draws the squares  
plt.close("all") 
rad = 1000
p = np.array([[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,rad)
ax.set_aspect(1.0)
ax.axis('off')
plt.figure(1)
fig.savefig('squares.png')


#draws the circles
fig, ax = plt.subplots() 
draw_circles(ax, 5, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
b = plt.figure(2)
b.show()
fig.savefig('circles.png')


#draws the circles with in the circles 
fig, ax = plt.subplots() 
draw_circles_within(ax,4, [100,0], 100)
ax.set_aspect(1.0)
ax.axis('off')
c = plt.figure(3)
c.show()
fig.savefig('circleswithin.png')

 # draws the trees
fig, ax = plt.subplots() 
draw_figure(ax, 5, [10,10],5,5)
ax.set_aspect(1.0)
ax.axis('off')
d = plt.figure(4)
d.show()
fig.savefig('triangles.png')
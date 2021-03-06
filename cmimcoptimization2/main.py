from ast import literal_eval
from random import randrange
import math

task = "1"

# edit to the name of the input file
f = open('circlecovers'+ task+'.txt', 'r')

n = int(f.readline())
points = [f.readline() for _ in range(n)]

m = int(f.readline())
radii = [int(f.readline()) for _ in range(m)]

# array of x coordinates
xcoords = []
#array of y coordinates
ycoords = []  

for point in range(len(points)):
  a,b = (int(i) for i in points[point].split())
  #adds all x coordinates to array
  xcoords.append(int(a))
  # adds all y coordinates to array
  ycoords.append(int(b))

#smallest x coordinate
xmin = sorted(xcoords)[0]
#biggest x coordinate
xmax = sorted(xcoords)[len(xcoords)-1]
#smallest y coordinate
ymin = sorted(ycoords)[0]
# largest y coordinate
ymax = sorted(ycoords)[len(ycoords)-1]

centers = []
radiiSorted = sorted(radii, reverse= True)
#method to check if point is in circle
def inCircle(radius, pointX, pointY, centerX, centerY):
  distance = math.sqrt((pointX-centerX)**2 + (pointY - centerY)**2)
  #print(distance, radius)
  if (distance <= radius):
    return True

#method determines whether you have 2 circles that are overlapping. parameters are radius, x, and y for the 2 circles that you are comparing. formula states if distance between centers is less than radii comob
def isOverlapping(r1,x1,y1):
  if (r != 0): # FIXME: why is this here?
    for circle in establishedCircles:
      if((math.sqrt((x1-circle[1])**2 + (y1-circle[2])**2)) < r1+circle[0]):
        return True
  return False

mostDenseX = 0
mostDenseY = 0
#iterates through all points <later change to radii length
establishedCircles = []
for r in range(len(radiiSorted)):
  print(str(len(radiiSorted)-r) + " iterations remaining")
  #note: the program speeds up as r increases. idk what you did there but good work
  maxPoints = 0
  for x in range(xmin,xmax):
    for y in range(ymin,ymax):
      #print("r:",r,"x:",x,"y:",y)
      pointsInCircle = 0
      #loop through all points in the circle
      if not isOverlapping(radiiSorted[r],x,y):
        for p in range(len(points)):
          pX,pY = (int(j) for j in points[p].split())
          if(inCircle(radiiSorted[r], pX, pY, x, y)):
            pointsInCircle += 1
            if pointsInCircle > maxPoints:
              maxPoints = pointsInCircle
              mostDenseX = x
              mostDenseY = y
          #established circles is a list of circles 
          #each circle is a list of the form [radius, x, y]
  circle = [radiiSorted[r],mostDenseX,mostDenseY]
  print(circle)
  if len(establishedCircles) > r:
    establishedCircles[r] = circle
  else:
    establishedCircles.append(circle)
          # if((len(establishedCircles)) >= ((r*3)+2)):
          #   establishedCircles[r*3] = radiiSorted[r]
          #   establishedCircles[(r*3)+1] = mostDenseX
          #   establishedCircles[(r*3)+2] = mostDenseY
          # else:
          #   establishedCircles.extend((radiiSorted[r],mostDenseX,mostDenseY))

for circle in establishedCircles:
  print("R:",circle[0],"x:",circle[1],"y:",circle[2])

out = open('output'+task+'.txt', 'w')

for radius in radii:
  for i in range(len(establishedCircles)):
    if establishedCircles[i][0] == radius:
      circle = establishedCircles[i]
      out.write(str(circle[1])+".0 " + str(circle[2])+".0\n")
      del establishedCircles[i]
      break
out.close()

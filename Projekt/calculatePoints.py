import numpy as np
import math as m

def calculatePointsWithinAngle(ammount, centerX, centerY, radius, startTime, endTime, startAngle, endAngle):

    # calculate increments and create array
    angleIncrement = (endAngle - startAngle) / (ammount + 1)
    timeIncrement = (endTime - startTime) / (ammount + 1)
    points = np.zeros((ammount + 2, 4), dtype=float)

    # calculate each point
    for i in range(ammount + 2):
        currentAngle = startAngle + angleIncrement * i
        currentTime = startTime + timeIncrement * i
        
        # x value
        points[i][0] = centerX + radius * m.cos(m.radians(currentAngle))

        # y value
        points[i][1] = centerY + radius * m.sin(m.radians(currentAngle))
        
        # rotation (depending on clockwise/counterclockwise)
        if(angleIncrement > 0):
            points[i][2] = m.radians(currentAngle + 90)
        else:
            points[i][2] = m.radians(currentAngle - 90)

        # time
        points[i][3] = currentTime

    return points

def printVRMLfromPoints(points):

    print("\npositions:")
    print("key [")
    for point in points:
        print("{:.5f}".format(point[3]))
    print("]")
    print("keyValue [")
    for point in points:
        print("{:.2f} {:.2f} {:.2f}".format(point[0], 0.0, point[1]))
    print("]")

    print("\norientations:")
    print("key [")
    for point in points:
        print("{:.5f}".format(point[3]))
    print("]")
    print("keyValue [")
    for point in points:
        print("0 1 0 {:.2f}".format(point[2]))
    print("]")

#center = (-25,47) # KURVE 1
#center = (-25,141) # KURVE 2
#center = (-25,235) # KURVE 3 (90 grad)
#center = (-48.5, 235) # KURVE 4 (klein, 90 grad)
center = (-48.5, 282) # KURVE 5 (klein, 90 grad, Uhrzeiger)
#radius = 47 # KURVE 1 2 3
radius = 23.5 # KURVE 4 5
ammount = 10
#startTime = 0.02 # KURVE 1
#endTime = 0.08 # KURVE 1
#startTime = 0.08 #KURVE 2
#endTime = 0.14 # KURVE 2
#startTime = 0.14 # KURVE 3
#endTime = 0.18 # KURVE 3
#startTime = 0.18 # KURVE 4
#endTime = 0.23 # KURVE 4
startTime = 0.23 # KURVE 5 (klein, 90 grad, Uhrzeiger)
endTime = 0.30 # KURVE 5 (klein, 90 grad, Uhrzeiger)
#startAngle = 90 # KURVE 1
#endAngle = 270 # KURVE 1
#startAngle = 90 # KURVE 2
#endAngle = -90 # KURVE 2
#startAngle = -180 # KURVE 3
#endAngle = -270 # KURVE 3
#startAngle = -180 # KURVE 4
#endAngle = -270 # KURVE 4
startAngle = 0 # KURVE 5
endAngle = -90 # KURVE 5

points = calculatePointsWithinAngle(ammount, center[0], center[1], radius, startTime, endTime, startAngle, endAngle)
printVRMLfromPoints(points)
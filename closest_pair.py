#!/usr/bin/python
# Given a set of points, find closest Euclidean pair

oneD_points = [4,9,21,1,200,22]
twoD_points = [(2,1),(2,2),(3,1),(5,2),(1,0)]

def closest_1D(points):
    if len(points) == 1:
        return points[0]
    sorted_points = sorted(points)
    shortest_distance = points[len(points)-1]
    shortest_pair = []
    index = 1
    for point in points[:-1]:
        if points[index] - point < shortest_distance:
            shortest_distance = points[index] - point
            closest_pair = [point, points[index]]
        index += 1

    return closest_pair
   
def sort_coordinates(points):
    # Sort ascending by x
    cmp_x = lambda left, right: cmp(left[0], right[0])
    x_sort = sorted(points,cmp_x)
    # Sort ascending by y
    cmp_y = lambda left, right: cmp(left[1], right[1])
    y_sort = sorted(points,cmp_y)
    
    return x_sort, y_sort

def closest_pair(Px,Py):
    n = len(Px)
    # Left half
    Qx = Px[: n / 2]
    Qy = Py[: n / 2]
    # Right half
    Rx = Px[n / 2:]
    Ry = Py[n / 2:]
    # Recurse
    P_1,Q_1 = closest_pair(Qx,Qy)
    a = distance(P_1,Q_1)
    P_2,Q_2 = closest_pair(Rx,Ry)
    b = distance(P_2,Q_2)
    delta = min(a,b)
    P_3,Q_3 = closest_split_pair(Px,Py, delta)
    c = distance(P_3,Q_3)
    return {
        a: (P_1,Q_1),
        b: (P_2,Q_2),
        c: (P_3,Q_3)
        }.get(min(a,b,c))

def closest_split_pair(Px,Py,delta):
    mid = len(Px) / 2
    x_bar = max([x for x,y in Px[:mid]])
    Sy = [ (x,y) for x,y in Py if x_bar - delta < x < x_bar + delta]
    best_pair = None
    best = delta
    for i in range(1,len(Sy)-1):
        for j in range(1,min(7,len(Sy)-1):
            p, q = Sy[i],Sy[j]
            if distance(p,q) < best:
                best_pair = [p,q], best = distance(p,q)
    return best_pair[0],best_pair[1]
                       
def distance(point_a,point_b):
    return math.sqrt((point_b[0]-point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)
    
#print closest_1D(oneD_points)

#print closest_2D(twoD_points)

#!/usr/bin/python
# Given a set of points, find closest Euclidean pair

oneD_points = [4,9,21,1,200,22]

def closest_1D(points):
    if len(points) == 1:
        return points[0]
    points.sort()
    shortest_distance = points[len(points)-1]
    shortest_pair = []
    index = 1
    for point in points[:-1]:
        if points[index] - point < shortest_distance:
            shortest_distance = points[index] - point
            closest_pair = [point, points[index]]
        index += 1

    return closest_pair
   

print closest_1D(oneD_points)

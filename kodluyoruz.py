import math

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        pointA = points[i]
        pointB = points[j]
        distance = euclideanDistance(pointA, pointB)
        distances.append(((pointA, pointB), distance))

for pair, dist in distances:
    pointA, pointB = pair
    print(f"{pointA} ve {pointB} noktaları arasındaki Öklid mesafesi: {dist}")
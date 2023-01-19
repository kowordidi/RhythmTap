# 4/4 time, with one bar, spanning 4 seconds
alistOfPoints = [0.8, 2, 3.1]
aGrid = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]


def snap(points, grid):
    snapped = []

    for p in points:
        snapped.append(closest_grid_line(p, grid))

    return snapped


def closest_grid_line(p, grid):
    shortestDistance = 100
    positionOfClosestGridLine = None
    for g in range(len(grid)):

        if distance(p, g) < shortestDistance:
            shortestDistance = distance(p, g)
            positionOfClosestGridLine = g

    return positionOfClosestGridLine


def distance(p, g):
    return abs(p - g)


print("expected result: [1, 2, 3]")
print("result:", snap(alistOfPoints, aGrid))

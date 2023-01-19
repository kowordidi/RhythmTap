def snap(points, grid):
    snapped = []

    for p in points:
        snapped.append(closest_grid_line(p, grid))

    return snapped


def distance(p, g):
    return abs(p - g)


def closest_grid_line(p, grid):
    shortestDistance = 100
    positionOfClosestGridLine = None
    for g in range(len(grid)):

        if distance(p, grid[g]) < shortestDistance:
            shortestDistance = distance(p, g)
            positionOfClosestGridLine = g

    return positionOfClosestGridLine

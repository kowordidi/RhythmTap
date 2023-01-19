def snap(points, grid):
    snapped = []

    for p in points:
        snapped.append(closest_grid_line(p, grid))

    return snapped


def distance(p, g):
    return abs(p - g)


def closest_grid_line(p, grid):
    shortest_distance = 100
    idx_of_closest_grid_line = None
    for grid_idx in range(len(grid)):
        dist = distance(p, grid[grid_idx])

        if dist < shortest_distance:
            shortest_distance = dist
            idx_of_closest_grid_line = grid_idx

    return idx_of_closest_grid_line

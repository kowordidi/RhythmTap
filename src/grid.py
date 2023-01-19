def snap(points, grid):
    snapped = []

    for p in points:
        snapped.append(idx_of_closest_grid_line(p, grid))

    return snapped


def distance(p, g):
    return abs(p - g)


def idx_of_closest_grid_line(p, grid):
    shortest_distance = None
    ret = None
    for grid_idx in range(len(grid)):
        dist = distance(p, grid[grid_idx])

        if shortest_distance is None or dist < shortest_distance:
            shortest_distance = dist
            ret = grid_idx

    return ret

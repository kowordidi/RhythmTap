def snap(points, grid):
    snapped = []

    for p in points:
        snapped.append(grid[idx_of_closest_grid_line(p, grid)])

    return snapped


def distance(p, g):
    return abs(p - g)


def idx_of_closest_grid_line(p, grid):
    shortest_dist = None
    ret = None
    for grid_idx in range(len(grid)):
        dist = distance(p, grid[grid_idx])

        def is_shorter(shortest_so_far, curr):
            return shortest_so_far is None or curr < shortest_so_far

        if is_shorter(shortest_dist, dist):
            shortest_dist = dist
            ret = grid_idx

    return ret

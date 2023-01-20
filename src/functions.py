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


def generate_eight_grid(number_of_beats):
    grid = []
    time_unit = 0
    for i in range(number_of_beats * 2):
        grid.append(time_unit)
        time_unit += 1 / 2
    return grid


def generate_triplet_grid(number_of_beats):
    grid = []
    time_unit = 0
    for i in range(number_of_beats * 3):
        grid.append(time_unit)
        time_unit += 1 / 3
    return grid


def generate_grid(grid_type, number_of_beats):
    if grid_type == 'triplet':
        return generate_triplet_grid(number_of_beats)
    else:
        return generate_eight_grid(number_of_beats)

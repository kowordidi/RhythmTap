from src.man_file import read_file

CONST_THRESHOLD = 0.08
CONST_NUMBER_OF_BEATS = 4


# ---------------------------------------

def snap(points):
    snapped = []
    grid = generate_grid(CONST_NUMBER_OF_BEATS)
    for p in points:
        next_snapped = grid[idx_of_closest_grid_line(p, grid)]
        snapped.append(next_snapped)
    return snapped


# ---------------------------------------
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


# ---------------------------------------
def generate_grid(number_of_beats):
    def part_of_grid(even_notes_per_beat):
        grid = []
        time_unit = 0
        for i in range(number_of_beats * even_notes_per_beat):
            grid.append(time_unit)
            time_unit += 1 / even_notes_per_beat
        for idx in range(len(grid)):
            grid[idx] = round(grid[idx], 4)
        return grid

    thirtysecond_grid = part_of_grid(8)
    triplet_grid = part_of_grid(3)

    full_grid = sorted(set(thirtysecond_grid + triplet_grid))

    return full_grid


# ---------------------------------------
def read_inputs():
    string_input = read_file('input.txt')
    string_input_array = string_input.split()
    float_input_array = []
    for i in range(len(string_input_array)):
        float_input_array.append(float(string_input_array[i]))
    return float_input_array

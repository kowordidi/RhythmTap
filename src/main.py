from src.functions import read_inputs, snap, generate_grid
from src.man_file import read_file


def my_main():
    list_of_points = read_inputs()
    print(list_of_points)
    grid = generate_grid(4, 1)
    print(grid)
    res = snap(list_of_points, grid)

    print(res)

# ---------------------------------------
if __name__ == "__main__":
    my_main()

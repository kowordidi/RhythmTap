from src.functions import read_inputs, snap, generate_grid
from src.man_file import read_file


def my_main():
    list_of_points = read_inputs()
    print(f"this is the original input: {list_of_points}")
    grid = generate_grid(4, 1)
    print(f"this is the grid input: {grid}")
    res = snap(list_of_points, grid)
    print(f"this is the result: {res}")


# ---------------------------------------
if __name__ == "__main__":
    my_main()

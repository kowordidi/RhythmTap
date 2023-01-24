from src.snap_functions import read_inputs, snap, generate_grid, CONST_NUMBER_OF_BEATS
from src.man_file import read_file


def my_main():
    points = read_inputs()
    res = snap(points)
    grid = generate_grid(CONST_NUMBER_OF_BEATS)
    print(f'this is the grid used {grid}')
    print(f'this is the input received: {points}')
    print('this is the expected result: [0, 0.3333, 0.6667, 1.0, 1.5, 2.0, 3.0]')
    print(f'this is the result:{res}')


# ---------------------------------------
if __name__ == "__main__":
    my_main()

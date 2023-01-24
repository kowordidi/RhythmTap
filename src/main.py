from src.functions import read_inputs, snap, generate_grid
from src.man_file import read_file


def my_main():
    points = read_inputs()
    res = snap(points)
    print(f'this is the input received: {points}')
    print('this is the expected result: [0, 0.3333, 0.6667, 1.0, 1.5, 2.0, 3.0]')
    print(f'this is the result:{res}')


# ---------------------------------------
if __name__ == "__main__":
    my_main()

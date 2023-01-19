from src.grid import snap



def my_main():
    # 4/4 time, with one bar, spanning 4 seconds
    alistOfPoints = [0.8, 2, 3.1]
    aGrid = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]


    print("expected result: [1, 2, 3]")
    print("result:", snap(alistOfPoints, aGrid))



# ---------------------------------------
if __name__ == "__main__":
    my_main()
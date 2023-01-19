from src.grid import distance, closest_grid_line


def test_distance():
    assert distance(4, 5) == 1
    assert distance(5, 4) == 1


def test_closest_grid_line():
    aGrid = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    assert closest_grid_line(0.3, aGrid) == 1
    assert closest_grid_line(0, aGrid) == 0
    assert closest_grid_line(4.9, aGrid) == 9


# ---------------------------------------
if __name__ == "__main__":
    test_distance()


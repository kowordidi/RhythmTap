from src.grid import distance, idx_of_closest_grid_line, snap


# ---------------------------------------
def test_distance():
    assert distance(4, 5) == 1
    assert distance(5, 4) == 1


# ---------------------------------------
def test_closest_grid_line():
    aGrid = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    assert idx_of_closest_grid_line(0.3, aGrid) == 1
    assert idx_of_closest_grid_line(0, aGrid) == 0
    assert idx_of_closest_grid_line(4.9, aGrid) == 9


# ---------------------------------------
def test_snap():
    assert snap([0.3, 4.1, 5], [0, 0.5, 4, 5]) == [0.5, 4, 5]


# ---------------------------------------
if __name__ == "__main__":
    test_distance()
    test_closest_grid_line()
    test_snap()

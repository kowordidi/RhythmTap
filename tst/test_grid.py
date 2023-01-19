from src.grid import distance

def test_distance():
    assert (distance(4, 5) == 1)

    got_4_5 = distance(4, 5)
    expect_4_5 = 1
    compare = (got_4_5 == expect_4_5 )
    assert(compare)

    got_3_5 = distance(3, 5)
    expect_3_5 = 2
    assert (got_4_5 == expect_4_5 )

    # assert(3==4)

# ---------------------------------------
if __name__ == "__main__":
    test_distance()


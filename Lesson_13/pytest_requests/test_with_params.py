import pytest

test_data = [
    (2, 5, 10),
    (0, 4, 0),
    (-1, 4, -4),
    (50, 60, 30000),
    (-2, -4, 8)
]

@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_multiple_and_result(num_1, num_2, result):
    assert num_1 * num_2 == result

# def test_multiple_2():
#     assert 0 * 4 == 0
#
# def test_multiple_3():
#     assert -1 * 4 == -4
#
# def test_multiple_4():
#     assert -2 * -4 == 8
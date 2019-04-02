"""Daily Coding Problem #85"""


def math_filer(x, y, b):
    """
    Mathematical equivalent of x if b == 1 else y.

    Except, this function is done with math only,
    no logic/if statements.

    :param x: 32-bit integer to return if b is 1
    :param y: 32-bit integer to return if b is 0
    :param b: 1 or 0 (can be assumed to be so)
    :return: x if b is 1 else y
    """
    return x*b + y*(1 - b)


def test_math_filter():
    """Present two test cases for math_filter."""
    case_1 = math_filer(87, 21, 1)
    case_2 = math_filer(37,1, 0)
    assert case_1 == 87, "Failed x test case: returned %f expected 87" % case_1
    assert case_2 == 1, "Failed x test case: returned %f expected 1" % case_2


if __name__ == '__main__':
    test_math_filter()
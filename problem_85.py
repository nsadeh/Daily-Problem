"""Daily Coding Problem #85"""

from hypothesis import given
from hypothesis.strategies import integers, booleans


def math_filter(x, y, b):
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


@given(x=integers(), y=integers(), b=booleans())
def test_math_filter(x, y, b):
    """Present two test cases for math_filter."""
    assert math_filter(x, y, int(b)) == (x if b else y), \
        "Failed test case: \n x: %f \n y: %f \n b: %f" % (x, y, int(b))


if __name__ == '__main__':
    test_math_filter()

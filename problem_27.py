"""
daily code problem 27.

Problem: given a string consisting of round,
curly, or square brackets ("(", "{", "["),
output whether the string is well-formed (i.e.,
all openining brackets are closed and a bracket
open before another is closed after)

This question was asked by Facebook.
"""


import queue


OPPOSITES = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def well_formed(in_str):
    """
    Test whether input has well-formed bracket algebra.

    Input can contain only round, curly, or square brackets.
    Function tests for whether each opening closes and
    whether sentenced close in correct order.
    
    This problem is solved by using a LIFO queue. 
    If the bracket is an opening action (left),
    then put to queue. If closing, it is only allowed to 
    close a bracket of its type, or otherwise the string
    is now well formed. Additionally, if the string is well-formed
    then the queue must be empty at the end. This solution
    is O(N).
    
    Example 1: input "([])" (well-formed)
    1. "(" put: queue("(")
    2. "[" put: queue("(", "[")
    3. "]" get: queue("(")
    4. ")" get: queue()
    Queue is empty: return True
    
    Example 2: input "((()" (not well-formed)
    1. "(" put: queue("(")
    2. "(" put: queue("(", "(")
    1. "(" put: queue("(", "(", "(")
    4. ")" get: queue("(", "(")
    Queue in not empty: return False

    :param in_str: a string consisting of brackets (str)
    :return: True if in_str is well-formed, else false
    """
    bracket_q = queue.LifoQueue(maxsize=-1)
    for bracket in in_str:
        if bracket in ['(', '[', '{']:
            bracket_q.put(bracket)
        else:
            if OPPOSITES[bracket_q.get()] == bracket:
                continue
            else:
                return False
    return bracket_q.empty()


def test_pos():
    """assert positive test case."""
    assert well_formed("([])[]({})") is True, "True test case returned False"


def test_false_ordering():
    """assert negative test case: bad ordering."""
    assert well_formed("([)]") is False, "Bad ordering returned True"


def test_false_numbering():
    """assert negative test case: mismatched number."""
    assert well_formed("((()") is False, "mismatched bracket numbers returned True"


if __name__ == '__main__':
    test_pos()
    test_false_ordering()
    test_false_numbering()

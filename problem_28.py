"""Solution to problem 28"""


def justify(words, k):
    """
    Justify a list of words.

    A list of words as string with no spaces
    should be turned into a list of short collections
    of words all with equal length k, with spaces
    interspersed equally starting from the left.

    See test for example.

    :param words: a list of str words with no spaces
    :param k: the length of the line as an int
    :return: list of strings of length k of justified lines
    """
    # TODO
    justified = []
    current_word = ""
    for word in words:
        current_word = current_word.strip()
        if len(current_word) + len(word) < k:
            current_word = "{} {}".format(current_word, word)
        else:
            justified.append(interspace(current_word, k=k))
            current_word = word
    justified.append(interspace(current_word, k=16))
    return justified


def interspace(word, k):
    """
    Inter-space word until len(word) == k.

    Inter-spacing is done from the left to
    right striving for an equal number of spaces
    between words. No space is added in beginning or end.

    Example:
    > case = "fox jumps over"
    > interspace(case, k=16)
    "fox  jumps  over"  # two spaces between "fox" and "jumps" and "jumps" and "over"

    :param word: str containing words separated by single spaces
    :param k: int length of final line
    :return: str words in word of length k with inter-spacing
    """
    separated = word.split(" ")
    length = len(word)
    index = 0
    while length < k:
        separated[index] = separated[index] + " "
        length += 1
        index = (index + 1) % (len(separated) - 1)
    return " ".join(separated)


def test_justify():
    """test string justification."""
    dog_case = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    dog_output = ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]
    assert justify(dog_case, k=16) == dog_output, "Failed to justify sentence"


if __name__ == '__main__':
    test_justify()

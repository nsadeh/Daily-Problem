"""Daily Coding Problem #66."""

import random

random.seed(42)
p = random.random()

def biased_toss():
    """
    Toss a coin with an unknown bias.

    Generates a random number p as the probability
    then a toss. If toss < p, return heads, else tails

    :return: heads (1) or tails (0)
    """
    global p
    toss = random.random()
    return int(toss < p)


def unbiased_toss():
    """
    Toss an unbiased coin using a biased toss.

    Relies on the fact that p(TH) = p(HT). Toss the coin twice,
    if HH (p = p^2) or TT (p=p(1-p)), toss again. Otherwise, return heads if HT
    or tails if TH.

    Can theoretically go into a long loop if always tosses homogeneous pair!

    :return: heads (1) or tails (0)
    """
    toss1 = biased_toss()
    toss2 = biased_toss()
    while toss1 == toss2:
        toss1 = biased_toss()
        toss2 = biased_toss()
    return toss1


def test_unbiased_toss(N):
    """
    Test that unbiased toss is unbiased

    N unbiased coin tosses should have a mean of 1/2.

    :return: A report on experiment statistics
    """
    experiment = [float(unbiased_toss()) for i in range(N)]
    mean = sum(experiment)/N
    variance = sum([(exp - mean)**2 for exp in experiment]) / N
    print("Mean: %f" % mean)
    print("Variance: %f" % variance)
    print("Biased p: %f" % p)


if __name__ == '__main__':
    test_unbiased_toss(1000)

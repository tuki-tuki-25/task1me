import numpy as np


def prod_non_zero_diag(x):
    return np.prod(np.diag(x)[np.diag(x) != 0])


def are_multisets_equal(x, y):
    return np.array_equal(x, y)


def max_after_zero(x):
    return np.max(x[1:][np.nonzero(x[:-1] == 0)])


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass

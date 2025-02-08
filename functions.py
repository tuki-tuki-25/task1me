def prod_non_zero_diag(x):
    res = 1
    k = min(len(x), len(x[0]))
    for i in range(k):
        if x[i][i] != 0:
            res *= x[i][i]
    return res


def are_multisets_equal(x, y):
    flag = True
    for k in x:
        if x.count(k) != y.count(k):
            flag = False
    return flag


def max_after_zero(x):
    res = 0
    for i in range(len(x)):
       if x[i] == 0 and i < len(x)-1:
          res = max(x[i+1], res)
    return res


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass

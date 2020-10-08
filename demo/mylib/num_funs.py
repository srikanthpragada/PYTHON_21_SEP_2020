def iseven(n):
    """
    iseven(number)
    Determines whether the given number is even

    :param n: number to check
    :return:  True for even, False for odd
    """
    return n % 2 == 0


def ispositive(n):
    """
        Determines whether the given number is positive
        :param n: number to check
        :return:  True for positive, False otherwise
    """
    return n > 0

if __name__ == '__main__':  # Module is run as script
    print("In num_funs module!")
else:
    print(__name__, ' is being imported!')
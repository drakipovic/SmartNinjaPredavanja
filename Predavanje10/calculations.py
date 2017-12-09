def numbers_sum(num_1, num_2):
    s = num_1 + num_2
    s = add_factor(s, 2)

    return s


def add_factor(num, factor=3):
    return num + factor


if __name__ == '__main__':
    print numbers_sum(4, 5)
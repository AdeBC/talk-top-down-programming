import argparse
import random


def main():
    args = parse_args()
    x = random.randint(1, 1000)
    y_expected = args.y
    y_current = E_step(x)
    diff = y_expected - y_current
    i = 0
    while abs(diff) >= args.limit:
        diff = y_expected - y_current
        x = x - M_step(diff, x, args.step_size)
        y_current = E_step(x)
        i += 1
    print('The squared root is {}.'.format(x))


def E_step(x):
    return x * x


def M_step(diff, x, step_size):
    if diff >= 0:
        return -2 * x * step_size
    else:
        return 2 * x * step_size


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('y', type=int)
    parser.add_argument('-l', '--limit', type=float, default=0.01)
    parser.add_argument('-s', '--step-size', type=float, default=0.0001)
    return parser.parse_args()
    

if __name__ == '__main__':
    main()
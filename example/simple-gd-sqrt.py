import argparse
import random


def main():
    args = parse_args()
    x_init = random.randint(1, 1000)
    x = solve(x=x_init, y_expected=args.y, limit=args.limit, step_size=args.step_size)
    print('The squared root is {}.'.format(x))


def solve(x, y_expected, limit, step_size):
    y_current = calculate_Y(x)
    diff = y_expected - y_current
    i = 0
    while abs(diff) >= limit:
        diff = y_expected - y_current
        x = update_X(diff, x, step_size)
        y_current = calculate_Y(x)
        i += 1
    return x


def calculate_Y(x):
    return x * x


def update_X(diff, x, step_size):
    if diff >= 0:
        return x - (-2 * x * step_size)
    else:
        return x - (2 * x * step_size)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('y', type=int)
    parser.add_argument('-l', '--limit', type=float, default=0.01)
    parser.add_argument('-s', '--step-size', type=float, default=0.0001)
    return parser.parse_args()
    

if __name__ == '__main__':
    main()
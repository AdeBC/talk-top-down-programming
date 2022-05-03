import argparse
import random


def main():
    args = parse_args()
    x = solve(y_expected=args.y, limit=args.limit, step_size=args.step_size, steps=args.steps)
    print('The squared root is {:.4f}.'.format(x))


def solve(y_expected, limit, step_size, steps, x=None):
    if not x:
        x = random.randint(1, 1000)
    y_current = calculate_Y(x)
    diff = y_expected - y_current
    i = 0
    while abs(diff) >= limit and i < steps:
        x = update_X(y_expected, y_current, x, step_size)
        y_current = calculate_Y(x)
        diff = y_expected - y_current
        # print('current x: {}, abs(diff): {}'.format(x, abs(diff)))
        i += 1
    return x


def calculate_Y(x):
    return x * x


def update_X(y_expected, y_current, x, step_size):
    return x - (-2 * x * step_size)
    # diff = y_expected - y_current
    # if diff >= 0:
    #     return x - (-2 * x * step_size)
    # else:
    #     return x - (2 * x * step_size)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('y', type=int)
    parser.add_argument('-l', '--limit', type=float, default=0.01)
    parser.add_argument('-s', '--step-size', type=float, default=0.0001)
    parser.add_argument('-n', '--steps', type=int, default=10**6)
    return parser.parse_args()


if __name__ == '__main__':
    main()
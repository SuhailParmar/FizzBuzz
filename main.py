from lib.fizz_buzz import FizzBuzz
from sys import argv
from sys import stdin


def parse_stdin():
    """ Convert stdin to integer """
    input = stdin.readline()
    arr = input.split()
    if len(arr) < 1:
        raise ValueError("Expected at least 1 arg: max_range")

    for i, string in enumerate(arr):
        try:
            arr[i] = int(string)
        except ValueError:
            raise ValueError("Arguments must be integers")

    return arr


def main(max_range, min_range=1):
    fb = FizzBuzz()
    fb.run_fizz_buzz(max_range, min_range)


if __name__ == "__main__":
    print('Input the max_number you want to FizzBuzz:')
    int_values = parse_stdin()
    max_range = int_values[0]
    min_range = 1
    if len(int_values) > 1:
        min_range = int_values[1]

    main(max_range, min_range)

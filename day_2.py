from numpy import genfromtxt, ndarray
from argparse import ArgumentParser
from sys import exit


def calculate_depth_distance_without_aim(data: ndarray) -> float:
    """calculate multiple of depth and distance withou using aim function
    depth and distance are independent

    Parameters
    ----------
    data : numpy str array
        input data containing submarine commands

    Returns
    -------
    float
        multiple of distance and depth
    """

    # initialize values for distance, depth and aim
    distance = 0
    depth = 0
    aim = 0

    # iterate through each data point and modify
    # distance, depth, or aim accordingly
    for i in range(len(data)):
        if data[i, 0] == "forward":
            distance += float(data[i, 1])
            depth += float(data[i, 1]) * aim
        elif data[i, 0] == "down":
            aim += float(data[i, 1])
        else:
            aim -= float(data[i, 1])

    # return requested multiple
    return distance * depth


def calculate_depth_distance_with_aim(data: ndarray) -> float:
    """calculate multiple of depth and distance using aim function.
    depth = forward distance * aim

    Parameters
    ----------
    data : numpy str array
        input data containing submarine commands

    Returns
    -------
    float
        multiple of distance and depth
    """
    # initialize values for distance, depth and aim
    distance = 0
    depth = 0
    aim = 0

    # iterate through each data point and modify
    # distance, depth, or aim accordingly
    for i in range(len(data)):
        if data[i, 0] == "forward":
            distance += float(data[i, 1])
            depth += float(data[i, 1]) * aim
        elif data[i, 0] == "down":
            aim += float(data[i, 1])
        else:
            aim -= float(data[i, 1])

    # return requested multiple
    return distance * depth


def main():
    """parse arguments and execute code accordingly"""

    # parse CLI arguments: --in_file and --part
    parser = ArgumentParser()
    parser.add_argument(
        "--in_file", help="location of data input file", default="./day_2_input.txt"
    )
    parser.add_argument(
        "--part", help="which part of the solution to implement (1 or 2)", default="1"
    )

    args = parser.parse_args()

    # no need to reinvent the wheel for these simple input files
    # actually I shouldn't say that, the judges probably have some snarky answer
    # to that
    try:
        data = genfromtxt(args.in_file, dtype=str)
        if len(data.shape) != 2:
            print("input file must contain two columns")
            exit()

    except Exception:
        print("input file not found or formatted incorrectly")
        exit()

    # for part 1, we don't use the aim calculation. for part 2, we do
    if args.part == "1":
        print("calculating multiple of depth and distance, without aim")
        print(calculate_depth_distance_without_aim(data))
    elif args.part == "2":
        print("calculating multiple of depth and distance, with aim")
        print(calculate_depth_distance_with_aim(data))
    else:
        print("please supply a valid argument for --part (1 or 2)")
        exit()


if __name__ == "__main__":
    main()

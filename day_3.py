from numpy import genfromtxt, ndarray, bincount, argmax
from argparse import ArgumentParser
from sys import exit
from typing import Tuple


def process_input(in_file: str) -> ndarray:
    """Process input file into numpy array
    Every bit gets its own column

    Parameters
    ----------
    str : input_file
        path to input file

    Returns
    -------
    ndarray
        2-d array representing binary numbers
    """
    data = genfromtxt(in_file, delimiter=1, dtype=int)
    return data


def calculate_oxygen_co2(data: ndarray) -> int:
    """calculate multiple of oxygen and co2 rating

    Parameters
    ----------
    data : numpy str array
        input data containing binary numbers

    Returns
    -------
    float
        multiple of co2 and oxygen rating
    """
    # yes yes dock me points for not being space efficient
    # it's a friday afternoon
    oxygen_candidates = data.copy()
    co2_candidates = data.copy()

    # use bincount and argmax to determine most common element
    # in each column
    # I would just build off the part 1 solution,
    # but now we need account for the possibility of a tie

    # also, screw it, two for-loops so I don't have to track when
    # co2 finishes and when oxygen finishes in the same loop
    for i in range(data.shape[1]):
        # if we only have one candidate left, take it
        if oxygen_candidates.shape[0] == 1:
            oxygen_rating = oxygen_candidates[0]
            break

        # grab the bin counts for 0 and 1
        common_value = bincount(oxygen_candidates[:, i])

        # if they match, oxygen goes off of 1
        if common_value[0] == common_value[1]:
            potential_oxygen_candidates = oxygen_candidates[
                oxygen_candidates[:, i] == 1
            ]

        # otherwise, oxygen goes off the most common value
        else:
            potential_oxygen_candidates = oxygen_candidates[
                oxygen_candidates[:, i] == argmax(common_value)
            ]

        # check to make sure we didn't lose all of our candidates
        if potential_oxygen_candidates.size > 0:
            oxygen_candidates = potential_oxygen_candidates

        # check to make sure we're not at the end of the bits
        # if we are, then we have multiple identical candidates,
        # so take the first one
        if i == data.shape[1] - 1:
            oxygen_rating = oxygen_candidates[0]

    # repeat the above loop for co2
    # tiebreaks are done with 0 instead of 1
    # and we use the least common element instead of the most common
    for i in range(data.shape[1]):

        if co2_candidates.shape[0] == 1:
            co2_rating = co2_candidates[0]
            break

        common_value = bincount(co2_candidates[:, i])
        if common_value[0] == common_value[1]:
            potential_co2_candidates = co2_candidates[co2_candidates[:, i] == 0]
        else:
            potential_co2_candidates = co2_candidates[
                co2_candidates[:, i] == 1 - argmax(common_value)
            ]

        if potential_co2_candidates.size > 0:
            co2_candidates = potential_co2_candidates

        if i == data.shape[1] - 1:
            co2_rating = co2_candidates[0]

    # convert binary list representation to integer by joining each element in a str
    # using list comprehension
    oxygen_rating_str = "".join(
        [str(oxygen_rating[i]) for i in range(len(oxygen_rating))]
    )
    oxygen_rating_int = int(oxygen_rating_str, 2)

    co2_rating_str = "".join([str(co2_rating[i]) for i in range(len(co2_rating))])
    co2_rating_int = int(co2_rating_str, 2)
    return oxygen_rating_int * co2_rating_int


def calculate_bits(data: ndarray) -> Tuple:
    """calculate multiple of gamma rate and its complement, epsilon rate

    Parameters
    ----------
    data : numpy str array
        input data containing binary numbers

    Returns
    -------
    float
        multiple of gamma and epsilon
    """
    # inversion dict for calculating epsilon
    inv_dict = {"0": "1", "1": "0"}
    gamma_string = ""

    # use bincount and argmax to determine most common element
    # in each column
    for i in range(data.shape[1]):
        gamma_string += str(bincount(data[:, i]).argmax())

    epsilon_string = "".join([inv_dict[i] for i in gamma_string])

    # convert binary string representation to integer
    converted_gamma = int(gamma_string, 2)
    converted_epsilon = int(epsilon_string, 2)

    return converted_gamma * converted_epsilon


def main():
    """parse arguments and execute code accordingly"""

    # parse CLI arguments: --in_file and --part
    parser = ArgumentParser()
    parser.add_argument(
        "--in_file", help="location of data input file", default="./day_3_input.txt"
    )
    parser.add_argument(
        "--part", help="which part of the solution to implement (1 or 2)", default="1"
    )

    args = parser.parse_args()

    # stubbing out a processing function, expecting this to become
    # more useful over time
    try:
        data = process_input(args.in_file)

    except Exception:
        print("input file not found or formatted incorrectly")
        exit()

    # for part 1, we don't use the aim calculation. for part 2, we do
    if args.part == "1":
        multiple = calculate_bits(data)
        print("calculating multiple of gamma and epsilon rates")
        print(multiple)
    elif args.part == "2":
        multiple = calculate_oxygen_co2(data)
        print("calculating multiple of oxygen and co2 ratings")
        print(multiple)
    else:
        print("please supply a valid argument for --part (1 or 2)")
        exit()


if __name__ == "__main__":
    main()

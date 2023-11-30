"""
Python il buono
"""


def hello_word(name: str):
    """
    display "Hello {name}!
    :name: name to display
    """
    print(f"Hello {name}")


def truncates_negative_numbers(numbers: list):
    """
    replace negative numbers by 0
    :numbers: list of numbers
    """

    for num_idx, num_value in enumerate(numbers):
        if num_value < 0:
            numbers[num_idx] = 0


if __name__ == "__main__":
    # display your name
    MY_NAME = "toto"
    hello_word(MY_NAME)

    # truncate numbers
    my_list = [1, 5, 0, 7, -8]
    print(f"My list before truncates_negative_numbers: {my_list}")
    truncates_negative_numbers(my_list)
    print(f"My list after truncates_negative_numbers: {my_list}")

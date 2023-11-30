"""
Python il cattivo global variables
"""

DEFAULT_LANGUAGE_NAME = "python"


def get_language_name(new_language_name: str):
    """
    to understand global variables
    :param new_language_name: a function parameter
    """
    print(f"langage par défault : {DEFAULT_LANGUAGE_NAME}")
    print(f"je programme en : {new_language_name}")


def set_language_name(new_language_name: str):
    """
    to understand global variables
    :param new_language_name: a function parameter
    """
    DEFAULT_LANGUAGE_NAME = new_language_name
    print(f"langage par défault : {DEFAULT_LANGUAGE_NAME}")
    print(f"je programme en : {new_language_name}")


if __name__ == "__main__":
    get_language_name("Java")
    set_language_name("Java")
    print(f"DEFAULT_LANGUAGE_NAME: {DEFAULT_LANGUAGE_NAME}")

"""""
Python il brutto
"""

from copy import deepcopy

if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = deepcopy(list_1)
    list_2.append("Soleil")

    print(f"List n°1: {list_1}")
    print(f"List n°2: {list_2}")

    list_3 = [[1, 2, 3]]
    list_4 = deepcopy(list_3)
    list_4[0].append("Soleil")

    print(f"List n°3: {list_3}")
    print(f"List n°4: {list_4}")

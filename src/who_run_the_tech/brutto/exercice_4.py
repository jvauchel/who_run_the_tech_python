"""""
Python il brutto
"""

if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = list_1
    list_2.append("Soleil")

    print(f"List n°1: {list_1}")
    print(f"List n°2: {list_2}")

    list_3 = [[1, 2, 3]]
    list_4 = list_3
    list_4[0].append("Soleil")

    print(f"List n°1: {list_3}")
    print(f"List n°2: {list_4}")

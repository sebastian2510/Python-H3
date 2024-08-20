def merge(l1: list, l2: list) -> list:
    return sorted(l1 + l2)


if __name__ == "__main__":
    print(merge([1, 3, 2, 5, 4], [6,7,8,9,10]))
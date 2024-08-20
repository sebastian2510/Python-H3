import math
if __name__ == "__main__":
    print("\nDag 2 øvelse datastruktur begreber\n")
    numbers = [1, 2, 3, 4, 5]
    strings = ["apple", "an","banana", "cat", "dog", "elephant"]
    squares = [int(math.pow(number, 2)) for number in numbers]
    long_strings = [string for string in strings if len(string) > 3]
    print(squares)
    print(long_strings)

    


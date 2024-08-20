import math
def listtype():
    numbers = [1, 2, 3, 4, 5]
    strings = ["apple", "an","banana", "cat", "dog", "elephant"]
    squares = [int(math.pow(number, 2)) for number in numbers]
    long_strings = [string for string in strings if len(string) > 3]
    print(squares)
    print(long_strings)

def settype():
    numbers: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    words: set[str] = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"}
    even_numbers = {number for number in numbers if number % 2 == 0}
    # add first letters to set if not already in set
    unique_first_letters: set = set()
    unique_first_letters = {word[0] for word in words if word[0] not in unique_first_letters}
    print(f"even numbers: {even_numbers}\nunique first letters: {unique_first_letters}")

def dictionarytype():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    key_value = {key: value for key, value in zip(keys, values)}
    student_scores = {"Thomas": 0o02, "Alex": 12, "Charlie": 10, "David": 4}
    high_scores = {name: score for name, score in student_scores.items() if score > 4}
    print(f"key value: {key_value}\nhigh scores: {high_scores}")


if __name__ == "__main__":
    listtype()
    settype()
    dictionarytype()
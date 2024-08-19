# Øvelse: Grundlæggendeinput/output funktion
value: int = 1
print(f"{value} + {value} equals {value + value}")
# name: str = input("Give me your name: ")
# print(f"Hello, {name}!")

for i in range(4):
    if i == 3:
        print("Bye!")
        continue

    print(f"Hello")


# Øvelse Grundlæggendevariable håndtering
a: int = 1
print(a)
b: str = "Some text"
print(b)

print(f"the type of a is {type(a).__name__}")
print(f"the type of b is {type(b).__name__}")
c = 0+2j
print(f"the type of c is {type(c*c).__name__} and the value is {complex(3, c)}")


# Binary values - print hello world
text = "Hello, World!"
print(f"{bytes.hex(b'Hello, World!')}")
import base64


# Decimal
decimal_values = [float(ord(char)) for char in text]
print(f"Decimal: {decimal_values}")

# Binary
binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
print(f"Binary: {binary_values}")

# Octal
octal_values = [oct(ord(char))[2:] for char in text]
print(f"Octal: {octal_values}")

# Base64
base64_value = base64.b64encode(text.encode()).decode()
print(f"Base64: {base64_value}")

# Unicode
unicode_values = [f"\\u{ord(char):04x}" for char in text]
print(f"Unicode: {unicode_values}")

# Øvelse 5
print()
 
print(f"Øvelse 5.1 (list)")
fruits: list = ["apple", "banana", "cherry", "Date"]
print(fruits)
fruits.append("elderberry")
fruits.append("fig")
print(fruits.__len__()) 
fruits.remove("cherry")
for fruit in fruits:
    print(fruit)

print("The list is already sorted")
for fruit in fruits.sort():
    print(fruit)

print("")
print(f"Øvelse 5.2 (Tuple)")
fruits: tuple = ("apple", "banana", "cherry", "Date")
print(fruits)
print(fruits.__len__())
print(f"{fruits[0]} | {fruits[-1]}")
for fruit in fruits:
    print(fruit)

fruits = list(fruits)
fruits.append("elderberry")
fruits.append("fig")
fruits = tuple(fruits)

print("")
print(f"Øvelse 5.3 (Sets)")
fruits: set = {"apple", "banana", "cherry", "Date"}
print(fruits)
fruits.add("elderberry")
fruits.add("fig")
print(fruits.__len__())
fruits.remove("cherry")
print(f"{fruits.__contains__('banana')}")
for fruit in fruits:
    print(fruit)

fruits.clear()
print(fruits)

print("")
print(f"Øvelse 5.4 (Dictionary)")
fruit_prices: dict = {"apple": 0.99, "banana": 0.59, "cherry": 2.99, "Date": 3.49}
print(fruit_prices)
fruit_prices["elderberry"] = 4.99
fruit_prices["fig"] = 1.99
print(fruit_prices.__len__())
fruit_prices.pop("cherry")
for fruit, price in fruit_prices.items():
    print(f"{fruit}: {price}")

fruit_prices["apple"] = 1.09
print(fruit_prices)

print("List: dynamisk storage af data")
print("Tuple: statisk storage af data")
print("Set: unikke værdier (hashset)")
print("Dictionary: key-value pairs (hashmap)")
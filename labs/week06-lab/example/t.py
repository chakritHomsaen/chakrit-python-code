# Example 1: Function with one parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()

"""
Calling greet_person with different names:
Hello, Alice! Nice to meet you.
Hello, Bob! Nice to meet you.
Hello, Charlie! Nice to meet you.

"""

def introduce_person(name, age, city):
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")
"""
Calling introduce_person:
Hi! My name is Diana.
I am 25 years old.
I live in New York.

Hi! My name is Eve.
I am 30 years old.
I live in Los Angeles.

"""

def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

"""
Calculating rectangle areas:
Rectangle with length 5 and width 3
Area = 5 × 3 = 15

Rectangle with length 10 and width 7
Area = 10 × 7 = 70

"""
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

"""
Using functions that return values:
5 + 3 = 8
10 + 7 = 17
Sum of both results: 25

"""

def greet_with_title(name="Yo", title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title()
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

"""
Using default parameters:
Hello, Mr./Ms. Smith!
Hello, Dr. Johnson!
Hello, Prof. Brown!

"""

def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

"""
Multiple default parameters:
Profile: Alice, Age: 18, Country: Unknown
Profile: Bob, Age: 25, Country: Unknown
Profile: Charlie, Age: 30, Country: USA

"""


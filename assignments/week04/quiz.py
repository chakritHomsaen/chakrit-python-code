
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

+++++++++++++

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("สมชาย", 2, "ลอนดอน", "อังกฤษ")  # name, age, city, country
    hobbies = []
    
    # Your code here
    age = int(input("input your age : "))
    hob = input("input your hobbies : ")

    new_person = (person[0], age, person[2], person[3])
    hobbies.append(hob)

    name, age, city, country = person
    print(f"Name: {name}, Age: {age}, city: {city}, country: {country}")
    name, age, city, country = new_person
    print(f"Name: {name}, Age: {age}, city: {city}, country: {country}")
    print(hobbies)

    pass

if __name__ == "__main__":
    personal_info_manager()

+++++++++++

Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

########"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        numbers = []
        num_Temporary = int(input(f"{i+1}.number : "))
        numbers.append(num_Temporary)
        print(numbers)
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    #even_numbers = # Your code here
    #odd_numbers = # Your code here
    
    # Calculate average
    #average = # Your code here
    
    # Numbers greater than average
    #above_average = # Your code here
    
    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()


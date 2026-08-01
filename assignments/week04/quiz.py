
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("สมชาย", 2, "ลอนดอน", "อังกฤษ")  # name, age, city, country
    hobbies = []
    
    # Your code here
    print("Hi")
    name, age, city, country = person
    print(f"Name: {name}, Age: {age}, City: {city}, Country: {country}")
    while(True):
        print("="*50)
        print("Choose what you want to do")
        print("1.Add hobbie")
        print("2.Remove hobbie")
        print("3.Update age")
        print("4.Exit")
        print("="*50)
        ans = input("you choose :")
        if not ans.strip():
            continue
        if ans == '1':
            hob_add = input("input your hobbies : ")
            if not hob_add.strip():
                continue
            hobbies.append(hob_add)
        elif ans == '2':
            print(hobbies)
            hob_remove = input("input your hobbies want to remove : ")
            if not hob_remove.strip():
                continue
            elif hob_remove in hobbies:
                hobbies.remove(hob_remove)
        elif ans == '3':
            age = input("input your new age : ")
            if not age.strip():
                continue
            new_person = (person[0], age, person[2], person[3])
        elif ans == '4':
            print("="*50)
            break
            
        print("="*50)
    name, age, city, country = new_person
    print(f"Name: {name}, Age: {age}, city: {city}, country: {country}")
    print(hobbies)



if __name__ == "__main__":
    personal_info_manager()

"""

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
    numbers = []
    for i in range(10):
        num_Temporary = int(input(f"{i+1}.number : "))
        numbers.append(num_Temporary)
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []
    odd_numbers = []# Your code here
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        elif number % 2 == 1:
            odd_numbers.append(number)
    # Calculate average
    average = float(sum(numbers)/10)
    
    # Numbers greater than average
    above_average = []
    for above in numbers:
        if above > average:
            above_average.append(above)
    # Display results
    # Your code here
    print(f"even_numbers: {even_numbers}")
    print(f"odd_numbers: {odd_numbers}")
    print(f"Average: {average :.2f}")
    print(f"Above Average: {above_average}")


if __name__ == "__main__":
    number_operations()


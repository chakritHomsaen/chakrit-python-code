"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    list_temp = [30, 41, 29, 25, 26, 30, 20]
    return list_temp    


'''
    for i in range(8):
        temp = input(f"put temperatures day {i}")
        list_temp.append(temp)
'''


def analyze_temps(temp_list):

    avg_temp = round(sum(temp_list) / 7, 2)
    max_temp = max(temp_list)
    min_temp = min(temp_list)

    return (avg_temp, max_temp, min_temp)

def display_analysis(avg, high, low):
    
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg} C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")

data = get_temperatures()
print(data)
analyze = analyze_temps(data)
print(analyze)
display_analysis(analyze[0], analyze[1], analyze[2])

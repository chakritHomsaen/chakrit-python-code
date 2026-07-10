print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

seconds = int(input("Input seconds :"))

hour = seconds // 3600
seconds_remain = seconds % 3600

minutes = seconds_remain // 60
seconds_remain1 = seconds_remain % 60

print(f" {seconds} seconds = {hour} hour, {minutes} minute, {seconds_remain1} second")

'''
# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age >= 0 and age <= 12:
    print("You are Child")
elif age >= 13 and age <= 19:
    print("You are Teenager")
elif age >= 20 and age <= 59:
    print("You are Adult")
elif age >= 60:
    print("You are Senior")
else:
    print("error")

print()
'''
# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:

        if choice == '1':
            print(f"Now you have Balance : {balance}")

        elif choice == '2':
            while True:
                withdraw = int(input("How many you want to withdraw :"))
                if withdraw > balance:
                    print("There isn't enough to withdraw")

                    ans = input("want to try again (y/n) :").lower()

                    if ans == 'y':
                        continue
                    elif ans == 'n':
                        break
                    else:
                        print("error")
                        continue
                balance -= withdraw
                print(f"Now you have balance {balance}")
                break

        elif choice == '3':
            Deposit = int(input("How many yuo want to Deposit :"))
            balance += Deposit

        elif choice == '4':
            break
        else:
            print("error")
        
else:
    print("Invalid PIN")

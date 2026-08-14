"""
แปลงค่าเงิน 
THB <-> USD 1 USD = 32 THB
THB <-> JPY 100 JPY = 22 THB


"""
def conversion_currency(num, ans):
    if ans == '1':
        print("You select THB to USD")
        result = num / 32
        print("you have :" ,round(result ,2),"USD")
        print(f"calculation formula used {num} / 32")
    elif ans == '2':
        print("You select USD to THB")
        result = num * 32
        print("you have :" ,round(result ,2),"THB")
        print(f"calculation formula used {num} * 32")

    elif ans == '3':
        print("You select THB to JPY")
        result = num * 4.545
        print("you have :" ,round(result ,2),"JPY")
        print(f"calculation formula used {num} * 4.545")

    elif ans == '4':
        print("You select JPY to THB")
        result = num * 0.22
        print("you have :" ,round(result ,2),"THB")
        print(f"calculation formula used {num} * 0.22")

    else:
        print("error")




print("=" * 50)
print("Currency Converter programe")
print("=" * 50)

while True:
    print("if want THB to USD press 1")
    print("if want USD to THB press 2")
    print("if want THB to JPY press 3")
    print("if want JPY to THB press 4")
    print("Exit press 5")
    ans = input("press you want :")
    if ans == '5':
        break
    num = float(input("press you amount to convert :"))
    conversion_currency(num, ans)
    print()

print("=" * 50)
print("End program Thank")
print("=" * 50)
print("Enter price of 6 item")
table = []
for i in range(1,7):
    add_price = int(input(f"Item {i}: "))
    
    table.append([i, add_price])
print()
badget_total = int(input("Enter total butget :"))
print()

current_total = badget_total
bought = []
for No, price in table:
    if price <= current_total:
        print(f"Item {No} = {price} -> Buy")
        current_total = current_total - price
        print(f"current total = {current_total}")
        bought.append(price)
        print()
    else :
        print(f"Item {No} = {price} -> connot buy")
        print(f"current total = {current_total}")
        print()

print(f"bought item: {bought}")
print(f"total spen: {badget_total - current_total}")
print(f"Remaining budget: {current_total}")
def calculate_electricity_cost(units):
    electricity_rate = [(   1, 2.50,   50), (  51, 3.00, 100         ),
                        ( 101, 3.50,  200), ( 201, 4.00, float("inf")),]
    cost_table = [(f"{low:,}-{units if high ==  float("inf") else high:,} หน่วย", ((min(units, high) - (low-1)) * rate))
                       for low, rate, high in electricity_rate if units >= low]
    
    return cost_table

while True:
    print("="*5 + " โปรแกรมคำนวนค่าไฟฟ้า " + "="*5)
    print("1. คำนวนค่าไฟ")
    print("2. ออกจากโปรแกรม")

    menu = input("เลือกเมนู: ")
    if menu == "1":
        print()
        if menu == "1":
            units = float(input("put units : ")) 
            cost_table = calculate_electricity_cost(units)
            cost_total = sum(cost for _, cost in cost_table)
            print()
            print("\n" .join(f"{label}: {cost:,.2f}" for label, cost in cost_table if cost >= 0))
            print("ค่าบริการ: 25.00 บาท")
            print(f"รวมค่าไฟทั้งสิ้น {cost_total + 25.00:,.2f}")
            print("="*30)
            print()

    elif menu == "2":
        print()
        print("จบการทำงาน")
        print("="*30)
        break

    else:
        print("ผิดพลาด โปรดใส่ตัวเลข 1 หรือ 2 เท่านั้น")
        print("="*30)
        print()
        continue



        

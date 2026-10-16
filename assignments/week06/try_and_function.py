def deposit(money):
    total = 1000
    return total + money

try:
    print(f"ยอดเงินเริ่มต้น: {deposit(0)}")
    num = int(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
    print()
    
    if num <= 0:
        raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

except ValueError as e:
    if str(e) == "จำนวนเงินฝากต้องมากกว่า 0":
        print(e)
    else:
        print()    
        print("กรุณากรอกตัวเลขเท่านั้น")

else:
    print("ฝากเงินสำเร็จ")
    print(f"ยอดเงินคงเหลือ: {deposit(num)}")

finally:
    print("สิ้นสุดรายการฝากเงิน")


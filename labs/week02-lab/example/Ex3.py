# Template 3: Shopping Calculator
#shopping_calculator = 
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal ราคาเต็มเท่าไหร่
# TODO: Calculate discount amount ได้ส่วนลด
# TODO: Calculate price after discount ราคาหลังแล้ว
# TODO: Calculate tax amount ภาษีเท่าไหร่
# TODO: Calculate final total สรุปต้องจ่ายเท่าไหร่
# TODO: Display itemized receipt พ่นออก

subtotal = item_price * quantity
discount = subtotal * (discount_percent / 100)
price_after_discount = subtotal - discount
tex = price_after_discount * (tax_percent/100)
final_total = price_after_discount + tex
print()
print(f"subtotal = {subtotal:.2f}")
print(f"discount amount = {discount:.2f}")
print(f"price after discount = {price_after_discount:.2f}")
print(f"tax amount = {tex:.2f}")
print(f"final total = {final_total:.2f}")

print()
print("thx")
print()
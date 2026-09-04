#1.รับค่า text จากผู้ใช้
#2.รับค่าอักขระจากที่ต้องการค้นหาจากผู้ใช้
#3.แสดงผลจำนวนของอัขระในข้อความ

'''print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text: ")
char_find = input("Character to find: ")
for letter in text:
    if letter == char_find:
        count += 1
print(f"{count} letters '{char_find}' found in '{text}'")'''

print()

password = input("Insert password: ")

listwords = password.split("@")
words = ''.join(listwords)

if words.isalnum() and len(password) >= 8 and password.count('@') == 1:
    print("your password is strong")
else:
    print("your password is not strong")
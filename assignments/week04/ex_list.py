print("="*50)
print()

name = input("What's your name? : ")

letters = list(name)
count = 0
vowels = ('a', 'e', 'i', 'o', 'u')

for letter in letters :
    letter = letter.lower()
    if letter in vowels :
        count = count + 1

print(f"your name have vowel : {count}")
print()
print("="*50)
import random
import secrets
import string

print("=== Password Generator ===")

print("\nChoose password strength:")
print("1. Weak")
print("2. Normal")
print("3. Good")
print("4. Powerful+")
print("5. PLUS ULTRA")

choice = input("\nChoose 1-5: ").strip()

if choice == "1":
    length = random.randint(6, 8)
    chars = string.ascii_lowercase
    strength = "Weak"

elif choice == "2":
    length = random.randint(8, 10)
    chars = string.ascii_letters
    strength = "Normal"

elif choice == "3":
    length = random.randint(12, 14)
    chars = string.ascii_letters + string.digits
    strength = "Good"

elif choice == "4":
    length = random.randint(24, 32)
    chars = string.ascii_letters + string.digits + string.punctuation
    strength = "Powerful+"

elif choice == "5":
    length = random.randint(50, 80)
    chars = string.ascii_letters + string.digits + string.punctuation
    strength = "PLUS ULTRA"

else:
    print("Invalid option!")
    exit()

password = ""

for i in range(length):
    password += secrets.choice(chars)

print("\nStrength:", strength)
print("Length:", length)
print("Generated password:")
print(password)
# Advanced Caesar Cipher Tool
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Welcome message
print("="*50)
print("🔥 Welcome to the Advanced Caesar Cipher Tool 🔥")
print("="*50)

# User input
message = input("Enter your message: ").strip()
if not message:
    print("❌ Message cannot be empty!")
    input("\nPress Enter to exit...")
    exit()

try:
    shift = int(input("Enter shift value (number): ").strip())
except ValueError:
    print("❌ Invalid shift value! Must be a number.")
    input("\nPress Enter to exit...")
    exit()

# Perform encryption and decryption
encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

# Display results
print("\n--- Results ---")
print(f"Original Message : {message}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted} (should match original)")

print("\n✅ Encryption & Decryption completed successfully!")
print("="*50)

# Pause so window doesn't close immediately
input("\nPress Enter to exit...")

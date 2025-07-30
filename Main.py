def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def reverse_text(text):
    return text[::-1]


def ascii_shift(text, shift_val):
    return ''.join(chr(ord(char) + shift_val) for char in text)


def ascii_unshift(text, shift_val):
    return ''.join(chr(ord(char) - shift_val) for char in text)


def encrypt(text, key, shift_val=1):
    print(f"\nEncryption Steps")
    step1 = caesar_encrypt(text, key)
    print("1. Caesar Cipher:", step1)

    step2 = reverse_text(step1)
    print("2. Reversed:", step2)

    step3 = ascii_shift(step2, shift_val)
    print("3. ASCII Shift (+1):", step3)

    return step3


def decrypt(text, key, shift_val=1):
    print(f"\nDecryption Steps")
    step1 = ascii_unshift(text, shift_val)
    print("1. ASCII Unshift (-1):", step1)

    step2 = reverse_text(step1)
    print("2. Reversed:", step2)

    step3 = caesar_decrypt(step2, key)
    print("3. Caesar Decryption:", step3)

    return step3


def main():
    mode = input("Do you want to (E)ncrypt or (D)ecrypt?: ").lower()
    text = input("Enter the message: ")
    key = int(input("Enter Caesar Cipher key (number): "))

    if mode == 'e':
        encrypted = encrypt(text, key)
        print("\nFinal Encrypted Text:", encrypted)

    elif mode == 'd':
        decrypted = decrypt(text, key)
        print("\nFinal Decrypted Text:", decrypted)

    else:
        print("Invalid mode. Choose 'E' or 'D'.")


if __name__ == "__main__":
    main()

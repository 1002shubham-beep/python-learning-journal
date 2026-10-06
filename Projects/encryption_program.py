import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
keys = chars.copy()
# keys = random.shuffle(chars) Wrong as random.shuffle(chars) is a method to modify the list not creating a new one so storing the result in keys is None as it doesnt returns anything
random.shuffle(chars)

# ENCRYPT
def to_encrypt(message):
    cipher_text=""
    for _ in message:
        idx1 =  chars.index(_)
        cipher_text += keys[idx1]
    return cipher_text

# DECRYPT
def to_decrypt(cipher_text):
    decrypted_text=""
    for _ in cipher_text:
        idx2 = keys.index(_)
        decrypted_text += chars[idx2]
    return decrypted_text

def main():
    pin = 6416
    message = input("Enter a message to encrypt: ")
    encrypted_message = to_encrypt(message)
    print(f"Encrypted message: {encrypted_message}")
    while True:
        decrypt= int(input("Enter the pin to decrypt: " ))
        if decrypt == pin:
            decrypted_message = to_decrypt(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
            break
        else:
            print("Wrong pin, Try again")
            continue

if __name__=='__main__':
    main()
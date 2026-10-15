import secrets
import string

chars = string.ascii_letters
nums = string.digits
punctuation = string.punctuation


def password_generator(length, special_chars, numbers):
    pool = chars
    password = [secrets.choice(chars)]  # guarantee at least one letter

    if special_chars:
        pool += punctuation
        password.append(secrets.choice(punctuation))
    if numbers:
        pool += nums
        password.append(secrets.choice(nums))

    # fill the remaining length from the full pool
    while len(password) < length:
        password.append(secrets.choice(pool))

    # shuffle so guaranteed characters aren't predictable positions
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def password_checker(password):
    score = 0
    if len(password) >= 12:
        score += 1
        print("+1 length")
    if any(c.isupper() for c in password):
        score += 1
        print("+1 uppercase")
    if any(c.islower() for c in password):
        score += 1
        print("+1 lowercase")
    if any(c.isdigit() for c in password):
        score += 1
        print("+1 digit")
    if any(c in punctuation for c in password):
        score += 1
        print("+1 punctuation")

    print(f"Score: {score}/5")

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def ask_yes_no(prompt):
    return input(prompt).strip().lower() == "y"


def main():
    print("Welcome to password generator")

    while True:
        try:
            length = int(input("Enter the length of your password: "))
            if length < 3:
                print("Please choose at least 3 characters.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    special_chars = ask_yes_no("Include special characters? (Y/N): ")
    numbers = ask_yes_no("Include numbers? (Y/N): ")

    password = password_generator(length, special_chars, numbers)
    print(f"\nYour password: {password}")
    print(f"Strength: {password_checker(password)}")


if __name__ == "__main__":
    main()
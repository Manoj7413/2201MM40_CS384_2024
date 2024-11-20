
with open('input.txt', 'w') as file:
    file.write("abc12345\n")
    file.write("abc\n")
    file.write("123456789\n")
    file.write("abcdefg$\n")
    file.write("abcdefgABHD!@313\n")
    file.write("abcdefgABHD$$!@313\n")

import re
def check_password(password, criteria):
    if len(password) < 8:
        return False, "Less than 8 characters"

    errors = []


    if 1 in criteria and not re.search(r'[A-Z]', password):
        errors.append("Uppercase letters missing")


    if 2 in criteria and not re.search(r'[a-z]', password):
        errors.append("Lowercase letters missing")


    if 3 in criteria and not re.search(r'[0-9]', password):
        errors.append("Numbers missing")


    special_characters = "!@#"
    if 4 in criteria:
        if not re.search(r'[!@#]', password):
            errors.append("Special characters missing")
        elif re.search(r'[^a-zA-Z0-9!@#]', password):
            errors.append("Contains invalid special characters")

    if errors:
        return False, ', '.join(errors)
    return True, "Valid"



def validate_passwords_from_file(filename):
    print("Select the criteria for password validation:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Special characters (!, @, #)")

    selected_criteria = input("Enter the numbers corresponding to the criteria (comma separated): ")
    criteria = list(map(int, selected_criteria.split(',')))

    valid_count = 0
    invalid_count = 0

    try:
        with open(filename, 'r') as file:
            passwords = file.readlines()

            for password in passwords:
                password = password.strip()
                is_valid, reason = check_password(password, criteria)

                if is_valid:
                    valid_count += 1
                else:
                    invalid_count += 1
                    print(f"'{password}' is Invalid. Reason: {reason}.")

        print(f"\nTotal valid passwords: {valid_count}")
        print(f"Total invalid passwords: {invalid_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



validate_passwords_from_file('input.txt')
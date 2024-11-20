
import re
def check_password(password, criteria):
    if len(password) < 8:
        print(f"'{password}' is Invalid. Reason: Less than 8 characters.")
        return

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
        print(f"'{password}' is Invalid. Reason: {', '.join(errors)}.")
    else:
        print(f"'{password}' is Valid.")



def validate_passwords(password_list):
    print("Select the criteria for password validation:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Special characters (!, @, #)")

    selected_criteria = input("Enter the numbers corresponding to the criteria (comma separated): ")
    criteria = list(map(int, selected_criteria.split(',')))

    for password in password_list:
        check_password(password, criteria)

password_list = [
    # "abc12345",
    # "abc",
    # "123456789",
    # "abcdefg$",
    # "abcdefgABHD!@313",
    # "abcdefgABHD$$!@313",
]

a=int(input())
for i in range (a):
  # pass = input()
  password_list.append(input())

validate_passwords(password_list)

character = input("Enter a single character: ")

if len(character) == 1:
    ascii_value = ord(character)
    print("ASCII value:", ascii_value)

    if character.isupper():
        print("Character type: Uppercase letter")
    elif character.islower():
        print("Character type: Lowercase letter")
    elif character.isdigit():
        print("Character type: Digit")
    else:
        print("Character type: Special Character")
else:
    print("Error: Please enter exactly one character.")
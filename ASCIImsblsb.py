def get_user_input():
    """Function to get a character input from the user."""
    char = input("Enter a character: ")
    return char


def char_to_ascii(char):
    """Convert a character to its ASCII value."""
    return ord(char)


def ascii_to_char(ascii_val):
    """Convert an ASCII value to its character."""
    return chr(ascii_val)


def main():
    """Main function to run the user assignment program."""
    char = get_user_input()
    ascii_val = char_to_ascii(char)
    char_from_ascii = ascii_to_char(ascii_val)

    print(f"\nCharacter: {char}")
    print(f"ASCII value: {ascii_val}")
    print(f"Character from ASCII: {char_from_ascii}")


if __name__ == "__main__":
    main()

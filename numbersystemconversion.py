def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def decimal_to_octal(n):
    return oct(n).replace("0o", "")


def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")


def binary_to_decimal(b):
    return int(b, 2)


def octal_to_decimal(o):
    return int(o, 8)


def hexadecimal_to_decimal(h):
    return int(h, 16)


def binary_to_octal(b):
    decimal = binary_to_decimal(b)
    return decimal_to_octal(decimal)


def binary_to_hexadecimal(b):
    decimal = binary_to_decimal(b)
    return decimal_to_hexadecimal(decimal)


def octal_to_binary(o):
    decimal = octal_to_decimal(o)
    return decimal_to_binary(decimal)


def octal_to_hexadecimal(o):
    decimal = octal_to_decimal(o)
    return decimal_to_hexadecimal(decimal)


def hexadecimal_to_binary(h):
    decimal = hexadecimal_to_decimal(h)
    return decimal_to_binary(decimal)


def hexadecimal_to_octal(h):
    decimal = hexadecimal_to_decimal(h)
    return decimal_to_octal(decimal)


# Main function to handle user input
def convert_number():
    print("Number System Converter")
    print("1. Decimal to Binary/Octal/Hexadecimal")
    print("2. Binary to Decimal/Octal/Hexadecimal")
    print("3. Octal to Decimal/Binary/Hexadecimal")
    print("4. Hexadecimal to Decimal/Binary/Octal")

    choice = int(input("Choose an option: "))

    if choice == 1:
        decimal = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal)}")
        print(f"Octal: {decimal_to_octal(decimal)}")
        print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
    elif choice == 2:
        binary = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
        print(f"Octal: {binary_to_octal(binary)}")
        print(f"Hexadecimal: {binary_to_hexadecimal(binary)}")
    elif choice == 3:
        octal = input("Enter an octal number: ")
        print(f"Decimal: {octal_to_decimal(octal)}")
        print(f"Binary: {octal_to_binary(octal)}")
        print(f"Hexadecimal: {octal_to_hexadecimal(octal)}")
    elif choice == 4:
        hexadecimal = input("Enter a hexadecimal number: ")
        print(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
        print(f"Binary: {hexadecimal_to_binary(hexadecimal)}")
        print(f"Octal: {hexadecimal_to_octal(hexadecimal)}")
    else:
        print("Invalid option selected!")


# Run the program
convert_number()

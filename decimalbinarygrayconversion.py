# Convert Decimal to BCD
def decimal_to_bcd(n):
    bcd = ''
    for digit in str(n):
        bcd += f'{int(digit):04b}'  # Convert each digit to 4-bit binary
    return bcd


# Convert BCD to Decimal
def bcd_to_decimal(bcd):
    decimal = ''
    for i in range(0, len(bcd), 4):
        digit = int(bcd[i:i + 4], 2)  # Take 4 bits and convert to decimal
        decimal += str(digit)
    return int(decimal)


# Convert Binary to Gray Code
def binary_to_gray(binary):
    binary = int(binary, 2)  # Convert binary string to integer
    gray = binary ^ (binary >> 1)  # XOR the binary number with itself shifted right by 1
    return format(gray, 'b')  # Return binary representation of gray code


# Convert Gray Code to Binary
def gray_to_binary(gray):
    gray = int(gray, 2)  # Convert gray code to integer
    binary = gray
    while gray > 0:
        gray = gray >> 1
        binary = binary ^ gray
    return format(binary, 'b')  # Return binary representation


# Main interactive program
def main():
    while True:
        print("\nConversion Options:")
        print("1. Decimal to BCD")
        print("2. BCD to Decimal")
        print("3. Binary to Gray")
        print("4. Gray to Binary")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            decimal_number = int(input("Enter a decimal number: "))
            bcd_code = decimal_to_bcd(decimal_number)
            print(f"Decimal: {decimal_number} to BCD: {bcd_code}")

        elif choice == '2':
            bcd_input = input("Enter a BCD code (group of 4-bit binary digits): ")
            decimal_output = bcd_to_decimal(bcd_input)
            print(f"BCD: {bcd_input} to Decimal: {decimal_output}")

        elif choice == '3':
            binary_number = input("Enter a binary number: ")
            gray_code = binary_to_gray(binary_number)
            print(f"Binary: {binary_number} to Gray: {gray_code}")

        elif choice == '4':
            gray_input = input("Enter a Gray code: ")
            binary_output = gray_to_binary(gray_input)
            print(f"Gray: {gray_input} to Binary: {binary_output}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

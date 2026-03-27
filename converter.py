def binary_to_hex(binary_str):
    # Validate binary input
    if not all(char in '01' for char in binary_str):
        raise ValueError("Input must be a binary string.")
    decimal_value = int(binary_str, 2)
    return hex(decimal_value)[2:]


def hex_to_binary(hex_str):
    # Validate hex input
    if not all(char in '0123456789abcdefABCDEF' for char in hex_str):
        raise ValueError("Input must be a hex string.")
    decimal_value = int(hex_str, 16)
    return bin(decimal_value)[2:]


# Main execution
if __name__ == '__main__':
    try:
        binary_input = input('Enter a binary number: ')
        print(f"Hexadecimal representation: {binary_to_hex(binary_input)}")

        hex_input = input('Enter a hexadecimal number: ')
        print(f"Binary representation: {hex_to_binary(hex_input)}")
    except ValueError as e:
        print(e)
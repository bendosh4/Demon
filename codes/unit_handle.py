import colors

def decimal_to_binary(number: int) -> str:
    binary_representation = bin(number)[2:]
    return binary_representation

def binary_to_decimal(binary_number: str) -> int:
    decimal_representation = int(binary_number, 2)
    return decimal_representation

def binary_to_exdecimal(binary_number: str) -> str:
    decimal_representation = int(binary_number, 2)
    exadecimal_representation = hex(decimal_representation)[2:]
    return exadecimal_representation

def exdecimal_to_binary(exadecimal_number: str) -> str:
    decimal_representation = int(exadecimal_number, 16)
    binary_representation = bin(decimal_representation)[2:]
    return binary_representation

def decimal_to_hexadecimal(decimal_number: int) -> str:
    hexadecimal_representation = hex(decimal_number)[2:]
    return hexadecimal_representation

def unit_conversion():
    types = ["decimal", "binary", "exadecimal"]
    
    for i, t in enumerate(types, start=1):
        print(f"{i}. {t}")
        
    print(f"{colors.COLORS['blue']}Enter the number his Type and type to turn (exp: 10 decimal binary): {colors.RESET}", end="")
    user_input = input()
    number, type_from, type_to = user_input.split()
    
    if type_from not in types or type_to not in types:
        print(f"{colors.COLORS['red']}Invalid type. Please choose from the given types (decimal, binary, exadecimal).{colors.RESET}")
        return
    
    if type_from == "decimal":
        if type_to == "binary":
            binary_representation = decimal_to_binary(int(number))
            print(f"{colors.COLORS['green']}Binary representation: {binary_representation}{colors.RESET}")
        elif type_to == "exadecimal":
            exadecimal_representation = decimal_to_hexadecimal(int(number))
            print(f"{colors.COLORS['green']}Exadecimal representation: {exadecimal_representation}{colors.RESET}")
    elif type_from == "binary":
        if type_to == "decimal":
            decimal_representation = binary_to_decimal(number)
            print(f"{colors.COLORS['green']}Decimal representation: {decimal_representation}{colors.RESET}")
        elif type_to == "exadecimal":
            exadecimal_representation = binary_to_exdecimal(number)
            print(f"{colors.COLORS['green']}Exadecimal representation: {exadecimal_representation}{colors.RESET}")
    elif type_from == "exadecimal":
        if type_to == "decimal":
            decimal_representation = int(number, 16)
            print(f"{colors.COLORS['green']}Decimal representation: {decimal_representation}{colors.RESET}")
        elif type_to == "binary":
            binary_representation = exdecimal_to_binary(number)
            print(f"{colors.COLORS['green']}Binary representation: {binary_representation}{colors.RESET}")

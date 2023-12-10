def convert_base_to_decimal(number, base):
    # function to convert base to decimal
    return int(str(number), base) if str(number).isdigit() else ValueError(f'invaled number inputed:{number}')

def convert_decimal_to_base(number, base):
    return "" if number == 0 else convert_decimal_to_base(number // base, base) + str(number % base)

def convert_base_to_base(number, from_base, to_base):
    return convert_decimal_to_base(int(str(number),from_base), to_base)

def get_user_input():
    to_convert = input("Enter tne number to convert")
    convert_from = int(input("Enter the base to convert from"))
    convert_to = int(input("Enter the base to convert to"))
    return to_convert, convert_from, convert_to

def main():
    try:
        number, from_base, to_base = get_user_input()
        result = convert_base_to_base(number, from_base, to_base)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error:{e}")
    
if __name__ == '__main__':
    main()    
    
    
    
    

def convert_unit(value, from_unit, to_unit):
    # Dictionary of conversion factors (you can expand this)
    conversions = {
        ('celsius', 'fahrenheit'): lambda x: x * 9/5 + 32,
        ('fahrenheit', 'celsius'): lambda x: (x - 32) * 5/9,
        ('kilometers', 'miles'): lambda x: x * 0.621371,
        ('miles', 'kilometers'): lambda x: x / 0.621371,
        # Add more conversions as needed
    }
    
    if (from_unit, to_unit) in conversions:
        return conversions[(from_unit, to_unit)](value)
    elif (to_unit, from_unit) in conversions:
        return 1 / conversions[(to_unit, from_unit)](1 / value)
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        try:
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            
            result = convert_unit(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
            
            convert_back = input("Do you want to convert back to the original unit? (yes/no): ").lower()
            if convert_back == 'yes':
                inverse_result = convert_unit(result, to_unit, from_unit)
                print(f"{result:.4f} {to_unit} is equal to {inverse_result:.4f} {from_unit}")
            
            another = input("Do you want to perform another conversion? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Unit Converter. Goodbye!")
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

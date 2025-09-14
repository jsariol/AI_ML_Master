
"""
Temperature Converter
- Prompts the user to enter a temperature and the unit (C/F).
- Converts the value to the other unit and prints the result.
"""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def main():
    print("=== Temperature Converter ===")
    try:
        value = float(input("Enter temperature value: "))
        unit = input("Enter unit (C/F): ").strip().upper()

        if unit == "C":
            converted = celsius_to_fahrenheit(value)
            print(f"{value:.2f} °C = {converted:.2f} °F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(value)
            print(f"{value:.2f} °F = {converted:.2f} °C")
        else:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Error: You must enter a numeric temperature.")

if __name__ == "__main__":
    main()

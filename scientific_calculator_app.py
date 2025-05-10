import math

# Basic Operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error (division by zero)" if y == 0 else x / y

# Scientific Functions
def power(x, y): return math.pow(x, y)
def sqrt(x): return math.sqrt(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x): return math.log10(x)
def ln(x): return math.log(x)

# Display Menu
def menu():
    print("\n=== Scientific Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. sin(x)")
    print("8. cos(x)")
    print("9. tan(x)")
    print("10. log10(x)")
    print("11. ln(x)")
    print("0. Exit")

# Main Program Loop
while True:
    menu()
    choice = input("Enter your choice (0-11): ")

    try:
        if choice == '0':
            print("Thank you for using the calculator!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        elif choice in ['6', '7', '8', '9', '10', '11']:
            x = float(input("Enter the number: "))

        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
        elif choice == '5':
            print("Result:", power(x, y))
        elif choice == '6':
            print("Result:", sqrt(x))
        elif choice == '7':
            print("Result:", sin(x))
        elif choice == '8':
            print("Result:", cos(x))
        elif choice == '9':
            print("Result:", tan(x))
        elif choice == '10':
            print("Result:", log(x))
        elif choice == '11':
            print("Result:", ln(x))
        else:
            print("Invalid choice. Please enter a number from 0 to 11.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("An error occurred:", e)

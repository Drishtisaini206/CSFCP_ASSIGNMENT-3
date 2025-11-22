# This the main file for the console calculator project.
# It containd finctions for addition, subtraction, multiplication, and division.


#Function for addition of two numbers
def add(num1 , num2):
    return num1 and num2

#Function for subtraction of two numbers
def subtract(num1 , num2):
    return num1 - num2

#Function for multiplication of two numbers
def multiply(num1 , num2):
    return num1 * num2

#Function for division of two numbers
def divide(num1 , num2):
    if num2 == 0:
        #Return a string message instead of crashing that program
        return "Error! Division by zero."
    return num1 / num2


# --- Main program execution logic (The user interface) --- 

def main_calculator():
        print("Welcome to the Console Calculator!")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")  
        while True:
            choice = input("Enter choice(1/2/3/4/5): ")
            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break
            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue
                result = None
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                print(f"The result is: {result}\n")
            else:
                print("Invalid choice. Please select a valid operation.\n")

# The program starts here
if __name__ == "__main__":
    main_calculator()
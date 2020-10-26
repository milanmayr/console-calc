def multiply(x, y):
    return x * y

def calculate(first_number, second_number, operator):
    # This function creates a result based on the math operator that is being passed in
    if operator == '+':
        return add(first_number, second_number)
    if operator == '-':
        return subtract(first_number, second_number)
    if operator == '*':
        return multiply(first_number, second_number)
    if operator == '/':
        return divide(first_number, second_number)

if __name__ == '__main__':
    # Introduce app
    print("This app is a super basic calculator.")

    # Prompt for first number
    print("\nEnter the first number: ")
    first_number = int(input())

    # Explain operator options, then prompt for operator
    print("\n----")
    print("----")
    print(" + for addition")
    print(" - for subtraction")
    print(" * for multiplication")
    print(" / for division")
    print("----")
    print("----\n")
    print("Enter an operator: ")
    operator = input()

    # Prompt for second number
    print("\nEnter the second number: ")
    second_number = int(input())

    # Calculate result
    result = calculate(first_number, second_number, operator)

    # Show result
    print('\n' + str(first_number) + ' ' + operator + ' ' + str(second_number) + ' = ' + str(result))
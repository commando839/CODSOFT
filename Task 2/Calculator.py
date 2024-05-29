# Add 2 number
def add(num1, num2):   
    return num1 + num2 

# Subtract 2 numbers
def subtract(num1, num2): 
    return num1 - num2

# Multiply 2 numbers
def product(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    return num1 * num2 

# Divide 2 numbers
def divide(num1, num2):
    if num2 == 0:
        print("MATH ERROR!")
    return num1 / num2 

while True:
    choice = input("Do you wish to continue? Press y for yes and n for no.\nEnter your choice: ")
    if choice == 'n':
        break
    
    elif choice == "y":
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))  

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter the operation of choice (1,2,3,4):")
        
        if operation not in ["1", "2", "3", "4"] :    
            print ("The operation is invalid.") 
        
        else: 
            if operation == "1":
                print ("The sum of the two numbers is", add(number1, number1), ".")
            elif operation == "2":
                print ("The difference is", subtract(number1, number2),".")
            elif operation == "3":
                print ("The product is", product(number1, number2), ".")
            elif operation == "4":
                print("The answer of dividing the first number by the second number is", divide(number1, number2), ".")
    else:
        print('Invalid choice! Select a valid choice') 

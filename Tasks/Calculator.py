def add():   
    return num1 + num2 

def subtract(): 
    return num1 - num2

def product(): 
    return num1 * num2 

def divide():
    if num2 == 0:
        print("MATH ERROR!")
    else:            
        return num1 / num2 

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit the program.")

    operation = input("Enter the operation of choice (1,2,3,4,5):")
    if operation == "5":
        break 
    elif operation != "1" or "2" or "3" or "4" or "5":   
        print ("The operation is invalid.") 
    else: 
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
    
    if operation == "1":
        print ("The sum of the two numbers is", add(), ".")
    elif operation == "2":
        print ("The difference is", subtract(),".")
    elif operation == "3":
        print ("The product is", product(), ".")
    elif operation == "4":
        print("The answer of dividing the first number by the second number is", divide(), ".")

def calculation(num1, num2, symbol):
    if symbol in ["+", "-", "*", "/"]:
        if symbol == "/" and num2 == 0:  
            print("Error: number cannot be divided by 0.")
            return None 
        else:
            result = eval(f"{num1}{symbol}{num2}")
            return result
    else:
        print("Enter a correct symbol.")
        return None

calculator_on = True 
result = None

while calculator_on:
    # Check if continuing or starting fresh
    if result is None:
        # Get first number (fresh start)
        while True:
            try:
                user_num1 = input("Enter first number: ")
                num1 = float(user_num1)
                break
            except ValueError:
                print("Please enter numeric value only.")
    else:
        # Use previous result (continuing)
        num1 = result
        print(f"Continuing with: {num1}")
    
    # Input symbols 
    while True:
        symbol = input("Enter a symbol (+, *, -, /): ")
        if symbol in ["+", "-", "*", "/"]:     
            break
        else:
            print("Please input valid symbol")      
    
    # Getting second number
    while True:
        try:        
            user_num2 = input("Enter a second number: ")
            num2 = float(user_num2)
            break
        except ValueError:
            print("Please enter numeric value only.")
    
    # Calculate result
    result = calculation(num1, num2, symbol)
    
    if result is not None:
        print(f"The answer is {result}")
    
    # Ask what they want to do
    print("\nWhat would you like to do?")
    choice = input("1. Continue with this result\n2. Start fresh\n3. Exit\nEnter choice (1/2/3): ")
    
    if choice == '1':
        # Continue with current result
        # result stays as is, next iteration uses it as num1
        pass
        
    elif choice == '2':
        # Start fresh
        print(f"The result is {result} \n")
        print("New calculation")
        result = None  # Reset result so next iteration asks for first number
        
    elif choice == '3':
        # Exit
        calculator_on = False
        print("Calculator ended. Goodbye!")
        
    else:
        print("Invalid choice. Exiting.")
        calculator_on = False
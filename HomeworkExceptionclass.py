def check_age():
    try:
        # Ask the user to input their age
        age = int(input("Enter your age: "))
        
        # Check if the age is greater than 18
        if age > 18:
            print("You are above 18.")
        elif age == 18:
            print("You are exactly 18.")
        else:
            print("You are below 18.")
        
        # Check if the age is odd or even
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")
    
    except ValueError:
        # Handle the case where input is not a valid integer
        print("Invalid input. Please enter a valid integer for age.")
    
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")

# Call the function
check_age()

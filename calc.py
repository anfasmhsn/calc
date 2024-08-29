def calculate_strike_rate(total_runs, balls_faced):
    """
    Calculate and return the cricket batting strike rate.
    
    Parameters:
        total_runs (int): Total runs scored by the batsman.
        balls_faced (int): Total number of balls faced by the batsman.
    
    Returns:
        str: A message indicating the batsman's strike rate or an error message if input is invalid.
    """
    # Check if the balls faced is zero to prevent division by zero
    if balls_faced == 0:
        return "Invalid input: Balls faced cannot be zero. Please try again with a valid number of balls."
    
    # Calculate the strike rate using the formula: (Runs / Balls) * 100
    strike_rate = (total_runs / balls_faced) * 100
    
    # Return the formatted strike rate in a user-friendly message
    return strike_rate

def main():
    """
    Main function to handle user input and display the strike rate.
    """
    # Welcome message to greet the user and explain what this program does
    print("Welcome to the Cricket Batting Strike Rate Calculator!")
    print("This tool calculates a cricketer's strike rate based on the runs scored and balls faced.")
    
    try:
        # Prompt the user to enter the batsman's name
        batsman_name = input("Please enter the name of the batsman: ")
        
        # Prompt the user to enter the total runs scored
        total_runs = int(input("Please enter the total runs scored by the batsman: "))
        
        # Prompt the user to enter the number of balls faced
        balls_faced = int(input("Please enter the total number of balls faced by the batsman: "))
        
        # Calculate the strike rate using the provided values
        strike_rate = calculate_strike_rate(total_runs, balls_faced)
        
        # Check if strike rate calculation was successful
        if isinstance(strike_rate, str):
            # If strike_rate is a string, it means there was an error
            print(strike_rate)
        else:
            # Display the result to the user
            print(f"{batsman_name}'s strike rate is {strike_rate:.2f}.")
    except ValueError:
        # Handle the case where the input was not a valid integer
        print("It looks like you entered a non-integer value. Please ensure you input whole numbers for both runs and balls faced.")

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()
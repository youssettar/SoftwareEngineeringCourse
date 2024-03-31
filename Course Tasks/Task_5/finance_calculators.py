# Task 5
# CAPSTONE PROJECT
import math


# At the top of the file include the line: import math
# Write a code that allows the user to choose which calculation they want to do. 
# The first output  that the user see should look like the one below.

"""
    Investment - to calculate  the amount of interest you'll earn on your investment
    Bond       - to calculate the amount you'll have to pay on a home loan

    Enter either 'investment' or 'bond' from the menu above to proceed: 
"""

# How the user capitalises their selection should not affect how the program proceed.
# If user doesn't type in a valid input, show an appropiate error message.
# If the user selects 'investment' ask the user to input:

""" 
    1. The amount of money they are depositing.
    2. The interest rate as a percentage. (Only the number of interest without '%').
    3. The number of years the plan to invest.
    4. Ask the user if they want "simple" or "compound" interest 
      and store this in a variable called "interest".
    5 Depending on interest type "simple" or "compound" 
      output the amount they will get back after the giving period, at the specified interest rate.
    6. Print out the answer.
"""
  
# If the user selects 'bond' ask the user to imput:

"""
    1. The present value of the house.
    2. The interest rate.
    3. The number of months planned to repay the bond.
    4. Calculate how much money the user will have to repay each month and output the answer.
"""




# Menu options
option_1 = "Investment - to calculate the amount of interest you'll earn on your investment"
option_2 = "Bond       - to calculate the amount you'll have to pay on a home loan"

# Print menu options
print(option_1)
print(option_2)
print(" ")

# User input for menu options
menu_options = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
menu_options = menu_options.lower()

# User input for 'investment' option
if menu_options == "investment":
    deposit_amount = int(input("Enter the amount you would like to deposite: "))
    interest_rate = int(input("Enter the interest rate as a percentage (without %): "))
    investment_years = int(input("Enter the number of years you are planning to invest: "))
    interest = input("Would you like 'simple' or 'compound' interest?: ")
    
    # If the user choose 'simple' interest
    if interest == "simple":

        # Simple interest formula
        interest_simple = deposit_amount * (1 + (interest_rate/100)  * investment_years)
        print("Your simple interest calculation is: ", interest_simple)

    # If the user choose 'compound' interest    
    elif interest == "compound":

        # Compound interest formula
        interest_compound = deposit_amount * math.pow((1 + interest_rate/100),investment_years)
        print("Your compound interest calculation is: ", interest_compound)

    # Invalid option
    else:
        print("Invalid option. Please enter 'investment' or 'bond'.")

# User input for 'bond' option
elif menu_option_lower == "bond":
    house_value = int(input("Enter the present value of the house: "))
    interest_rate2 = int(input("Enter the interest rate: "))
    repay_months = int(input("Enter the number of months planned to repay the bond: "))

    # Monthly 'bond' repayment formula
    repayment = ((interest_rate2/100) * house_value)/(1 - (1 + interest_rate2/100)**(-repay_months))
    print("Your monthly bond repayment is: ", repayment)   

# Invalid menu option
else:
    print("Invalid option, please choose one of the availible options.")    
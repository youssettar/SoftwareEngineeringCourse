#PRACTICAL TASK 9
#TASK 1

#(SYNTAX ERROR) The function print was missing Parenthesis 
print("Welcome to the error program")

#(SYNTAX ERROR) The function print was missing Parenthesis and not aligned with the necessary order of the line
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result

#(SYNTAX ERROR) Removed extra equals sign, assigned an integer value to age_str and remove extra text "years old"
age_str = 24 
#(RUNTIME ERROR) )Used str function to convert age_str to a string
age = str(age_str) 
#(RUNTIME ERROR) Used proper string formatting with commas
print("I'm", age,  "years old.")

    # Variables declaring additional years and printing the total years of age

#(RUNTIME ERROR) Removed quotes to represent it as an integer
years_from_now = 3
#(LOGICAL ERROR) Properly performed the addition operation
total_years = age_str + years_from_now

#(SYNTAX ERROR) Corrected: Added parenthesis for print statement and correct the variable "answer_years"
print("The total number of years:", total_years)


    # Variable to calculate the total amount of months from the total amount of years and printing the result

#(LOGICAL ERROR) Added the 6 months missing in the equation and parentheses to ensure proper order of operations 
total_months = (total_years * 12) + 6
#(SYNTAX AND RUNTIME ERROR) Used proper string concatenation and added missing print statement
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
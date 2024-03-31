#PRACTICAL TASK 9
#TASK 2


#WRITE A PROGRAM THAT DISPLAYS A 'LOGICAL ERROR'

"""
I PLAN TO DEVELOP A FIVE-YEAR INVESTMENT PROGRAM WITH THE AIM OF AGGREGATING FUNDS FOR THE "BUSNI" GROUP OF FRIENDS.
EACH OF THE 12 FRIENDS IS EXPECTED TO CONTRIBUTE TO A COLLECTIVE "KULNI" POT ON A MONTHLY BASIS.
THE ACCUMULATED FUNDS WILL BE UTILIZED TO CONSTRUCT A SHARED COUNTRYSIDE HOUSE, 
PROVIDING A SPACE WHERE ALL FAMILIES CAN GATHER AND ENJOY TIME TOGETHER.
"""

# MAKE A LIST OF FRIENDS
# MAKE A LIST OF MONTHS
# DISPLAY WELCOME MESSAGE
# INITIALIZE AN EMPTY LIST TO STORE MONTHLY INVESTMENTS
# INITIALIZE AN EMPTY LIST TO STORE EACH FRIEND'S INVESTMENT
# MAKE AN INPUT FOR EACH FRIEND AND ASK HOW MUCH THEY WILL INVEST FOR THE MONTH
# PRINT THE TOTAL RESULT OF EACH MONTH INCLUDING THE AMOUNT INVESTED OF EACH FRIEND
# STORE THE MONTHLY TOTAL INVESTMENT FOR A YEAR AND PRINT RESULTS
# ASK THE USER IF THEY WANT TO SEE THE AVERAGE INVESTMENT TOTAL IN 5 YEARS
# IF THE USER SELECTS 'NO' FINISH THE CALCULATION WITH A MESSAGE




# NAME OF FRIENDS
name_1 = "Youssef"
name_2 = "Monika"
name_3 = "Bilal"
name_4 = "Mazin"
name_5 = "Zayn"
name_6 = "Tanja"
name_7 = "Agne"
name_8 = "Yassin"
name_9 = "Younes"
name_10 = "Hardon"
name_11 = "Manito"
name_12 = "Krimo"

# FRIENDS LIST
friends = [
    name_1, name_2, name_3, name_4, name_5, name_6, 
    name_7, name_8, name_9, name_10,name_11, name_12
]

# WELCOME MESSAGE
print("\n!!!HAPPY DAY 'BUSNI' FAMILY AND WELCOME TO YOUR INVESTMENT TRACKER!!!\n")
print("Each one of the club members will be called by His/Hers personal name,\nPlease follow further instructions. \n")

# MONTH NAMES LIST
month_names = [
    "January", "February", "March", "April", "May", "June",
     "July", "August", "September", "October", "November", "December"
]

# LIST TO STORE MONTHLY INVESTMENT
kulni_pot_monthly = []

# LOOP THROUGH EACH MONTH
"""
THE LOGICAL ERROR IN HERE IS THE RANGE SELECTION. RANGE SHOULD BE BETWEEN (1, 13) INSTEAD OF (0. 12)
THE SYSTEM WILL ONLY PRINT 11 NAMES OF THE LIST OF FRIENDS INSTEAD OF 12
THE CORRECT CODE SHOULD BE AS THE FOLLOWING:
for month_input in range(1, 13):
"""

for month_input in range(0, 12):
    print(f"===== Month {month_names[month_input-1]} ====== \n")
    
    # DICTIONARY TO STORE INVESTMENT FOR EACH FRIEND
    month_investment = {}

    # LOOP THROUGH EACH FRIEND TO GET INVESTMENT
    for friend_name in friends:
        investment = float(input(f"Dear {friend_name}. I hope you are doing great today! \nPlease provide the amount you willing to invest this month: \n"))
        month_investment[friend_name] = investment
        print(" ")

    # CALCULATE TOTAL MONTHLY INVESTMENT   
    total_month_investment = sum(month_investment.values())  

    # DISPLAY MONTHLY INVESTMENT
    print(f"Dear BUSNI Family, Your total investment for the month {month_names[month_input-1]} is: {total_month_investment}")      
    print("Keep the good work and remember, 'The struggle of todays, is the Glory of tomorrow!'\n")

    #APPEND TOTAL INVESTMENT TO THE LIST
   
    kulni_pot_monthly.append(total_month_investment)

# DISPLAY TOTAL YEARLY INVESTMENT
print("===== TOTAL INVESTMENT FOR THE YEAR =====\n")
kulni_pot_yearly = sum(kulni_pot_monthly)
print(f"Dear BUSNI Family, the Total yearly amount invested this year is: {kulni_pot_yearly}")
print("Great results so far!!! Keep up the hard work and stay motivated!\nHappy new year and more success in this new chapter!\n")

# ASK FOR 5-YEAR AVERAGE INVESTMENT
user_input = input("If you would like to see the average Total investment in 5 years, please write 'yes'. If not, just type 'no':\n")
user_input = user_input.lower()

# DISPLAY 5-YEAR AVERAGE IF REQUESTED
if user_input == "yes":
    print(f"\nYour estimated 5 years investment Total is: {kulni_pot_yearly * 5}")

else:
    print("\nNo worries, I hope you have a wonderful day.\nThank you for using the BUSNI Family Investment Tracker.")
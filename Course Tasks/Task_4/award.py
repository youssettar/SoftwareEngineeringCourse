#PRACTICAL TASK 3
#TASK_1


#Get the times (in minutes) for swimming, cycling and running
#Calculate the total time for Trianthlon
#Determine the award based on the total time
#TIME RANGE:   0 - 100      AWARD = Provincial Colours
#TIME RANGE: 101 - 105      AWARD = Provincial Half Colours
#TIME RANGE: 106 - 110      AWARD = Provincial  Scroll
#TIME RANGE: 111+           AWARD = NO AWARD

# Prompting the user to enter swimming time (in minutes)
swimming_time = int(input("Enter swimming time (in minutes): "))

# Prompting the user to enter cycling time (in minutes)
cycling_time = int(input("Enter cycling time (in minutes): "))

# Prompting the user to enter running time (in minutes)
running_time = int(input("Enter running time (in minutes): "))

# Calculating the total time by summing swimming, cycling, and running times
total_time = swimming_time + cycling_time + running_time

# Checking if the total time qualifies for Provincial Colours award
if total_time <= 100:
    print("Provincial Colours")

# Checking if the total time qualifies for Provincial Half award
elif 101 <= total_time <= 105:
    print("Provincial Half")

# Checking if the total time qualifies for Provincial Scroll award
elif 106 <= total_time <= 110:
    print("Provincial Scroll")

# If none of the conditions above are met, no award is printed
else:
    print("No award")

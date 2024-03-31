#PRACTICAL TASK 3
#TASK_1


#Get the times (in minutes) for swimming, cycling and running
#Calculate the total time for Trianthlon
#Determine the award based on the total time
#TIME RANGE:   0 - 100      AWARD = Provincial Colours
#TIME RANGE: 101 - 105      AWARD = Provincial Half Colours
#TIME RANGE: 106 - 110      AWARD = Provincial  Scroll
#TIME RANGE: 111+           AWARD = NO AWARD

swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

total_time = swimming_time + cycling_time + running_time


if total_time <= 100:
    print("Provincial Colours")

elif 101 <= total_time <= 105:
    print("Provincial Half")

elif 106 <= total_time <= 110:
    print("Provincial Scroll")

else:
    print("No award")
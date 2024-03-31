#PRACTICAL TASK 3
#TASK_1


#Create an integer variable and name it "age"
#Use if-elif-else to create the program
#Set up the conditions in the right order

age = int(input("What is your age? "))

if age > 100:
    print("Sorry, you're dead.")  

elif age >= 65:
    print("Enjoy your retirement!")

elif age >= 40:
    print("You're over the hill.")

elif age == 21:
    print("Congrats on your 21st")   

elif age < 13:
    print("You qualify for the kiddie discount.")

else:
    print("Age is but a number.")     
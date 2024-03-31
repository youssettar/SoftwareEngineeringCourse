#PRACTICAL TASK 7


#Write a program that continually asks user to enter a number
#When the user enters "-1", the program should stop requesting the user to enter a number
#The program must then calculate the average of the numbers entered excluding the -1
#Make use of the while loop repetition structure to implement the program


#Avarage count Variables
total = 0
count = 0

#Ask user to imput number
number_input = int(input("Please enter a number: "))

#While loop if number doesn't meet condition
while number_input != -1:
    
    #Avarage count sum
    total += int(number_input)
    count += 1

    #Ask user to input number again
    number_input = int(input("Please enter a number: "))


#When number meet condition
if number_input == -1:

    #Average count total
    average_count_total = total / count
    print("The avarage of the numbers entered excluding (-1) is: ", average_count_total)

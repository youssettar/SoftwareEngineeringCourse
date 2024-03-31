#PRACTICAL TASK 14


""" 
Write a program that reads the data from the text file provided (DOB.txt) 
and prints it out in two different sections in the format displayed below:
"""

# Name
# Orville Wright
# Rogelio Holloway
# Marjorie Figueroa
# ...etc

# Birthdate
# 21 July 1988
# 13 September 1988
# 9 October 1988
# ...etc.

""" 
- Remember to ensure that the text folder is in the appropiate file directory
    or python won't be able to find it when running the program. 
- Get this right first by running the example files, and do the task
"""



# Open the file from stored carpet and read lines
with open(r'C:\Users\admin\Desktop\Software Engineering Course\Course Tasks\Task_14\dob.txt', 'r') as file:
    lines = file.readlines()

# Lists of Names and Birthdates
names = []
birthdates = []

for line in lines:

    # Split each line into name and birthdate
    parts = line.strip().split(', ')
    names.append(parts[0])
    birthdates.append(parts[1])

# Print names
print("Name")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)

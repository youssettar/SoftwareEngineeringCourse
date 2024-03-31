#PRACTICAL TASK 8

"""
Write code to output the star pattern shown below, using an 'if-else' statement in combination 
with a single 'for' loop 

*
**
***
****
*****
****
***
**
*
"""


#Number of rows
rows = 5 

# Loop through values from 1 to double the number of rows
for value in range(1, 2 * rows):

    #While value is less or equal to rows
    if value <= rows:
        print('*' * value)
        
    #shrinking formula when the condition of 'if' is met
    else:
        print('*' * (2 * rows - value))

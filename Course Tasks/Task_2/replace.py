#PRACTICAL TASK 2
#TASK_2


#Create the sentance ("The!quick!brown!fox!jumps!over!the!lazy!dog.")
#Reprint the sentance using (replace()) function
#Reprint the sentance using (upper()) function
#Reprint the sentance in reverse

sentance = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentance.replace('!' , ' '))

sentance_upper = sentance.replace('!' , ' ').upper()
print(sentance_upper)

sentance_reverse = sentance_upper[::-1]
print(sentance_reverse)

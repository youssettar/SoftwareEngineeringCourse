# PRACTICAL TASK 12


# Create a list called 'menu', which should contain at least four items sold in the cafe.
# Create a dictionary called 'stock',which should contain the stock value for each item on your menu.
# Create another called 'price', which should contain the prices for each item on your menu.
# Calculate the 'total_stock' worth in the cafe.You will need to remember to loop through the appropiate dictoiinaries and lists to do this.
""" TIP: When you loop through the menu list, the 'items' can be set as keys to access the corresponding 'stock' and 'price' values.
 Each 'item_value' is calculated by multiplying the stock value by the price value. For example: 
 item_value = (stock[items] * price[items])"""
# Finally, print out the result of your calculation.


# 'menu' List with four items sold in the cafe
menu = ["Coffee", 
        "Pastries", 
        "Shake", 
        "Sandwishes"
]

# 'stock' Dictionary with stock values for each item on the menu
stock = {"Coffee": 120, 
         "Pastries": 75, 
         "Shake": 40, 
         "Sandwishes": 25
}

# 'price' Dictionary with prices for each item on the menu
price = {"Coffee": 2.50, 
         "Pastries": 1.75, 
         "Shake": 4.00, 
         "Sandwishes": 5.00
}

# Calculate the total_stock worth in the cafe
total_stock = 0

# Loop through the menu list to calculate the total value of the cafe's stock
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# Print out the result of the calculation
print(f"The total stock worth in the cafe is: {total_stock:}")
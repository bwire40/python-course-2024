# Tip calculator app
# total=100
# tip=20 per cent
# total payment

# math operators +, -, /, *, **, //, %


# food_amount = 100
# tip_percent = 20 / 100
# tip_amount = food_amount * tip_percent
# total_amount = food_amount + tip_amount
# print("$" + str(total_amount))
#

# use inputs make it dynamic
food_amount = int(input("Enter food amount: "))
tip_percent = int(input("Enter the tip percentage: "))/100
tip_amount = food_amount * tip_percent
total_amount = food_amount + tip_amount
print("$" + str(total_amount))


# Tip calculator app

# add functions

# total=100
# tip=20 per cent
# total payment

# math operators +, -, /, *, **, //, %


# food_amount = 100
# tip_percent = 20 / 100
# tip_amount = food_amount * tip_percent
# total_amount = food_amount + tip_amount
# print("$" + str(total_amount))

# def calculate_tip(f_amount, t_percent):
#     """
#
#     :param f_amount:
#     :param t_percent:
#     :returns the tip_amount:
#     """
#     return f_amount * t_percent


# use inputs make it dynamic
food_amount = int(input("Enter food amount: "))
tip_percent = int(input("Enter the tip percentage: "))

print("********************************************")


def calculate_food_total(f_amount, t_percentage):
    """

    :param f_amount:
    :param t_percentage:
    :returns the total amount by adding food and tip amount:
    """
    tip_amount = food_amount * (t_percentage / 100)

    return f_amount + tip_amount


total = calculate_food_total(food_amount, tip_percent)

print(total)

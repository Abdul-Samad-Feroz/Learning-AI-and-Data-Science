def calculatePercentage():  # Define Function
    marks = 400
    percentage = marks / 500 * 100
    print(percentage)


calculatePercentage()

# Create a function named show_welcome
# that displays Welcome to our school!.
# Call it twice.
# Create another function named
# show_rules that displays three classroom rules.
# Call show_rules() before show_welcome()
# and observe the output order.


def show_welcome():
    print("Welcome to our school!")


def show_rules():
    print("Take permision before entering in classroom!")
    print("Do not eat while lecture!")
    print("Do not misbehave with instuctors!")


show_rules()
show_welcome()
show_welcome()


def calculate_percentage(marks):  # Marks is a parameter
    percentage = marks / 500 * 100
    print(percentage)


calculate_percentage(380)


def calculate_percentage(marks, total):  # Marks is a parameter
    percentage = marks / total * 100
    print(percentage)


calculate_percentage(440, 500)


def calculate_total(price, quantity):
    totalCost = price * quantity
    print(f"Total Cost = {totalCost}")


calculate_total(1000, 3)

# write check_temperature(temperature).
# Below 20: display Cold.
# From 20 through 30: display Comfortable.
# Above 30: display Hot.


def check_temprature(temprature):
    if temprature < 20:
        print("Cold")
    elif temprature >= 20 and temprature <= 30:
        print("comfortable")
    else:
        print("Hot")


check_temprature(29)

balance = float(input("Enter Account balance: "))
w_amount = float(input("Enter Withdrawal amount: "))

if w_amount > balance:
    print("Insufficient Balance")
elif balance - w_amount < 1000:
    print("You have withdrawn Rs.", w_amount)
    print("Low Balance")
else:
    print("You have withdrawn Rs.", w_amount)
    print("Transaction Successful")


age = int(input("Enter Your age: "))
ticket = input("Did you have a valid ticket? ")

if age >= 18 and (ticket == "yes" or ticket == "Yes"):
    print("Entry Allowed")
else:
    print("Entry denied")


# Nested comparison Operator
user_age = int(input("Enter Your age: "))

if user_age >= 18:
    user_ticket = input("Did you have a valid ticket? ")
    if user_ticket == "yes" or user_ticket == "Yes":
        print("Entry Allowed")
    else:
        print("Buy a ticket")


else:
    print("You are underage")

driver_age = int(input("Enter Your age: "))

if driver_age >= 18:
    driver_licence = input("Did you have passed driving test? ")
    if driver_licence == "yes" or driver_licence == "Yes":
        print("Licence can be issued")
    else:
        print("You need to pass the test")

else:
    print("You can not apply for driving licence")


p_course = input("Have you completed prerequsite course? ")
if p_course == "yes" or p_course == "Yes":
    fees = input("Have you paid your fees? ")
    if fees == "yes" or fees == "Yes":
        print("Enrollment Successful")
    else:
        print("Please Pay your fees")

else:
    print("Please complete prerequisite course")


p_age = int(input("Enter your age: "))

if p_age >= 18:
    passport = input("Do you have a valid passport? ")
    if passport == "yes" or passport == "Yes":
        ticket = input("Do you have valid Ticket? ")
        if ticket == "yes" or ticket == "Yes":
            luggage = input("Do you excess luggage? ")
            if luggage == "yes" or luggage == "Yes":
                print("Extra luggage fees required")
            else:
                print("Check in successful")
        else:
            print("Ticket Required")
    else:
        print("Passport Required")

else:
    print("Age verification required")

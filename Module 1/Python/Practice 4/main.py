def create_profile(name, age, city, course):
    print(name)
    print(age)
    print(city)
    print(course)


# positional arguments
create_profile("Abdul Samad Feroz", 16, "Karachi", "AI & DS")
# keyword arguments
create_profile(name="Abdul Samad Feroz", age=16, course="AI & DS", city="Karachi")


def calculate_result(name, english, maths, science):
    total = english + maths + science
    percentage = total / 300 * 100
    print(f"Student: {name}")
    print(f"Total: {total}")
    print(f"Percentage: {percentage}")


calculate_result(name="Faisal", english=87, maths=78, science=98)
calculate_result("Imran", 88, 95, 86)

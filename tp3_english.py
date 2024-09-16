age = int(input("Enter your age: "))  # age input
eligibility = ""  # scholarship eligibility is set through this variable, currently empty

if age < 18:  # checks if age is lesser than 18
    eligibility = "not eligible"
else:
    average = float(input("Enter your average: "))
    if average < 10:  # this is ignored if q2 is = to yes
        eligibility = "not eligible"
    elif 10 <= average < 12:  # checks if student does extracurricular activities
        eligibility = "eligible but under review"
    q1 = input("Do you participate in extracurricular activities? (yes/no): ").lower()
    if q1 == "yes":
        eligibility = "eligible"
    else:  # low income families are prioritized for scholarships
        q2 = input("Do you come from a low-income family? (yes/no): ").lower()
        if q2 == "yes":
            eligibility = "eligible"
        else:
            print(" ")  # for spacing

if eligibility == "eligible":  # checks final eligibility
    print("You are eligible for a scholarship!")

elif eligibility == "eligible but under review":
    print("You are technically eligible but further checks are required...")
    print("Consider trying out extracurriculars")  # extracurriculars are highly valued for scholarships

else:
    print("You are not eligible for the scholarship")

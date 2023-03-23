print("Welcome to the tip calculator!")
bill = float(input("What was the total bill without tax? $"))
tip_percent = int(input("How much tip would you like to give? 10, 15 or 20: "))
number_of_people = int(input("How many people are going ot split the bill? "))
tax = bill * .1
bill_with_tip_tax = bill * ((tip_percent * .01) + 1) + tax
each_pays = bill_with_tip_tax/number_of_people
print(f"Each person should pay: ${round(each_pays, 2)}")
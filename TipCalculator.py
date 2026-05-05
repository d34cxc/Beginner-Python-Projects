#Just a simple tip calculator created with python.

bill_amount = float(input("Please enter the bill amount: $"))
tip_amount = int(input("Please enter the percentage you'd like to tip: "))
tip_value = tip_amount / 100
tipped_value = tip_value * bill_amount
response = "The tip you'd like leave is: $" + str(tipped_value)
total = bill_amount + tipped_value

print("Tip: $" + str(round(tipped_value, 2)))
print("Total: $" + str(round(total, 2)))

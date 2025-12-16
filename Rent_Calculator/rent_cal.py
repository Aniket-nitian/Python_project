rent = int(input("Enter your monthly rent amount: "))
food = int(input("Enter your food expenses: "))
el_units = int(input("Enter your electricity units consumed: "))
el_rate = int(input("Enter electricity per unit rate: "))
total_person = int(input("Number of person sharing flat: "))

total_amount = rent + food + (el_units * el_rate )
amount_per_person = total_amount / total_person

print(" Total amount to be paid: ", total_amount)
print(" Amount to be paid per person: ", amount_per_person)



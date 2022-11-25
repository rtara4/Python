print("Account Interest Calculator")
print("---------------------------")
print()

starting_balance = float(input("Please enter the starting balance> £"))
final_balance = float(input("Please enter the final balance> £"))
interest_rate = float(input("Please enter the interest rate> "))

current_balance = starting_balance
month = 1

print("Month\tBalance (£)")

while current_balance < final_balance:
    current_balance = (current_balance * interest_rate) / 100.0

        
print()
print("It will take " + str(month) + " months to achieve the balance £" + "{:.2f}".format(final_balance))

amount_owed = float(input("How much do you owe?: \n "))
interest_rate = float(input("What is your annual interest rate?:\n "))
payment = float(input("How much are you able to pay each month?:\n "))
months = int(input("How many months of results do you want to see?\n "))

monthly_interest_rate = interest_rate / 100 / 12

for i in range(months):

    paid = amount_owed * monthly_interest_rate

    amount_owed = amount_owed + paid

    if(amount_owed - payment < 0):
        print("The last payment is: ", amount_owed)
        print("You paid off the loan in: ", i+1, "months\n")
        break

    amount_owed = amount_owed - payment

    print("Paid: ", payment, "out of which", paid, "was interest\n")
    print("Now you owe: ", amount_owed)

bill = float(input("enter the bill amount: $"))
tip = int(input("what percent of tip you would like to give? 10, 12 or 15?")) 
people = int(input("how many people split the bill?"))

total_tip_amount = (tip / 100) * bill
bill_with_tip = (tip / 100) * bill + bill
bill_each = bill_with_tip / people

bill_each = "{:.2f}".format(bill_each)
print(f"Each of you should pay: ${bill_each}")
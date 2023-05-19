print("Welcome to the tip calculator.")

total_bill = float(input("Whata was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

total_people = int(input("How many people to split the bill? "))


bill_and_tip = total_bill * (1 + percentage_tip) 
share_price = bill_and_tip / total_people

print(f"Each person should pay: ${round(share_price, 2)}")
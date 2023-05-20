from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
person_for_bid = {}

end_for_bid = False

while not end_for_bid:
    name = input("What is your name?: ")
    price_for_bid = int(input("What's your bid?: $"))

    person_for_bid[name] = price_for_bid

    people_remain = input("Are there any other bidders? Type 'yes' or 'on'.\n").lower()
    clear()
    
    if people_remain == "no":
        # 可以把下面的寫成一個function
        max_bid = -1
        win_person = ""
        for person in person_for_bid:
            if person_for_bid[person] > max_bid:
                max_bid = person_for_bid[person]
                win_person = person
        print(f"The winner is {win_person} with a bid of ${max_bid}.")
        end_for_bid = True
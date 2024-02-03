### Main file for the Fast Recipt Scanner Software

# Importing the required libraries
import numpy as np
from datetime import datetime, timedelta


def make_recipt(card_number, items):
    # make recipt
    recipt = {
        "message": "Takk for at du handler på Rapido!",
        "student_card_number": card_number,
        "items": items,
        "valid_until": datetime.now() + timedelta(minutes=10)
    }

    return recipt

def make_old_recipt(card_number, items):
    # make recipt
    recipt = {
        "student_card_number": card_number,
        "items": items,
        "valid_until": datetime.now() + timedelta(minutes=10)
    }

    return recipt

def print_recipt(recipt):
    # Printing the message and student card number
    print(recipt['message'] if 'message' in recipt else "")
    print(f"Student Card Number: {recipt['student_card_number']}")

    # Printing each item in the purchase
    print("Items Purchased:")
    for item in recipt['items']:
        print(f" - {item['name']}: {item['price']} NOK")

    # Printing the validity
    valid_until = recipt['valid_until'].strftime('%Y-%m-%d %H:%M:%S')
    print(f"Valid Until: {valid_until}")


def check_if_valid(recipt):
    # Check if the recipt is still valid
    return recipt['valid_until'] > datetime.now()

# Main function
def main():
    # read
    #card_number = read_rfid()
    print("starting")
    card_number = "1234567890"

    items_1 = [
        {
            "name": "Iskaffe",
            "price": 18.90
        },
        {
            "name": "Kanelbolle",
            "price": 23.90
        }
    ]

    items_2 = [
        {
            "name": "Kaffe",
            "price": 12.90
        },
        {
            "name": "Red Bull",
            "price": 33.90
        }
    ]

    items_3 = [
        {
            "name": "baguette",
            "price": 12.90
        },
        {
            "name": "Coca Cola Zero",
            "price": 28.90
        },
        {
            "name": "Litago sjokolademelk",
            "price": 23.90
        },
    ]

    recipt = make_recipt(card_number, items_1)
    print_recipt(recipt)

    # check if recipt is valid
    print(f"is_valid: {check_if_valid(recipt)}")

    print("dine tidligere kjøp:")
    recipt2 = make_old_recipt(card_number, items_2)
    print("")
    recipt3 = make_old_recipt(card_number, items_3)
    print_recipt(recipt2)
    print_recipt(recipt3)
    print("done")

# Run the main function
if __name__ == "__main__":
    main()  
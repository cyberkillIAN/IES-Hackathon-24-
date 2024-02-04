import serial
from datetime import datetime, timedelta

# Open the serial port
ser = serial.Serial('COM5', 9600)  # Update the serial port and baud rate as needed
ser.flush()

def read_rfid():
    # Read data from the serial port
    """data = ser.readline().strip().decode('utf-8')  # Decode the bytes to string
    return data"""
    # Read data from the serial port
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            # Check if line contains "In dec:"
            if "In dec:" in line:
                # Extract the decimal values
                dec_values = line.split("In dec: ")[1]
                print(f"Card Number (Decimal): {dec_values}")
                return dec_values
                
            

def make_receipt(card_number, items):
    # Create a receipt with the provided data
    receipt = {
        "message": "Takk for at du handler på Rapido!",
        "student_card_number": card_number,
        "items": items,
        "valid_until": datetime.now() + timedelta(minutes=10)
    }
    return receipt

def print_receipt(receipt):
    # Printing the message and student card number
    print(receipt['message'] if 'message' in receipt else "")
    print(f"Student Card Number: {receipt['student_card_number']}")

    # Printing each item in the purchase
    print("Items Purchased:")
    for item in receipt['items']:
        print(f" - {item['name']}: {item['price']} NOK")

    # Printing the validity
    valid_until = receipt['valid_until'].strftime('%Y-%m-%d %H:%M:%S')
    print(f"Valid Until: {valid_until}")

def PaaVeiUt(receipt):
    card_number = read_rfid()
    if card_number == receipt["student_card_number"]:
        print ("Godkjent du kan passere")
    else:
        print("Du har ikke betalt")


# Main function
def main():
    # Read RFID data from the Arduino
        card_number = read_rfid()
        print(card_number)

        # Example items for the receipt
        items_1 = [
            {"name": "Iskaffe", "price": 18.90},
            {"name": "Kanelbolle", "price": 23.90}
        ]

        # Create a receipt with the RFID data and items
        receipt = make_receipt(card_number, items_1)

        # Print the receipt
        print_receipt(receipt)

        # Close the serial port
        ser.close()

        PaaVeiUt(receipt) # riktig kort

        ser.close()

        PaaVeiUt(receipt) # feil kort

        ser. close()
# Run the main function
if __name__ == "__main__":
    main()

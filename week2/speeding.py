

def speeding_ticket(speed, is_birthday):
   
    if is_birthday :
        speed -= 5
    if speed <= 60 :
        return ("No Ticket")
    elif 61 <=speed <= 80 :
        return ("Small Ticket")
    else :
        return ("Big Ticket")
    
speed = int(input("Speed: "))
is_birthday = input("Is it the driver's birthday? (yes/no): ").lower() == "yes"
print (speeding_ticket(speed, is_birthday))



# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"
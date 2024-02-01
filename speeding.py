"""
Speeding Ticket Function

Objective:
Write a function named 'speeding_ticket' that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

Function Parameters:
1. speed (integer): The driver's speed in mph (miles per hour).
2. is_birthday (boolean): A flag indicating whether the driver is driving on their birthday.

Instructions:
- The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
- If the driver's speed is 60 mph or less, they should receive "No Ticket".
- If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
- If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
- On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if is_birthday is True.

Example Test Cases:
1. speeding_ticket(60, False) should return "No Ticket".
2. speeding_ticket(75, False) should return "Small Ticket".
3. speeding_ticket(85, False) should return "Big Ticket".
4. speeding_ticket(65, True) should return "No Ticket".
5. speeding_ticket(85, True) should return "Small Ticket".
"""


def speeding_ticket(speed, is_birthday):
   No_Ticket_limit = 60
   Small_Ticket_limit = 80 
   
   if is_birthday:
       No_Ticket_limit += 5
       Small_Ticket_limit += 5
       
       if speed < 60:
        return "No Ticket"
       elif 60 <= speed <= 80:
           return "Small Ticket"
       else:
           return "Big Ticket"
       
speed_input = int(input("Enter the speed: "))
birthday_input = input("Is it the driver's birthay('yes' or 'no')")      

is_birthday =  birthday_input == 'yes'

result = speeding_ticket(speed_input, is_birthday)

print ("Result", result)
        
   
       

       
       
   


# Test cases
speeding_ticket(60, False)  # Expected output: "No Ticket"
speeding_ticket(75, False)  # Expected output: "Small Ticket"
speeding_ticket(85, False)  # Expected output: "Big Ticket"
speeding_ticket(65, True)  # Expected output: "No Ticket"
speeding_ticket(85, True)  # Expected output: "Small Ticket"

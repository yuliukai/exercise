def case_counter(text):
   
    text = input ("Enter your word: ")
   
 uppercase_count = 0
    lowercase_count = 0
    
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)
            
   

# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0

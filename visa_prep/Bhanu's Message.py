import re
def validate_number(number):
    if len(number) == 10 and number.isdigit():
        print("Correct")
        return
    pattern = r'^\+(\d{1,2})\s(\d{10})$'   
    match = re.match(pattern, number)
    if match:
        country_code = match.group(1)
        digits = match.group(2)
        if sum(int(digit) for digit in digits) > 0:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
number = input().strip()
validate_number(number)    
    

# Making a calculator which calculate root values up to user's input decimal places by 'Binomial theorem'.

def root_calculator(x, n, no_of_decimal_place, common_no):
    final_value = common_no
    current_value = common_no
    
    # This loop runs to add all the terms
    for k in range(1, no_of_decimal_place):
        current_value = current_value * ((n - k + 1) / k * x)
        final_value += current_value
        
    # Returning the final formatted value
    return f"{final_value:.{no_of_decimal_place}f}" 

# Taking inputs and converting them into mathematical numbers/fractions
user_x = eval(input("Enter the value of x (e.g., -4/125): "))
user_n = eval(input("Enter the value of n (e.g., 1/3): "))
user_terms = int(input("Enter number of terms/decimal places: "))
user_common = float(input("Enter the number taken as common: "))

# Printing the final result 
result = root_calculator(user_x, user_n, user_terms, user_common)    
print(result)

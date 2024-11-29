# Question 1
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Example 
original_price = 100.0
discount = 15.0
final_price = calculate_discount(original_price, discount)
print(f"The final price is: {final_price}")

# Question 2
# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for the price and discount.")
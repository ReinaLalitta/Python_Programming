def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage (0-100)
        
    Returns:
        float: Final price after applying discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage (0-100): "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount)
    
    # Print the result
    if discount >= 20:
        print(f"Original price: ${original_price:.2f}")
        print(f"Discount applied: {discount}%")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount.")
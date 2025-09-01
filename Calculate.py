# Predefined values (input simulation)
original_price = 5000.0       # price of the item
discount_percentage = 25.0    # discount percentage

# Validate negative values
if original_price < 0 or discount_percentage < 0:
    print("❌ Error: Values cannot be negative.")
else:
    if discount_percentage >= 20:
        discount_amount = original_price * discount_percentage / 100
        final_price = original_price - discount_amount
    else:
        discount_amount = 0
        final_price = original_price

    # Display results in a table
    print("\n================ RESULT =================")
    print(f"{'Original Price':<20}: {original_price:>10.2f} MT")
    print(f"{'Discount (%)':<20}: {discount_percentage:>10.2f} %")
    print(f"{'Discount Amount':<20}: {discount_amount:>10.2f} MT")
    print(f"{'Final Price':<20}: {final_price:>10.2f} MT")
    print("========================================\n")

    if discount_percentage < 20:
        print("ℹ️ Discount less than 20%, not applied.")

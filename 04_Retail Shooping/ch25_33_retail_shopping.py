# Retail Shopping Application – Coding Challenges 25 to 33

items = []
grand_total = 0
total_quantity = 0

PROMO_CODE = "PROMO10"

print("=== Retail Shopping Application ===")

# -------- Challenge 25 & 26: Item Entry and Grand Total --------
while True:
    code = input("\nEnter Item Code: ")
    description = input("Enter Item Description: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit (₹): "))

    item_total = quantity * price

    # -------- Challenge 30: Promotional Discount --------
    promo_discount = 0
    if code == PROMO_CODE:
        promo_discount = 0.10 * item_total
        item_total -= promo_discount

    items.append({
        "code": code,
        "description": description,
        "quantity": quantity,
        "price": price,
        "promo_discount": promo_discount,
        "total": item_total
    })

    grand_total += item_total
    total_quantity += quantity

    print(f"Item Total: ₹{item_total:.2f}")

    choice = input("Add another item? (y/n): ").lower()
    if choice != 'y':
        break

print("\nInitial Grand Total: ₹", round(grand_total, 2))

# -------- Challenge 27: Discounts --------
discount = 0

if grand_total > 10000:
    discount += 0.10 * grand_total

if total_quantity > 20:
    discount += 0.05 * (grand_total - discount)

grand_total -= discount

print(f"Total Discount Applied: ₹{discount:.2f}")
print(f"Amount After Discounts: ₹{grand_total:.2f}")

# -------- Challenge 28: Membership Discount --------
member = input("\nAre you a member? (y/n): ").lower()
membership_discount = 0

if member == 'y':
    membership_discount = 0.02 * grand_total
    grand_total -= membership_discount

print(f"Membership Discount: ₹{membership_discount:.2f}")
print(f"Amount After Membership Discount: ₹{grand_total:.2f}")

# -------- Challenge 29: Tax Calculation --------
tax = 0

if grand_total < 5000:
    tax = 0.05 * grand_total
elif grand_total <= 20000:
    tax = 0.10 * grand_total
else:
    tax = 0.15 * grand_total

grand_total += tax

print(f"Tax Applied: ₹{tax:.2f}")
print(f"Amount After Tax: ₹{grand_total:.2f}")

# -------- Challenge 31: Payment Mode --------
payment_mode = input("\nSelect Payment Mode (Cash/Credit): ").lower()
surcharge = 0

if payment_mode == "credit":
    surcharge = 0.02 * grand_total
    grand_total += surcharge

print(f"Surcharge: ₹{surcharge:.2f}")
print(f"Final Payable Amount: ₹{grand_total:.2f}")

# -------- Challenge 32: Minimum Purchase Check --------
if grand_total < 500:
    print("\n❌ Minimum purchase of ₹500 not met. Invoice cannot be generated.")
    exit()

# -------- Challenge 33: Loyalty Points --------
loyalty_points = int(grand_total // 100)

# -------- Invoice Display --------
print("\n========== FINAL INVOICE ==========")
for item in items:
    print(f"{item['description']} | Qty: {item['quantity']} | Total: ₹{item['total']:.2f}")

print("----------------------------------")
print(f"Total Quantity: {total_quantity}")
print(f"Final Amount Payable: ₹{grand_total:.2f}")
print(f"Loyalty Points Earned: {loyalty_points}")
print("==================================")

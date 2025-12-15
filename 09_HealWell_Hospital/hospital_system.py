import datetime

# Global Data (Simulating Database) - Level 7 Init
services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

def display_services():
    print("\nAvailable Services:")
    for i, (svc, cost) in enumerate(zip(services, costs)):
        print(f"{i+1}. {svc} (Rs. {cost})")

def admin_mode():
    print("\n--- Admin Mode: Setup Services ---")
    while True:
        display_services()
        print("\nOptions: 1. Add Service, 2. Update Cost, 3. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter Service Name: ")
            try:
                cost = float(input("Enter Cost: "))
                services.append(name)
                costs.append(cost)
                print("Service added successfully.")
            except ValueError:
                print("Invalid cost.")
        elif choice == '2':
            try:
                idx = int(input("Enter Service ID (Number) to update: ")) - 1
                if 0 <= idx < len(services):
                    new_cost = float(input(f"Enter new cost for {services[idx]}: "))
                    costs[idx] = new_cost
                    print("Cost updated.")
                else:
                    print("Invalid Service ID.")
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def patient_mode():
    print("\n--- Patient Registration & Billing ---")
    
    # Level 1: Patient Details
    print("Enter Patient Details:")
    name = input("Name: ")
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid Age. Defaulting to 30.")
        age = 30
    gender = input("Gender: ")
    contact = input("Contact: ")
    
    # Level 2: Display & Select Services
    display_services()
    selected_indices = []
    print("\nEnter Service Numbers to select (comma separated, e.g., 1,4):")
    selection_str = input("Selection: ")
    
    try:
        parts = selection_str.split(',')
        for p in parts:
            idx = int(p.strip()) - 1
            if 0 <= idx < len(services):
                selected_indices.append(idx)
            else:
                print(f"Warning: Service ID {p} is invalid. Ignoring.")
    except ValueError:
        print("Invalid input format.")
        return

    if not selected_indices:
        print("No valid services selected. Aborting.")
        return

    # Level 3: Fetch Costs
    selected_services_names = [services[i] for i in selected_indices]
    selected_costs = [costs[i] for i in selected_indices]
    
    # Level 4: Total Cost
    subtotal = sum(selected_costs)
    print(f"\nSubtotal (Before Discounts & GST): Rs. {subtotal:.2f}")
    
    # Level 8: Discounts
    # 1. Senior Citizen (>60): 10%
    discount_amount = 0
    discount_log = []
    
    current_total = subtotal
    
    if age >= 60:
        senior_disc = current_total * 0.10
        current_total -= senior_disc
        discount_amount += senior_disc
        discount_log.append(f"Senior Citizen Discount (10%): -{senior_disc:.2f}")
        
    # 2. High Bill (>5000): 5% on remaining
    
    if current_total > 5000:
        high_val_disc = current_total * 0.05
        current_total -= high_val_disc
        discount_amount += high_val_disc
        discount_log.append(f"High Value Discount (5% on >5k): -{high_val_disc:.2f}")

    # Level 5: GST (18%)
    # Applied on the final discounted amount.
    gst_amount = current_total * 0.18
    grand_total = current_total + gst_amount
    
    # Level 6: Invoice
    print("\n" + "-"*40)
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-"*40)
    print("Patient Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Contact: {contact}")
    print("\nServices Availed:")
    for i in range(len(selected_indices)):
        print(f"{i+1}. {selected_services_names[i]}: Rs. {selected_costs[i]:.2f}")
    
    print("-"*40)
    print(f"Subtotal: Rs. {subtotal:.2f}")
    
    if discount_log:
        print("Discounts Applied:")
        for log in discount_log:
            print(log)
        print(f"Net Amount after Discounts: Rs. {current_total:.2f}")
        
    print(f"GST (18%): Rs. {gst_amount:.2f}")
    print(f"Grand Total: Rs. {grand_total:.2f}")
    print("-"*40)
    print("Thank you for choosing HealWell Care Hospital!")
    print("-"*40)

def main():
    print("Welcome to HealWell Care Hospital System")
    while True:
        print("\nMain Menu:")
        print("1. Patient Registration (New Invoice)")
        print("2. Admin Mode (Setup Services)")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            patient_mode()
        elif choice == '2':
            admin_mode()
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

def farmer_problem():
    print("Coding Challenge 5: Farmer Problem Statement")
    
    # Constants
    total_land = 80 # acres
    segments = 5
    land_per_segment = total_land / segments # 16 acres each
    
    # Crop: Tomato
    # 30% of tomato land (16 * 0.3) -> 10 tonnes/acre
    # 70% of tomato land (16 * 0.7) -> 12 tonnes/acre
    tomato_land_1 = land_per_segment * 0.30
    tomato_land_2 = land_per_segment * 0.70
    tomato_yield_1 = tomato_land_1 * 10 * 1000 # tonnes to kg
    tomato_yield_2 = tomato_land_2 * 12 * 1000 # tonnes to kg
    tomato_total_yield = tomato_yield_1 + tomato_yield_2
    tomato_sales = tomato_total_yield * 7
    
    # Crop: Potato
    potato_yield = land_per_segment * 10 * 1000 # 10 tonnes/acre -> kg
    potato_sales = potato_yield * 20
    
    # Crop: Cabbage
    cabbage_yield = land_per_segment * 14 * 1000 # 14 tonnes/acre -> kg
    cabbage_sales = cabbage_yield * 24
    
    # Crop: Sunflower
    sunflower_yield = land_per_segment * 0.7 * 1000 # 0.7 tonnes/acre -> kg
    sunflower_sales = sunflower_yield * 200
    
    # Crop: Sugarcane
    sugarcane_yield = land_per_segment * 45 # tonnes (sales price is per tonne)
    sugarcane_sales = sugarcane_yield * 4000
    
    # Total Sales
    overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
    
    print(f"a. Overall sales achieved by Mahesh from 80 acres: Rs. {overall_sales:,.2f}")
    
    # b. Sales realisation from chemical-free farming at the end of 11 months
    # Timeline:
    # 0-6 months: Vegetables (Tomato, Potato, Cabbage) converted? 
    #   Prompt says: "Mahesh starts with the conversion of vegetables... He spends the first 6 months doing the same."
    #   "Sales realisation from chemical-free farming at the end of 11 months"
    #   Assumption: Crops harvested AFTER conversion are 'chemical-free'.
    #   If conversion finishes at month 6, and he gets yield "in one crop cycle", we assume the yield mentioned IS from that cycle.
    #   If the cycle finishes within the 11 months and is after conversion, it counts.
    #   However, the prompt is slightly ambiguous on WHEN the yield happens relative to conversion. 
    #   But typically, "realisation ... at the end of 11 months" implies what has successfully completed conversion.
    #   Veg (6 months) -> Converted.
    #   Sunflower (6 + 4 = 10 months) -> Converted.
    #   Sugarcane (10 + 4 = 14 months) -> NOT Converted by month 11.
    
    chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
    print(f"b. Sales realisation from chemical-free farming at the end of 11 months: Rs. {chemical_free_sales:,.2f}")

if __name__ == "__main__":
    farmer_problem()

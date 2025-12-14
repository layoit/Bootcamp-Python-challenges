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
    
    
    chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
    print(f"b. Sales realisation from chemical-free farming at the end of 11 months: Rs. {chemical_free_sales:,.2f}")

if __name__ == "__main__":
    farmer_problem()


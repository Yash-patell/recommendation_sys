import pandas as pd
import random

# Generating sample data for 600 rows
data = {
    "brand_id": range(1, 601),
    "brand_name": [f"Brand{random.randint(1, 100)}" for _ in range(600)],
    "product_category": random.choices(
        [
            "Cosmetics", "Fitness Equipment", "Gadgets", "Clothing", 
            "Travel Services", "Fashion Accessories", "Nutrition Products", 
            "Home Appliances", "Gaming Products", "Eco-friendly Goods", 
            "Pet Supplies", "Books", "Smartphones", "Food Products", "Art Supplies"
        ], k=600),
    "audience_age": random.choices(
        ["15-24", "18-25", "18-30", "25-34", "25-40", "30-45", "18-28", "22-40", "40-50", "All"], 
        k=600),
    "audience_gender": random.choices(
        ["Male", "Female", "All"], k=600),
    "audience_location": random.choices(
        [
            "Madhya Pradesh", "Delhi", "India", "Goa", "Maharashtra", 
            "Punjab", "Karnataka", "Gujarat", "Kerala", "Tamil Nadu", 
            "West Bengal", "Haryana", "Uttar Pradesh", "Rajasthan", "Bihar"
        ], k=600)
}

# Creating DataFrame
sample_df = pd.DataFrame(data)

# Saving to CSV
csv_file_path = '/mnt/data/ecommerce_brands_dataset.csv'
sample_df.to_csv(csv_file_path, index=False)

csv_file_path

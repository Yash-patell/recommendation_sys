import pandas as pd
import random

# Generating sample data for 600 rows
data = {
    "id": range(601, 1601),
    # "brand_name": [f"Brand{random.randint(1, 100)}" for _ in range(600)],
    "Influencer_name": random.choices(
        [
            "Ankit", "Sujeet", "Saurav", "Gaurav", 
            "Akshay", "Ashwin", "Vicky", 
            "Faisal", "Gagan", "Rahul", 
            "Rohit", "Salman Khan", "Sarukh khan", "Amitabh", "Sanjay Dutt"
            "Aiden Smith", "Mia Johnson", "Zoe Williams", "Lucas Brown", "Ethan Jones", "Emma Garcia", "Noah Martinez", "Sophia Rodriguez", "Jackson Lee", "Ava Wilson", "Liam Harris", "Isabella Anderson", "Oliver Thompson", "Amelia Taylor","Elijah White"
        ], k=1000),
    
    "Handle": random.choices(
        [
            "Ankit@jk", "Sujeet@r", "Saurav@jn", "Gaurav@jn", 
            "Akshay@kumar", "Ashwin@ravichandra", "Vicky@kaushal", 
            "Faisal@dscdf", "Gagan@fef", "Rahul@cdf", 
            "Rohit@abc", "Salman Khan@abc", "Sarukh khan@abc", "Amitabh@abc", "Sanjay Dutt@abc"
            "Aiden Smith@abc", "Mia Johnson@abc", "Zoe Williams@abc", "Lucas Brown@abc", "Ethan Jones@abc", "Emma Garcia@abc", "Noah Martinez@abc", "Sophia Rodriguez@abc", "Jackson Lee@abc", "Ava Wilson@abc", "Liam Harris@abc", "Isabella Anderson@abc", "Oliver Thompson@abc", "Amelia Taylor@abc","Elijah White@abc"
        ], k=1000),
    
    "Followers": random.choices( [
        "340770", "702603", "113855", "202147", "495171", "341829", "487464", "733223", "183216", 
        "409843", "856447", "767339", "885659", "757739", "302086", "992087", "801403", "114466", 
        "704611", "287030", "980666", "971583", "204024", "254997", "981916", "842653", "784742", 
        "857495", "338878", "366076", "682670", "324945", "440405", "851696", "709166", "664210", 
        "264487", "750376", "546160", "426339", "360266", "169890", "258700", "638336", "741445", 
        "230748", "981575", "612971", "338287", "997417"
        ], k=1000),
    
    "Posts": random.choices( [
       986, 847, 241, 944, 508, 135, 122, 545, 127, 762, 394, 60, 762, 976, 
        999, 245, 58, 534, 386, 961, 390, 962, 609, 540, 174, 544, 757, 317, 
        205, 358, 978, 153, 114, 922, 301, 143, 690, 229, 412, 175, 572, 193, 
        433, 973, 605, 632, 190, 832, 669, 51
        ], k=1000),
    
    "Likes": random.choices( [
       31587, 49725, 41587, 8042, 30531, 26257, 17005, 40347, 28785, 41313, 
        32383, 40011, 5494, 6893, 42198, 18570, 46587, 15636, 21103, 29251, 
        13377, 24228, 36337, 25661, 21697, 41717, 7083, 6903, 47405, 42833, 
        37363, 26869, 27018, 12822, 27084, 12931, 49145, 43038, 32011, 34550, 
        24651, 12690, 20008, 28180, 39221, 24716, 5859, 29874, 22289, 34817
        ], k=1000),

    "Category": random.choices(
        [
            "Nutrition Products", "Smartphones", "Home Appliances", "Gadgets", "Home Appliances", 
        "Fashion Accessories", "Gadgets", "Eco-friendly Goods", "Nutrition Products", 
        "Fashion Accessories", "Travel Services", "Smartphones", "Food Products", 
        "Nutrition Products", "Travel Services", "Gaming Products", "Nutrition Products", 
        "Nutrition Products", "Cosmetics", "Gadgets", "Gadgets", "Pet Supplies", 
        "Books", "Fashion Accessories", "Clothing", "Art Supplies", "Gaming Products", 
        "Cosmetics", "Art Supplies", "Smartphones", "Food Products", "Gaming Products", 
        "Home Appliances", "Travel Services", "Cosmetics", "Food Products", 
        "Travel Services", "Smartphones", "Gadgets", "Smartphones", "Pet Supplies", 
        "Cosmetics", "Travel Services", "Art Supplies", "Eco-friendly Goods", 
        "Travel Services", "Travel Services", "Travel Services", "Art Supplies", 
        "Smartphones", "Fashion Accessories", "Cosmetics", "Smartphones", 
        "Gaming Products"
        ], k=1000),
    
    "Sentiment": random.choices(
        [
            "Positive", "Positive", "Positive", "Negative", "Negative", "Neutral", 
        "Negative", "Negative", "Neutral", "Negative", "Positive", "Neutral", 
        "Negative", "Negative", "Neutral", "Neutral", "Neutral", "Neutral", 
        "Negative", "Negative", "Neutral", "Positive", "Negative", "Negative", 
        "Neutral", "Neutral", "Negative", "Neutral", "Neutral", "Negative", 
        "Negative", "Negative", "Negative", "Positive", "Neutral", "Negative", 
        "Neutral", "Neutral", "Positive", "Neutral", "Neutral", "Positive", 
        "Neutral", "Neutral", "Neutral", "Negative", "Negative", "Negative", 
        "Neutral", "Neutral", "Neutral", "Neutral"
        ], k=1000),
    
    
    "audience_location": random.choices(
        [
           "Kerala", "Gujarat", "Kerala", "Kerala", "Tamil Nadu", "Madhya Pradesh", 
        "Gujarat", "Tamil Nadu", "West Bengal", "Karnataka", "Bihar", "Karnataka", 
        "Kerala", "Karnataka", "Punjab", "Delhi", "Goa", "Kerala", "Tamil Nadu", 
        "Karnataka", "Maharashtra", "Punjab", "Uttar Pradesh", "Rajasthan", 
        "Maharashtra", "Kerala", "Delhi", "Goa", "Punjab", "Rajasthan", 
        "Madhya Pradesh", "Karnataka", "Uttar Pradesh", "Madhya Pradesh", 
        "Maharashtra", "Delhi", "Uttar Pradesh", "Kerala", "Goa", "Rajasthan", 
        "Maharashtra", "Karnataka", "Madhya Pradesh", "Kerala", "Karnataka", 
        "Madhya Pradesh", "Karnataka", "Uttar Pradesh", "Delhi", "Madhya Pradesh", 
        "Delhi", "Haryana"
        ], k=1000),
    
    
    "audience_age": random.choices(
        ["15-24", "All", "18-30", "15-24", "40-50", "40-50", "30-45", "18-30", 
        "30-45", "22-40", "18-30", "18-25", "30-45", "15-24", "18-28", "All", 
        "18-30", "All", "25-40", "18-28", "15-24", "25-40", "18-25", "22-40", 
        "All", "All", "18-30", "18-30", "18-28", "15-24", "22-40", "18-30", 
        "40-50", "15-24"], 
        k=1000),
    
    "audience_gender": random.choices(
        ["Male", "Female", "All"], k=1000),
    
    "Platform": random.choices(
        ["Tiktok", "Instagram", "Facebook", "Twitter","Youtube"], k=1000),
    
    
}

# Creating DataFrame
sample_df = pd.DataFrame(data)

# Saving to CSV
csv_file_path = 'expanded_dataset.csv'
sample_df.to_csv(csv_file_path, index=False)

csv_file_path






import pandas as pd
import random

# Generating sample data for 600 rows
data = {
    "id": range(601, 1601),
    # "brand_name": [f"Brand{random.randint(1, 100)}" for _ in range(600)],
    "brand_name": random.choices(
        [
            'Brand101','Brand102','Brand103','Brand104','Brand105','Brand106','Brand107',
            'Brand108','Brand109','Brand110','Brand111','Brand112','Brand113','Brand114',
            'Brand115','Brand116','Brand117','Brand118','Brand119','Brand120','Brand121',
            'Brand122','Brand123','Brand124','Brand125','Brand126','Brand127','Brand128',
            'Brand129','Brand130','Brand131','Brand132','Brand133','Brand134','Brand135',
            'Brand136','Brand137','Brand138','Brand139','Brand140','Brand141','Brand142',
            'Brand143','Brand144','Brand145','Brand146','Brand147','Brand148','Brand149',
            'Brand150',
        ], k=1000),
    



    "Category": random.choices(
        [
            "Nutrition Products", "Smartphones", "Home Appliances", "Gadgets", "Home Appliances", 
        "Fashion Accessories", "Gadgets", "Eco-friendly Goods", "Nutrition Products", 
        "Fashion Accessories", "Travel Services", "Smartphones", "Food Products", 
        "Nutrition Products", "Travel Services", "Gaming Products", "Nutrition Products", 
        "Nutrition Products", "Cosmetics", "Gadgets", "Gadgets", "Pet Supplies", 
        "Books", "Fashion Accessories", "Clothing", "Art Supplies", "Gaming Products", 
        "Cosmetics", "Art Supplies", "Smartphones", "Food Products", "Gaming Products", 
        "Home Appliances", "Travel Services", "Cosmetics", "Food Products", 
        "Travel Services", "Smartphones", "Gadgets", "Smartphones", "Pet Supplies", 
        "Cosmetics", "Travel Services", "Art Supplies", "Eco-friendly Goods", 
        "Travel Services", "Travel Services", "Travel Services", "Art Supplies", 
        "Smartphones", "Fashion Accessories", "Cosmetics", "Smartphones", 
        "Gaming Products"
        ], k=1000),
    
    
    "target_age": random.choices(
        ["15-24", "All", "18-30", "15-24", "40-50", "40-50", "30-45", "18-30", 
        "30-45", "22-40", "18-30", "18-25", "30-45", "15-24", "18-28", "All", 
        "18-30", "All", "25-40", "18-28", "15-24", "25-40", "18-25", "22-40", 
        "All", "All", "18-30", "18-30", "18-28", "15-24", "22-40", "18-30", 
        "40-50", "15-24"], 
        k=1000),
    
    
     "target_gender": random.choices(
        ["Male", "Female", "All"], k=1000),
    
    
    "target_location": random.choices(
        [
        "Kerala", "Gujarat", "Kerala", "Kerala", "Tamil Nadu", "Madhya Pradesh", 
        "Gujarat", "Tamil Nadu", "West Bengal", "Karnataka", "Bihar", "Karnataka", 
        "Kerala", "Karnataka", "Punjab", "Delhi", "Goa", "Kerala", "Tamil Nadu", 
        "Karnataka", "Maharashtra", "Punjab", "Uttar Pradesh", "Rajasthan", 
        "Maharashtra", "Kerala", "Delhi", "Goa", "Punjab", "Rajasthan", 
        "Madhya Pradesh", "Karnataka", "Uttar Pradesh", "Madhya Pradesh", 
        "Maharashtra", "Delhi", "Uttar Pradesh", "Kerala", "Goa", "Rajasthan", 
        "Maharashtra", "Karnataka", "Madhya Pradesh", "Kerala", "Karnataka", 
        "Madhya Pradesh", "Karnataka", "Uttar Pradesh", "Delhi", "Madhya Pradesh", 
        "Delhi", "Haryana"
        ], k=1000),
    
    
    
    
   
    
    
    
}

# Creating DataFrame
sample_df = pd.DataFrame(data)

# Saving to CSV
csv_file_path = 'brand_expanded_dataset.csv'
sample_df.to_csv(csv_file_path, index=False)

csv_file_path

import pandas as pd

def load_ingredient_data(csv_path='ingredient_data.csv'):
    return pd.read_csv(csv_path)

def analyze_ingredients(ingredient_list, user_allergies=[]):
    data = load_ingredient_data()
    harmful = []

    for ingredient in ingredient_list:
        match = data[data['ingredient'].str.lower() == ingredient.lower()]
        if not match.empty:
            row = match.iloc[0]
            flags = row['flags'].split(',') if pd.notna(row['flags']) else []
            if row['risk_level'].lower() != 'low' or ingredient.lower() in [a.lower() for a in user_allergies]:
                harmful.append({
                    'ingredient': ingredient,
                    'risk_level': row['risk_level'],
                    'reason': row['reason'],
                    'flags': flags
                })

    return harmful

def analyze_product(product_name):
    example_ingredients = {
        'KitKat': ['Sugar', 'Cocoa', 'Milk Solids'],
        'Peanut Butter': ['Sugar', 'Salt', 'Peanuts'],
        'Dark Chocolate': ['Cocoa', 'Sugar'],
    }

    ingredients = example_ingredients.get(product_name, [])
    harmful = analyze_ingredients(ingredients)

    status = "Safe" if not harmful else "Warning"
    suggestions = ["Choose sugar-free options", "Consult a nutritionist"] if harmful else []

    return {
        'product': product_name,
        'status': status,
        'harmful_ingredients': harmful,
        'suggestions': suggestions
    }

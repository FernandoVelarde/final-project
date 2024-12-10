import requests, json
from pprint import pprint

def ingredient_api(endpoint, params=None):
    try:
        r = requests.get(endpoint, params)
        r.raise_for_status()
        data = r.json()

        return data
    
    except:
        pprint('please try again')

def search_ingredient(ingredients):
    recipes = []
    
    for recipe in ingredients:
        meal_name = recipe.get('title', 'Unknown Meal')
        image = recipe.get('image', 'No Image Available')
        
        all_ingredients = recipe.get('missedIngredients', []) + recipe.get('usedIngredients', [])
        
        ingredients = [
            f"{item['amount']} {item['unit']} {item['name']}".strip() 
            for item in all_ingredients
            if item.get('name')
        ]
        
        recipes.append({
            'meal_name': meal_name,
            'ingredients': ingredients,
            'image': image
        })
    
    return recipes

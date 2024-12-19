import requests, json
from pprint import pprint

def param(ingredients):
    
    api_key = 'b2e95471eaf54dd2bbd82b1af46e53dd'
    params = {
    "apiKey": api_key,
    "ingredients": ingredients,
    "number": 30,
    "ranking": 2,
    "ignorePantry": True,
    "addRecipeInformation": True
    }
    return params

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
        recipe_id = recipe.get('id', 'Unknown ID')
        source_url = recipe.get('')

        all_ingredients = recipe.get('missedIngredients', []) + recipe.get('usedIngredients', [])
        
        ingredients = [
            f"{item['amount']} {item['unit']} {item['name']}".strip() 
            for item in all_ingredients
            if item.get('name')
        ]
        
        recipes.append({
            'meal_name': meal_name,
            'ingredients': ingredients,
            'image': image,
            'id': recipe_id
        })
    
    return recipes
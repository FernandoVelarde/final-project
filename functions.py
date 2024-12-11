import requests, json
from pprint import pprint

# This is what we did in class, but it's a function for any other future api we will need.
def ingredient_api(endpoint, params=None):
    try:
        r = requests.get(endpoint, params)
        r.raise_for_status()
        data = r.json()

        return data
    
    except:
        pprint('please try again')

# This is the functions that gets the needed information from the api.
# This will then get passed onto the website getting shown by flask.
def search_ingredient(ingredients):
    recipes = []
        
    for recipe in ingredients:
# The next three lines gets from the dictionary, the meal name, image, and recipe id.
        meal_name = recipe.get('title', 'Unknown Meal')
        image = recipe.get('image', 'No Image Available')
        recipe_id = recipe.get('id', 'Unknown ID')

# This gets all the ingredients that were typed in and ingredients that were not typed in.
        all_ingredients = recipe.get('missedIngredients', []) + recipe.get('usedIngredients', [])
        
# This list loops through the ingredients and gets measurements and organizes it to its corresponding ingredient.
# The if statement ensures it is getting from a valid key.
        ingredients = [
            f"{item['amount']} {item['unit']} {item['name']}".strip() 
            for item in all_ingredients
            if item.get('name')
        ]
        
        recipes.append({
            'meal_name': meal_name,
            'ingredients': ingredients,
            'image': image,
            'recipe_id': recipe_id
        })
    
    return recipes

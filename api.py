from functions import search_ingredient, ingredient_api
from pprint import pprint
import requests, json

url = "https://api.spoonacular.com/recipes/findByIngredients"
    
api_key = 'b2e95471eaf54dd2bbd82b1af46e53dd'
# ingredients = input('Enter ingredients: ')

params = {
    "apiKey": api_key,
    "ingredients": ingredients,
    "number": 9,
    "ranking": 2,
    "ignorePantry": True
}

# meals = ingredient_api(url, params)
# pprint(meals)
# pprint(search_ingredient(meals))

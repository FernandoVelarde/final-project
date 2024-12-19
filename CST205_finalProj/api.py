from functions import search_ingredient, ingredient_api
from pprint import pprint
import requests, json

url = "https://api.spoonacular.com/recipes/findByIngredients"
    
api_key = 'b2e95471eaf54dd2bbd82b1af46e53dd'
# ingredients = input('Enter ingredients: ')

"""
For the ingredients variable, it should connect with the search bar where the ingredients are typed in.
It does not work at the moment because I tested it with the input above.
We need to connect the user input (search bar) to this variable.
"""

params = {
    "apiKey": api_key,
    "ingredients": "ingredients",
    "number": 9,
    "ranking": 2,
    "ignorePantry": True
}

# meals = ingredient_api(url, params)
# pprint(meals)
# pprint(search_ingredient(meals))

from pprint import pprint
import requests, json
Github = 'https://github.com/FernandoVelarde/final-project/tree/main'
endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
#APIKEY was here
def apisearch(endpoint, params=None):
    try:
        r = requests.get(endpoint, params)
        data = r.json()
        pprint(data)
    except:
        print('please try again')

query = input('Enter recipe: ')
recipeParameters = {
    'apiKey': apiKey,
    'query': query,
    'addRecipeInformation': True,
    'addRecipeInstructions': True,
    'titleMatch': query,
    'number': 1,
    'instructionsRequired': True,
}
#need step, ingredients, number(for what step we are on if needed), name, image
#return fillIngredients, addRecipeInformation, addRecipeInstructions
def searchrecipe(recipes):
    return_data = []
    #to get the nested lists and dictionaries
    for recipe in recipes:
        name = recipe.get('title', 'Unknown recipe')
        instructions = recipe.get('analyzedInstructions', [])
        image = recipe.get('image', 'No image available')
        source_url = recipe.get('sourceUrl', 'No source')
    for instruction in instructions:
        for step in instruction.get('steps', []):
            step_number = step.get('number', 'N/A')
            step_description = step.get('step', 'No step')
            ingredients = [ingredient['name'] for ingredient in step.get('ingredients', [])]
            #process the data
            return_data.append({
                'recipe_name': name,
                'recipe_image': image,
                'source_url':source_url,
                'step_number': step_number,
                'step_description': step_description,
                'ingredients': ingredients
            })
    return return_data
        
meals = apisearch(endpoint, recipeParameters)

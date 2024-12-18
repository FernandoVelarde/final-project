# NAME: Marissa Benenati
# DATE: 11.20.24
# COURSE: CST 205
# ASSIGNMENT: Final Project


##### ##### IMPORTS ##### #####
from functions import search_ingredient, ingredient_api, param
from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
import random
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

########## SEARCH FORM (HOME PAGE) ##########
class SearchBar(FlaskForm):
    user_search = StringField(
        #'Enter Search: ', 
        validators=[DataRequired()]
    )


########## RESULTS DICTIONARY ##########
"""
TO DO:
  > replace sample results with actual search results
search_results = [
    {'image': '/imagepath.png', 'title': 'RECIPE TITLE 1', 'ingredients': 'ingredients separated by commas', 'link': 'https://example.com/1'},
    {'image': '/imagepath.png', 'title': 'RECIPE TITLE 2', 'ingredients': 'ingredients separated by commas', 'link': 'https://example.com/2'},
    # ... more results
]
"""
ingredients = []
recipes = []
url = "https://api.spoonacular.com/recipes/findByIngredients"

"""
def store_ingredient(my_ingredient):
   ingredients.append(dict(ingredient = my_ingredient))
"""

########## HOME PAGE ##########
@app.route('/', methods=['GET', 'POST'])
def home():
   user_search = None
   form = SearchBar()
   # validate form input
   if form.validate_on_submit():
      user_search = form.user_search.data      # assigns data within form (search bar) to variable "user_search"
      #form.user_search.data = ""       # resets form
      return redirect(url_for('results-view.html'))
   return render_template('home.html', user_search=user_search, form=form)


########## SEARCH RESULTS ##########
@app.route('/searchIngredient', methods=["POST"])
def searchIngredient():
   query = request.form['query']
   print("INGREDIENT!!")

   if not query:
        flash("No ingredients provided.\nPlease go back and enter ingredients.")
        return redirect(url_for('home'))
   
   ingredients.append(query)

   parameters = param(ingredients)
   full_recipes = ingredient_api(url, parameters)
   results = search_ingredient(full_recipes)

   pprint(full_recipes)

   return render_template('results-view.html', results=results)

# @app.route('/searchRecipe', methods=["POST"])
# def searchRecipe():
#    query = request.form['query']

#    print("RECIPE!!")
#    if not query:
#         flash("No ingredients provided.\nPlease go back and enter ingredients.")
#         return redirect(url_for('home'))
   
#    ingredients.append(query)

#    parameters = param(ingredients)
#    full_recipes = ingredient_api(url, parameters)
#    results = search_ingredient(full_recipes)


#    return render_template('results-view.html', results=results)

@app.route('/detail/<recipe_id>')
def detail(recipe_id):
   recipes = session.get('recipes')
   if not recipes:
      flash("No recipes found. Please try a different search.")
      return redirect(url_for('index'))
   
   recipe_data = None
   for i in recipes:
      if str(i['id']) == recipe_id:
         recipe_data = i
         break
      
   meal = recipe_data['meal_name']
   ingredients_list = recipe_data['ingredients']
   image = recipe_data['image']

   return render_template('detail.html', ingredients=ingredients, meal=meal, ingredients_list=ingredients_list, image=image)


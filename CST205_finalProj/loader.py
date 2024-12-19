from functions import search_ingredient, ingredient_api, param
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
from api import params
import random

url = "https://api.spoonacular.com/recipes/findByIngredients"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class Ingredient(FlaskForm):
    ingredient_names = StringField('Ingredients', validators=[DataRequired()])
    
ingredients = []
recipes = []

def store_ingredient(my_ingredient):
    ingredients.append(dict(ingredient = my_ingredient))


@app.route('/', methods=('GET', 'POST'))
def index():
    form = Ingredient()
    if form.validate_on_submit():
        ingredients = form.ingredient_names.data
        session['ingredients'] = ingredients
        return redirect(url_for('info'))
    
    return render_template('index.html', form=form)


@app.route('/info')
def info():
    ingredients = session.get('ingredients', '')
    if not ingredients:
        flash("No ingredients provided.\nPlease go back and enter ingredients.")
        return redirect(url_for('index'))
    
    parameters = param(ingredients)
    full_recipes = ingredient_api(url, parameters)
    recipes = search_ingredient(full_recipes)

    session['recipes'] = recipes
    return render_template('info.html', recipes=recipes)

@app.route('/detail/<recipe_id>')
def detail(recipe_id):
    recipes = session.get('recipes')
    if not recipes:
        flash("No recipes found. Please search again.")
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
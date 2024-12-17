# NAME: Marissa Benenati
# DATE: 11.20.24
# COURSE: CST 205
# ASSIGNMENT: Final Project


##### ##### IMPORTS ##### #####
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
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
"""
search_results = [
    {'image': '/imagepath.png', 'title': 'RECIPE TITLE 1', 'ingredients': 'ingredients separated by commas', 'link': 'https://example.com/1'},
    {'image': '/imagepath.png', 'title': 'RECIPE TITLE 2', 'ingredients': 'ingredients separated by commas', 'link': 'https://example.com/2'},
    # ... more results
]

########## HOME PAGE ##########
@app.route('/')
def home():
   return render_template('home.html')

########## SEARCH RESULTS ##########
@app.route('/results-view')
def results():
   return render_template('results-view.html', results=search_results)  # references results dictionary


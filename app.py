from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired
import finnhub
import pandas as pd
import requests
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

#finnhub library - stock information
my_api_key = "c1lqu4q37fkqle0e7290"



class NewsForm(FlaskForm):
    category = RadioField("Category: ",  choices=['General', 'Forex', 'Crypto', 'Merger'], validators=[DataRequired()])
    submit = SubmitField("Search")


@app.route('/', methods=["GET", "POST"])
def index():
    news_form = NewsForm(csrf_enabled=False)
    market_news = []
    if news_form.validate_on_submit():
        stock_query = news_form.category.data
        print(stock_query)
        market_news = requests.get(f'https://finnhub.io/api/v1/news?category={stock_query}&token={my_api_key}').json()
        print(len(market_news))
    return render_template('index.html', template_form=news_form, template_data=market_news)

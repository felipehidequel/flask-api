from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
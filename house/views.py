from flask import Blueprint, render_template
from datetime import datetime
from .models import House
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    houses = House.query.order_by(House.address).all()
    return render_template('index.html', houses = houses)




    
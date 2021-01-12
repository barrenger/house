from flask import Blueprint, render_template, url_for, request
from datetime import datetime
from .models import House, Room, Bedroom, Kitchen, Living, Bath, Garage
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    houses = House.query.order_by(House.address).all()
    return render_template('index.html', houses = houses)

# Displays details of house
@bp.route('/details/<int:houseId>/', methods=['POST','GET'])
def details(houseId):
    address = request.values.get('address')
    suburb = request.values.get('suburb')
    
    house = None
    if address and suburb:
        house = House(address = address, suburb=suburb)
        try:
            db.session.add(house)
            db.session.commit()
            houseId = house.id
        except:
            print('failed at creating a new house')
            house = None
    elif houseId:
        house = House.query.get(houseId)
        
    bedrooms = Bedroom.query.filter(Bedroom.house_id == houseId).all()
    kitchens = Bedroom.query.filter(Kitchen.house_id == houseId)
    livingrooms = Bedroom.query.filter(Living.house_id == houseId)
    bathrooms = Bedroom.query.filter(Bath.house_id == houseId)
    garages = Bedroom.query.filter(Garage.house_id == houseId)

    return render_template('details.html', house=house, bedroom_qty=len(bedrooms), bedrooms=bedrooms)

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
        
    rooms = []
    roomOverviews = Room.query.filter(Room.house_id == houseId).all()
    for overview in roomOverviews:
        bedroom = Bedroom.query.filter(Bedroom.room_id == overview.id).all()
        kitchen = Kitchen.query.filter(Bedroom.room_id == overview.id).all()
        living = Living.query.filter(Bedroom.room_id == overview.id).all()
        bath = Bath.query.filter(Bedroom.room_id == overview.id).all()
        garage = Garage.query.filter(Bedroom.room_id == overview.id).all()
        
        myType = ""
        room = None

        if len(bedroom) == 1:
            myType = "bedroom"
            room = bedroom[0]
        if len(kitchen) == 1:
            myType = "kitchen"
            room = kitchen[0]
        if len(living) == 1:
            myType = "living"
            room = living[0]
        if len(bath) == 1:
            myType = "bath"
            room = bath[0]
        if len(garage) == 1:
            myType = "garage"
            room = garage[0]

        if myType != "":
            roomComplete = RoomComplete(overview,myType,room)
            rooms.append(roomComplete)

    return render_template('details.html', house=house, rooms=rooms)

class RoomComplete:
    def __init__(self, overview, roomType, room):
        self.overview = overview
        self.roomType = roomType
        self.room = room

    def __repr__(self):
        str = "Room Id: {}, Type: {}\n" 
        str =str.format( self.overview.id, self.roomType)
        return str

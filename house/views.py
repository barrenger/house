from flask import Blueprint, render_template, url_for, request
from datetime import datetime
from .models import House, Room, Bedroom, Kitchen, Living, Bath, Garage
from . import db


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Query for list of houses
    houses = House.query.order_by(House.address).all()

    # Get the qty of each room in the house.
    for house in houses:
        bedrooms = Bedroom.query.filter(Bedroom.house_id == house.id).all()
        house.bedrooms = len(bedrooms)
        kitchens = Kitchen.query.filter(Kitchen.house_id == house.id).all()
        house.kitchens = len(kitchens)
        livingrooms = Living.query.filter(Living.house_id == house.id).all()
        house.livingrooms = len(livingrooms)
        bathrooms = Bath.query.filter(Bath.house_id == house.id).all()
        house.bathrooms = len(bathrooms)

        # Get the number of car spaces.
        garages = Garage.query.filter(Garage.house_id == house.id).all()
        carSpaces = 0
        for garage in garages:
            if garage.cars != None:
                carSpaces += garage.cars
        house.garages = carSpaces

    # Render the page passing the list of houses.
    return render_template('index.html', houses = houses)

# Displays details of house.
@bp.route('/details/<int:houseId>/', methods=['POST','GET'])
def details(houseId):
    new = request.values.get('new')
    update = request.values.get('update')
    
    house = None
    bedrooms = None
    kitchens = None
    livingrooms = None
    bathrooms = None
    garages = None

    if new:
        address = request.values.get('address')
        suburb = request.values.get('suburb')

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
        if update:
            # Update the House model.
            house.address = request.values.get('address')
            house.suburb = request.values.get('suburb')
            house.price_ask = ConvertNumber(request.values.get('price_ask'))
            house.price_sale = ConvertNumber(request.values.get('price_sale'))
            try:
                house.date_market = datetime.strptime(request.values.get('date_market'), "%Y-%m-%d")
            except:
                house.date_market = None
                print('failed at updating dates')
            try:
                house.date_sale = datetime.strptime(request.values.get('date_sale'), "%Y-%m-%d")
            except:
                house.date_sale = None
                print('failed at updating dates')

            house.construction_mat = request.values.get('construction_mat')
            house.land_size = request.values.get('land_size')
            house.house_size = request.values.get('house_size')
            house.street_type = request.values.get('street_type')
            house.roof_mat = request.values.get('roof_mat')
            house.roof_cond = request.values.get('roof_cond')
            house.insulation = ConvertBool(request.values.get('insulation'))
            house.driveway_cond = request.values.get('driveway_cond')
            house.fenced = request.values.get('fenced')
            house.fence_cond = request.values.get('fence_cond')
            house.backyard_size = request.values.get('backyard_size')
            house.yard_level = request.values.get('yard_level')
            house.landcaping_cond = request.values.get('landcaping_cond')
            house.pool = request.values.get('pool')
            house.pool_type = request.values.get('pool_type')
            house.pool_construction = request.values.get('pool_construction')
            house.pool_filter = request.values.get('pool_filter')
            house.pool_cleaner = request.values.get('pool_cleaner')

            house.underhouse_access = ConvertBool(request.values.get('underhouse_access'))
            house.council_approval = ConvertBool(request.values.get('council_approval'))
            house.cracks = request.values.get('cracks')
            house.roof_lines = ConvertBool(request.values.get('roof_lines'))
            house.gutters_cond = request.values.get('gutters_cond')
            house.downpipes = request.values.get('downpipes')
            house.trees = request.values.get('trees')
            house.outside_elec_cond = request.values.get('outside_elec_cond')
            house.flood_zone = ConvertBool(request.values.get('flood_zone'))
            house.sewage = request.values.get('sewage')

            house.notes = request.values.get('notes')

            # Commit changes to the database.
            try:
                db.session.commit()
            except:
                print('failed at updating house')
        
            # Update the Bedroom model.
            bedrooms = Bedroom.query.filter(Bedroom.house_id == houseId).all()

            # Check for new bedrooms.
            newBedrooms = int(request.values.get('newBedrooms'))
            for i in range(newBedrooms):
                room = Room()
                try:
                    db.session.add(room)
                    db.session.commit()
                    roomId = room.id
                except:
                    print('failed at creating a new room')
                
                bedroom = Bedroom(house_id = houseId, room_id = roomId)
                try:
                    db.session.add(bedroom)
                    db.session.commit()
                except:
                    print('failed at creating a new bedroom')

            # Update bedrooms.
            for i in range(len(bedrooms)):
                bedrooms[i].room.size = request.values.get('bedroom-' + str(i) + '-size')
                bedrooms[i].room.floor_mat = request.values.get('bedroom-' + str(i) + '-floor_mat')
                bedrooms[i].room.layout = request.values.get('bedroom-' + str(i) + '-layout')
                bedrooms[i].room.power_points = request.values.get('bedroom-' + str(i) + '-power_points')
                bedrooms[i].room.door_close = request.values.get('bedroom-' + str(i) + '-door_close')
                bedrooms[i].room.light_natural = request.values.get('bedroom-' + str(i) + '-light_natural')
                bedrooms[i].room.light_artificial = request.values.get('bedroom-' + str(i) + '-light_artificial')
                bedrooms[i].room.window_op = request.values.get('bedroom-' + str(i) + '-window_op')
                bedrooms[i].room.fly_screens = request.values.get('bedroom-' + str(i) + '-fly_screens')
                bedrooms[i].room.wall_windows_qty = ConvertNumber(request.values.get('bedroom-' + str(i) + '-wall_windows_qty'))
                bedrooms[i].room.window_dir_1 = request.values.get('bedroom-' + str(i) + '-window_dir_1')
                bedrooms[i].room.window_dir_2 = request.values.get('bedroom-' + str(i) + '-window_dir_2')
                bedrooms[i].room.window_dir_3 = request.values.get('bedroom-' + str(i) + '-window_dir_3')
                bedrooms[i].room.ceiling_sag = ConvertBool(request.values.get('bedroom-' + str(i) + '-ceiling_sag'))
                bedrooms[i].room.moisture = request.values.get('bedroom-' + str(i) + '-moisture')
                bedrooms[i].room.plasterboard_defects = ConvertBool(request.values.get('bedroom-' + str(i) + '-plasterboard_defects'))
                
                bedrooms[i].fan = request.values.get('bedroom-' + str(i) + '-fan')
                bedrooms[i].ac = request.values.get('bedroom-' + str(i) + '-ac')
                bedrooms[i].blinds = request.values.get('bedroom-' + str(i) + '-blinds')
                bedrooms[i].wardrobe = request.values.get('bedroom-' + str(i) + '-wardrobe')
                bedrooms[i].walk_in = request.values.get('bedroom-' + str(i) + '-walk_in')

            # Commit changes to the database.
            try:
                db.session.commit()
            except:
                print('failed at updating bedrooms')

            # Check for removed bedrooms.
            removeBedrooms = request.values.get('removeBedrooms')
            if removeBedrooms != '':
                removeArr = removeBedrooms.split(",")
                for removeId in removeArr:
                    bedroom = Bedroom.query.get(removeId)
                    try:
                        db.session.delete(bedroom)
                        db.session.commit()
                    except:
                        print('failed at deleting a bedroom')


            # Update the Kitchen model.
            kitchens = Kitchen.query.filter(Kitchen.house_id == houseId).all()

            # Check for new kitchens.
            newKitchens = int(request.values.get('newKitchens'))
            for i in range(newKitchens):
                room = Room()
                try:
                    db.session.add(room)
                    db.session.commit()
                    roomId = room.id
                except:
                    print('failed at creating a new room')
                
                kitchen = Kitchen(house_id = houseId, room_id = roomId)
                try:
                    db.session.add(kitchen)
                    db.session.commit()
                except:
                    print('failed at creating a new kitchen')

            # Update kitchens.
            for i in range(len(kitchens)):
                kitchens[i].room.size = request.values.get('kitchen-' + str(i) + '-size')
                kitchens[i].room.floor_mat = request.values.get('kitchen-' + str(i) + '-floor_mat')
                kitchens[i].room.layout = request.values.get('kitchen-' + str(i) + '-layout')
                kitchens[i].room.power_points = request.values.get('kitchen-' + str(i) + '-power_points')
                kitchens[i].room.door_close = request.values.get('kitchen-' + str(i) + '-door_close')
                kitchens[i].room.light_natural = request.values.get('kitchen-' + str(i) + '-light_natural')
                kitchens[i].room.light_artificial = request.values.get('kitchen-' + str(i) + '-light_artificial')
                kitchens[i].room.window_op = request.values.get('kitchen-' + str(i) + '-window_op')
                kitchens[i].room.fly_screens = request.values.get('kitchen-' + str(i) + '-fly_screens')
                kitchens[i].room.wall_windows_qty = request.values.get('kitchen-' + str(i) + '-wall_windows_qty')
                kitchens[i].room.window_dir_1 = request.values.get('kitchen-' + str(i) + '-window_dir_1')
                kitchens[i].room.window_dir_2 = request.values.get('kitchen-' + str(i) + '-window_dir_2')
                kitchens[i].room.window_dir_3 = request.values.get('kitchen-' + str(i) + '-window_dir_3')
                kitchens[i].room.ceiling_sag = ConvertBool(request.values.get('kitchen-' + str(i) + '-ceiling_sag'))
                kitchens[i].room.moisture = request.values.get('kitchen-' + str(i) + '-moisture')
                kitchens[i].room.plasterboard_defects = ConvertBool(request.values.get('kitchen-' + str(i) + '-plasterboard_defects'))

                kitchens[i].fan = request.values.get('kitchen-' + str(i) + '-fan')
                kitchens[i].ac = request.values.get('kitchen-' + str(i) + '-ac')
                kitchens[i].quality = request.values.get('kitchen-' + str(i) + '-quality')
                kitchens[i].bench_mat = request.values.get('kitchen-' + str(i) + '-bench_mat')
                kitchens[i].bench_mat = request.values.get('kitchen-' + str(i) + '-bench_mat')
                kitchens[i].cupboard_space = request.values.get('kitchen-' + str(i) + '-cupboard_space')
                kitchens[i].pantry_space = request.values.get('kitchen-' + str(i) + '-pantry_space')
                kitchens[i].oven_size = request.values.get('kitchen-' + str(i) + '-oven_size')
                kitchens[i].cooktop = request.values.get('kitchen-' + str(i) + '-cooktop')
                kitchens[i].sink = request.values.get('kitchen-' + str(i) + '-sink')
                kitchens[i].water_pressure = request.values.get('kitchen-' + str(i) + '-water_pressure')
                kitchens[i].hot_water_lag = ConvertNumber(request.values.get('kitchen-' + str(i) + '-hot_water_lag'))

            # Commit changes to the database.
            try:
                db.session.commit()
            except:
                print('failed at updating kitchens')

            # Check for removed kitchens.
            removeKitchens = request.values.get('removeKitchens')
            if removeKitchens != '':
                removeArr = removeKitchens.split(",")
                for removeId in removeArr:
                    kitchen = Kitchen.query.get(removeId)
                    try:
                        db.session.delete(kitchen)
                        db.session.commit()
                    except:
                        print('failed at deleting a bedroom')

            # Update the Livingroom model.
            livingrooms = Living.query.filter(Living.house_id == houseId).all()
            
            # Check for new livingrooms.
            newLivingrooms = int(request.values.get('newLivingrooms'))
            for i in range(newLivingrooms):
                room = Room()
                try:
                    db.session.add(room)
                    db.session.commit()
                    roomId = room.id
                except:
                    print('failed at creating a new room')
                
                livingroom = Living(house_id = houseId, room_id = roomId)
                try:
                    db.session.add(livingroom)
                    db.session.commit()
                except:
                    print('failed at creating a new livingroom')

            # Update livingroom.
            for i in range(len(livingrooms)):
                livingrooms[i].room.size = request.values.get('livingroom-' + str(i) + '-size')
                livingrooms[i].room.floor_mat = request.values.get('livingroom-' + str(i) + '-floor_mat')
                livingrooms[i].room.layout = request.values.get('livingroom-' + str(i) + '-layout')
                livingrooms[i].room.power_points = request.values.get('livingroom-' + str(i) + '-power_points')
                livingrooms[i].room.door_close = request.values.get('livingroom-' + str(i) + '-door_close')
                livingrooms[i].room.light_natural = request.values.get('livingroom-' + str(i) + '-light_natural')
                livingrooms[i].room.light_artificial = request.values.get('livingroom-' + str(i) + '-light_artificial')
                livingrooms[i].room.window_op = request.values.get('livingroom-' + str(i) + '-window_op')
                livingrooms[i].room.fly_screens = request.values.get('livingroom-' + str(i) + '-fly_screens')
                livingrooms[i].room.wall_windows_qty = request.values.get('livingroom-' + str(i) + '-wall_windows_qty')
                livingrooms[i].room.window_dir_1 = request.values.get('livingroom-' + str(i) + '-window_dir_1')
                livingrooms[i].room.window_dir_2 = request.values.get('livingroom-' + str(i) + '-window_dir_2')
                livingrooms[i].room.window_dir_3 = request.values.get('livingroom-' + str(i) + '-window_dir_3')
                livingrooms[i].room.ceiling_sag = ConvertBool(request.values.get('livingroom-' + str(i) + '-ceiling_sag'))
                livingrooms[i].room.moisture = request.values.get('livingroom-' + str(i) + '-moisture')
                livingrooms[i].room.plasterboard_defects = ConvertBool(request.values.get('livingroom-' + str(i) + '-plasterboard_defects'))

                livingrooms[i].fan = request.values.get('livingroom-' + str(i) + '-fan')
                livingrooms[i].ac = request.values.get('livingroom-' + str(i) + '-ac')
                livingrooms[i].layout = request.values.get('livingroom-' + str(i) + '-layout')
                livingrooms[i].size = request.values.get('livingroom-' + str(i) + '-size')
                livingrooms[i].ariel = request.values.get('livingroom-' + str(i) + '-ariel')

            # Commit changes to the database.
            try:
                db.session.commit()
            except:
                print('failed at updating livingrooms')

            # Check for removed livingrooms.
            removeLivingrooms = request.values.get('removeLivingrooms')
            if removeLivingrooms != '':
                removeArr = removeLivingrooms.split(",")
                for removeId in removeArr:
                    livingroom = Living.query.get(removeId)
                    try:
                        db.session.delete(livingroom)
                        db.session.commit()
                    except:
                        print('failed at deleting a livingroom')


            # Update the Bathroom model.
            bathrooms = Bath.query.filter(Bath.house_id == houseId).all()

            # Check for new bathrooms.
            newBathrooms = int(request.values.get('newBathrooms'))
            for i in range(newBathrooms):
                room = Room()
                try:
                    db.session.add(room)
                    db.session.commit()
                    roomId = room.id
                except:
                    print('failed at creating a new room')
                
                bathroom = Bath(house_id = houseId, room_id = roomId)
                try:
                    db.session.add(bathroom)
                    db.session.commit()
                except:
                    print('failed at creating a new bathroom')

            # Update bathrooms.
            for i in range(len(bathrooms)):
                bathrooms[i].room.size = request.values.get('bathroom-' + str(i) + '-size')
                bathrooms[i].room.floor_mat = request.values.get('bathroom-' + str(i) + '-floor_mat')
                bathrooms[i].room.layout = request.values.get('bathroom-' + str(i) + '-layout')
                bathrooms[i].room.power_points = request.values.get('bathroom-' + str(i) + '-power_points')
                bathrooms[i].room.door_close = request.values.get('bathroom-' + str(i) + '-door_close')
                bathrooms[i].room.light_natural = request.values.get('bathroom-' + str(i) + '-light_natural')
                bathrooms[i].room.light_artificial = request.values.get('bathroom-' + str(i) + '-light_artificial')
                bathrooms[i].room.window_op = request.values.get('bathroom-' + str(i) + '-window_op')
                bathrooms[i].room.fly_screens = request.values.get('bathroom-' + str(i) + '-fly_screens')
                bathrooms[i].room.wall_windows_qty = request.values.get('bathroom-' + str(i) + '-wall_windows_qty')
                bathrooms[i].room.window_dir_1 = request.values.get('bathroom-' + str(i) + '-window_dir_1')
                bathrooms[i].room.window_dir_2 = request.values.get('bathroom-' + str(i) + '-window_dir_2')
                bathrooms[i].room.window_dir_3 = request.values.get('bathroom-' + str(i) + '-window_dir_3')
                bathrooms[i].room.ceiling_sag = ConvertBool(request.values.get('bathroom-' + str(i) + '-ceiling_sag'))
                bathrooms[i].room.moisture = request.values.get('bathroom-' + str(i) + '-moisture')
                bathrooms[i].room.plasterboard_defects = ConvertBool(request.values.get('bathroom-' + str(i) + '-plasterboard_defects'))

                bathrooms[i].toilet_cond = request.values.get('bathroom-' + str(i) + '-toilet_cond')
                bathrooms[i].shower_cond = request.values.get('bathroom-' + str(i) + '-shower_cond')
                bathrooms[i].shower_size = request.values.get('bathroom-' + str(i) + '-shower_size')
                bathrooms[i].shower_head = request.values.get('bathroom-' + str(i) + '-shower_head')
                bathrooms[i].sink_cond = request.values.get('bathroom-' + str(i) + '-sink_cond')
                bathrooms[i].water_pressure = request.values.get('bathroom-' + str(i) + '-water_pressure')
                bathrooms[i].hot_water_lag = ConvertNumber(request.values.get('bathroom-' + str(i) + '-hot_water_lag'))
                bathrooms[i].extraction_fan = request.values.get('bathroom-' + str(i) + '-extraction_fan')

            # Commit changes to the database.
            try:
                db.session.commit()
            except:
                print('failed at updating bathrooms')

            # Check for removed bathrooms.
            removeBathrooms = request.values.get('removeBathrooms')
            if removeBathrooms != '':
                removeArr = removeBathrooms.split(",")
                for removeId in removeArr:
                    bathroom = Bath.query.get(removeId)
                    try:
                        db.session.delete(bathroom)
                        db.session.commit()
                    except:
                        print('failed at deleting a bathroom')                

            # Update the Garage model
            garages = Garage.query.filter(Garage.house_id == houseId).all()

            # Check for new garages
            newGarages = int(request.values.get('newGarages'))
            for i in range(newGarages):
                garage = Garage(house_id = houseId)
                try:
                    db.session.add(garage)
                    db.session.commit()
                except:
                    print('failed at creating a new garage')

            # Update garages.
            for i in range(len(garages)):
                garages[i].garage_type = request.values.get('garage-' + str(i) + '-garage_type')
                garages[i].cars = ConvertNumber(request.values.get('garage-' + str(i) + '-cars'))
                garages[i].garage_cond = request.values.get('garage-' + str(i) + '-garage_cond')
                garages[i].door = request.values.get('garage-' + str(i) + '-door')

            #commit changes to the database
            try:
                db.session.commit()
            except:
                print('failed at updating garages')

            # Check for removed garages.
            removeGarages = request.values.get('removeGarages')
            if removeGarages != '':
                removeArr = removeGarages.split(",")
                for removeId in removeArr:
                    garage = Garage.query.get(removeId)
                    try:
                        db.session.delete(garage)
                        db.session.commit()
                    except:
                        print('failed at deleting a garage') 

    bedrooms = Bedroom.query.filter(Bedroom.house_id == houseId).all()
    kitchens = Kitchen.query.filter(Kitchen.house_id == houseId).all()
    livingrooms = Living.query.filter(Living.house_id == houseId).all()
    bathrooms = Bath.query.filter(Bath.house_id == houseId).all()
    garages = Garage.query.filter(Garage.house_id == houseId).all()
    bedroom_qty = len(Bedroom.query.filter(Bedroom.house_id == houseId).all())
    kitchen_qty = len(Kitchen.query.filter(Kitchen.house_id == houseId).all())
    livingroom_qty = len(Living.query.filter(Living.house_id == houseId).all())
    bathroom_qty = len(Bath.query.filter(Bath.house_id == houseId).all())
    garage_qty = len(Garage.query.filter(Garage.house_id == houseId).all())

    if house.date_market != None:
        house.date_m = house.date_market.strftime("%Y-%m-%d")
    else:
        house.date_m = ""
    if house.date_sale != None:
        house.date_s = house.date_sale.strftime("%Y-%m-%d")
    else:
        house.date_s = ""
    return render_template('details.html', house=house, bedroom_qty=bedroom_qty, bedrooms=bedrooms, kitchen_qty=kitchen_qty, kitchens=kitchens, livingroom_qty=livingroom_qty, livingrooms=livingrooms, bathroom_qty=bathroom_qty, bathrooms=bathrooms, garage_qty=garage_qty, garages=garages)

def ConvertBool(input):
    if input == "0":
        return 0
    elif input == "1":
        return 1
    else:
        return None

def ConvertNumber(input):
    output = None

    if input != None and len(input) > 0:
        try:
            output = float(input)
        except:
            output = None
    else:
        output = None

    return output

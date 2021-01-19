from . import db

class House(db.Model):
    __tablename__='houses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500), unique=True)
    suburb = db.Column(db.String(64),nullable=False)
    link = db.Column(db.String(255),nullable=True)
    # Final Sale Price
    price_ask = db.Column(db.Float, nullable=True)
    # Final Sale Price
    price_sale = db.Column(db.Float, nullable=True)
    # Date Placed on Market
    date_market = db.Column(db.DateTime, nullable=True)
    # Date Sold
    date_sale = db.Column(db.DateTime, nullable=True)
    
    # Construction Material: 1 = wood, 2 = brick, 3 = other.
    construction_mat = db.Column(db.Integer, nullable=True) 
    # Land Size: square meters.
    land_size = db.Column(db.Integer, nullable=True)
    # House Size : square meters.
    house_size = db.Column(db.Integer, nullable=True)
    # Street Type: 1 = main road, 2 = busy road, 3 = quiet road, 4 = dead end.
    street_type = db.Column(db.Integer, nullable=True)
    # Roof Material: 1 = corrugated iron, 2 = tile, 3 = other.
    roof_mat = db.Column(db.Integer, nullable=True)
    # Roof Condition: 1 = poor, 2 = good.
    roof_cond = db.Column(db.Integer, nullable=True)
    # Insulation: true/yes or false/no.
    insulation = db.Column(db.Boolean, nullable=True)
    # Driveway Condition: 1 = poor, 2 = good.
    driveway_cond = db.Column(db.Integer, nullable=True)
    # Fenced Yard: 1 = none/incomplete, 2 = back only, 3 = fully fenced.
    fenced = db.Column(db.Integer, nullable=True)
    # Fence Condition: 1 = no fence, 2 = poor, 3 = mixed, 4 = good.
    fence_cond = db.Column(db.Integer, nullable=True)
    # Backyard Size: 1 = none, 2 = small, 3 = medium, 4 = large.
    backyard_size = db.Column(db.Integer, nullable=True)
    # Yard Level?: 1 = no yard, 2 = unlevel, 3 = partially level, 4 = level.
    yard_level = db.Column(db.Integer, nullable=True)
    # Landscaping: 1 = poor, 2 = good, high maintenance, 3 = good, low maintenance.
    landcaping_cond = db.Column(db.Integer, nullable=True)
    # Pool: 1 = none, 2 = old, 3 = new.
    pool = db.Column(db.Integer, nullable=True)
    # Pool Type: 1 = chlorine, 2 = salt, 3 = bromine.
    pool_type = db.Column(db.Integer, nullable=True)
    # Pool Construction: 1 = Inground, 2 = Above Ground, 3 = above ground, in the ground.
    pool_construction = db.Column(db.Integer, nullable=True)
    # Pool Filter: 1 = cartridge, 2 = sand, 3 = glass.
    pool_filter = db.Column(db.Integer, nullable=True)
    # Pool Cleaner: 1 = none, 2 = creepy crawly, 3 = robot.
    pool_cleaner = db.Column(db.Integer, nullable=True)

    # Plumbing and Electrical accessible under house: Boolean.
    underhouse_access = db.Column(db.Boolean, nullable=True)
    # Renovations and Extensions have council approval: Boolean.
    council_approval = db.Column(db.Boolean, nullable=True)
    # Large Cracks in Building: 1 = none, 2 = single, 3 = multiple.
    cracks = db.Column(db.Integer, nullable=True)
    # Roof Lines Straight?: Boolean.
    roof_lines = db.Column(db.Boolean, nullable=True)
    # Gutters Condition: 1 = rusty, 2 = blocked, 3 = good.
    gutters_cond = db.Column(db.Integer, nullable=True)
    # Downpipes: 1 = evidence of flooding at base, 2 = drain to ground, 3 = drain to soak well.
    downpipes = db.Column(db.Integer, nullable=True)
    # Trees close to house: 1 = none, 2 = small, 3 = large.
    trees = db.Column(db.Integer, nullable=True)
    # Outside Electrics Condition: 1 = none, 2 = loose or broken power points or cables, 3 = good.
    outside_elec_cond = db.Column(db.Integer, nullable=True)
    # Flood Zone: Boolean.
    flood_zone = db.Column(db.Boolean, nullable=True)
    # Sewage: 1 = separate, 2 = connects to combined, 3 = is combine.
    sewage = db.Column(db.Integer, nullable=True)
    # Additional Notes: String.
    notes = db.Column(db.String(500), nullable=True)


    

    def __repr__(self):
        str = "Id: {}, address: {}\n" 
        str =str.format( self.id, self.address)
        return str



class Room(db.Model):
    __tablename__='rooms'
    id = db.Column(db.Integer, primary_key=True)
    # Size: 1 = small, 2 = medium, 3 = large.
    size = db.Column(db.Integer, nullable=True) 
    # Floor Material: 1 = wood, 2 = tile, 3 = carpet, 4 = lino, 5 = concrete, 6 = other.
    floor_mat = db.Column(db.Integer, nullable=True) 
    # Layout: 1 = poor, 2 = good.
    layout = db.Column(db.Integer, nullable=True) 
    # Power Points, Number/Location/quality: 1 = bad locations, 2 = old style, 3 = good location and updated.
    power_points = db.Column(db.Integer, nullable=True) 
    # Door Close Easily?: 1 = jams or sticks, 2 = door operates correctly.
    door_close = db.Column(db.Integer, nullable=True) 
    # Natural Lighting: 1 = dark, 2 = adequate, 3 = bright.
    light_natural = db.Column(db.Integer, nullable=True) 
    # Artificial Lighting: 1 = poor, 2 = good, 3 = good (LED).
    light_artificial = db.Column(db.Integer, nullable=True) 
    # Window Operation: 1 = sticks/jams, 2 = opens and closes easily.
    window_op = db.Column(db.Integer, nullable=True) 
    # Fly Screens: 1 = none, 2 = poor quality, 3 = good quality.
    fly_screens = db.Column(db.Integer, nullable=True) 
    # Walls with windows: Integer from 0 to 3.
    wall_windows_qty = db.Column(db.Integer, nullable=True) 
    # Window Wall 1 Direction: Integer 1 to 16. N, NNE, NE, NEE, E, SEE, SE, SSE, S, SSW, SW, SWW, W, NWW, NW, NNW.
    window_dir_1 = db.Column(db.Integer, nullable=True) 
    # Window Wall 2 Direction: Integer 1 to 16. N, NNE, NE, NEE, E, SEE, SE, SSE, S, SSW, SW, SWW, W, NWW, NW, NNW.
    window_dir_2 = db.Column(db.Integer, nullable=True) 
    # Window Wall 3 Direction: Integer 1 to 16. N, NNE, NE, NEE, E, SEE, SE, SSE, S, SSW, SW, SWW, W, NWW, NW, NNW.
    window_dir_3 = db.Column(db.Integer, nullable=True) 
    # Sagging Ceiling?: Boolean.
    ceiling_sag = db.Column(db.Boolean, nullable=True) 
    # Signs of Moisture: 1 = none, 2 = mold, 3 = peeling paint, 4 = other.
    moisture = db.Column(db.Integer, nullable=True) 
    # Plasterboard, fine cracks (map cracking): Boolean.
    plasterboard_defects = db.Column(db.Boolean, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str


class Bedroom(db.Model):
    __tablename__='bedrooms'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship("Room")
    # Ceiling Fan: 1 = none, 2 = old, 3 = new.
    fan = db.Column(db.Integer, nullable=True) 
    # Air Conditioning: 1 = none, 2 = old, 3 = new.
    ac = db.Column(db.Integer, nullable=True) 
    # Blinds: 1 = none, 2 = non-blackout, 3 = blackout (poor condition), 4 = blackout (good condition).
    blinds = db.Column(db.Integer, nullable=True) 
    # Wardrobe: 1 = none, 2 = small, 3 = large, 4 = walk-in.
    wardrobe = db.Column(db.Integer, nullable=True) 
    # Walk-in Wardrobe: 1 = none, 2 = none but space to build one, 3 = small, 4 = large.
    walk_in = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str


class Kitchen(db.Model):
    __tablename__='kitchens'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship("Room")
    # Ceiling Fan: 1 = none, 2 = old, 3 = new.
    fan = db.Column(db.Integer, nullable=True) 
    # Air Conditioning: 1 = none, 2 = old, 3 = new.
    ac = db.Column(db.Integer, nullable=True) 
    # Overall Quality: 1 = needs immediate update, 2 = dated, 3 = modern.
    quality = db.Column(db.Integer, nullable=True) 
    # Bench Material: 1 = lino, 2 = wood, 3 = stone/granite, 4 = concrete.
    bench_mat = db.Column(db.Integer, nullable=True) 
    # Bench Space: 1 = small, 2 = adequate, 3 = plentiful.
    bench_space = db.Column(db.Integer, nullable=True) 
    # Cupboard Space: 1 = lacking, 2 = adequate, 3 = plentiful.
    cupboard_space = db.Column(db.Integer, nullable=True) 
    # Pantry Space: 1 = none, 2 = small, 3 = large, 4 = walk-in.
    pantry_space = db.Column(db.Integer, nullable=True) 
    # Oven Size: 1 = small, 2 = large.
    oven_size = db.Column(db.Integer, nullable=True) 
    # Cooktop: 1 = old electric, 2 = new electric, 3 = induction, 4 = gas.
    cooktop = db.Column(db.Integer, nullable=True) 
    # Sink: 1 = small, 2 = large, 3 = farmhouse.
    sink = db.Column(db.Integer, nullable=True) 
    # Water Pressure: 1 = poor, 2 = good.
    water_pressure = db.Column(db.Integer, nullable=True) 
    # Hot Water Lag: seconds.
    hot_water_lag = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str


class Living(db.Model):
    __tablename__='living_rooms'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship("Room")
    # Ceiling Fan: 1 = none, 2 = old, 3 = new.
    fan = db.Column(db.Integer, nullable=True) 
    # Air Conditioning: 1 = none, 2 = old, 3 = new.
    ac = db.Column(db.Integer, nullable=True) 
    # Ariel Location: 1 = not practical, 2 = practical.
    ariel = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str


class Bath(db.Model):
    __tablename__='bathrooms'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship("Room")
    # Toilet Condition: 1 = none, 2 = poor, 3 = good.
    toilet_cond = db.Column(db.Integer, nullable=True) 
    # Shower Condition: 1 = none, 2 = poor, 3 = average, 4 = good.
    shower_cond = db.Column(db.Integer, nullable=True) 
    # Shower Size: 1 = small, 2 = large.
    shower_size = db.Column(db.Integer, nullable=True) 
    # Shower Head: 1 = poor, 2 = good.
    shower_head = db.Column(db.Integer, nullable=True) 
    # Sink Condition: 1 = poor, 2 = good.
    sink_cond = db.Column(db.Integer, nullable=True) 
    # Water Pressure: 1 = poor, 2 = good.
    water_pressure = db.Column(db.Integer, nullable=True) 
    # Hot Water Lag: seconds.
    hot_water_lag = db.Column(db.Integer, nullable=True) 
    # Extraction Fan: 1 = none, 2 = noisy, 3 = good
    extraction_fan = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str


class Garage(db.Model):
    __tablename__='garages'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    # Garage Type: 1 = carport, 2 = garage.
    garage_type = db.Column(db.Integer, nullable=True) 
    # Quanty of Car Spaces: Integer
    cars = db.Column(db.Integer, nullable=True) 
    # Garage Condition: 1 = poor, 2 = good.
    garage_cond = db.Column(db.Integer, nullable=True)
    # Garage Door: 1 = none, 2 = manual, 3 = auto.
    door = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        str = "Id: {}\n" 
        str =str.format( self.id)
        return str
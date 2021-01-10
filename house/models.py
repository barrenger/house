from . import db

class House(db.Model):
    __tablename__='house'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500), unique=True)
    price = db.Column(db.Float, nullable=True)
    #construction = db.Column(db.Integer, nullable=False)
    #landsize = db.Column(db.Integer, nullable=False)
    #street = db.Column(db.Integer, nullable=False)
    #notes = db.Column(db.String(500), nullable=True)
    

    def __repr__(self):
        str = "Id: {}, address: {}\n" 
        str =str.format( self.id, self.address)
        return str

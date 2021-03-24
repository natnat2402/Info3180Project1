from . import db
from werkzeug.security import generate_password_hash

class PropertyInformation(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Property_Information'

    Property_id = db.Column(db.Integer,primary_key=True)
    Title = db.Column(db.String(20))
    Number_of_Bedrooms = db.Column(db.Integer)
    Number_of_Bathrooms = db.Column(db.Integer)
    Location = db.Column(db.String(80))
    Price = db.Column(db.Integer)
    Property_type = db.Column(db.String(12))
    Description = db.Column(db.String(80))
    Photo = db.Column(db.String(200))

    def __init__(self,Title,Number_of_Bedrooms,Number_of_Bathrooms,Location,Price,Property_type,Description,Photo):
        self.Title = Title
        self.Number_of_Bedrooms = Number_of_Bedrooms
        self.Number_of_Bathrooms = Number_of_Bathrooms
        self.Location = Location
        self.Price = Price
        self.Property_type = Property_type 
        self.Description = Description
        self.Photo = Photo
        
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

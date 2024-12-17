from app import db
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False)
    email = db.Column(db.String(20), unique=True)
    # date_joined = db.Column(db.Date,default = datetime.datetime().now())
    # date_joined = db.Column(db.Date,default =  = forms.DateTimeField())

    def __repr__(self):
        return self.first_name

# class Spa(db.Model):
#     spa_id = db.Column(db.Integer,primary_key = True)
#     spa_name = db.Column(db.String(20),unique = True)
#     spa_add = db.Column(db.String(20),unique = True)
#     spa_services = db.Column(db.String(30))

#     def __repr__(self):
#         return self.spa_name
# from models.models import Users

from flask import Flask, redirect, render_template,request
from flask.app import T_template_filter
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate
from sqlalchemy.orm import mapped_column,Mapped
# from sympy import true

# from main import app, db


app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

"""
init , migrate , upgrade the flask db to make migrations 
"""
# akjfhajsdf

# class Services(db.Model):
#     id = db.Column(db.Integer,primary_key = True,autoincrement = True)
#     first_name = db.Column(db.String(20))
#     email = db.Column(db.String(20))
#     trainer_id = db.Column(db.Integer)

# class Trainer(db.Model):
#     id = db.Column(db.Integer,primary_key = True,autoincrement = True)
#     trainer_name = db.Column(db.String(20))
#     user_name = db.Column(db.String(20))

#     def __repr__(self):
#         return self.trainer_name

class Spa_Service(db.Model):
    service_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(100))

class Service_Providers(db.Model):
    service_provider_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    service_id = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name},{self.experience},{self.cost}"


migrate = Migrate(app,db)

@app.route('/')
def index():
    users = Spa_Service.query.all()
    return render_template('index.html',users = users)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add_data',methods = ['POST'])
def add_data():
    id = request.form.get('id')
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    u = Spa_Service(id = id,first_name=first_name,email=email)
    db.session.add(u)
    db.session.commit()
    return redirect('/')

@app.route(f'/delete/<id>')
def delete(id):
    Spa_Service.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/')

@app.route('/trainers/<id>')
def trainers(id):
    # print(service)
    filt_trainers = Service_Providers.query.filter_by(service_id = id).all()
    return render_template('trainers.html',trainers = filt_trainers)

@app.template_filter('get_length')
def get_length(a):
    return len(a)
if __name__ == '__main__':
    app.run()


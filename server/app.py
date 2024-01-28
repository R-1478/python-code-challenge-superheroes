#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Hero, Power, db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/heroes', methods= ['GET'])
def get_heroes():
    heroes = Hero.query.all()
    for hero in heroes:
        result = [
            {"name": hero.name,"id": hero.id , "super_name": hero.super_name}
        ]
        
        return result
    
    response = make_response(jsonify(result))
    # response.headers['Custom-Header'] = 'SomeValue'

    return response

@app.route('/powers/<int:id>')
def powers_by_id():
    powers = Power.query.filter_by(id=id).first()

    result = powers.query().all()

    response = make_response(jsonify(result))

    return response




    


if __name__ == '__main__':
    app.run(port=5555)

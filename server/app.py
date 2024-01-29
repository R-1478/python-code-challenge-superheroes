#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import Hero, Power, db, HeroPowers




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "<h1>Superheroes</h1>"


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()

    result = [
        {"name": hero.name, "id": hero.id, "super_name": hero.super_name}
        for hero in heroes
    ]
    

    response = make_response(jsonify(result))
    

    return response

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.filter_by(id=id).first()

    if hero:
        result = {
            "name": hero.name, "id": hero.id, "super_name": hero.super_name}
        response = make_response(jsonify(result))
    else:
        response = make_response(jsonify({"error":"Hero not found"}), 404)

    return response

@app.route('/powers', methods=['GET'])
def powers():
    powers = Power.query.all()
    result = [
        {"id": power.id, "name": power.name,"description": power.description}
        for power in powers
    ]
    response =  make_response(jsonify(result))

    return response


@app.route('/powers/<int:id>', methods=['GET'])
def powers_by_id(id):  
    power = Power.query.filter_by(id=id).first()

    if power:
        result = {
            "id": power.id,
            "name": power.name,
            "description": power.description
            
        }
        response = make_response(jsonify(result))
    else:
        response = make_response(jsonify({"error": "Power not found"}), 404)

    return response

@app.route('/powers/<int:id>', methods=['PATCH'])
def patch_power(id):
    power = Power.query.filter_by(id=id).first()
    if power is None:
        # Return an error response if the power does not exist
        return make_response(jsonify({"error": "Power not found"}), 404)
    else:
    # Parse the JSON data from the request body
        data = request.get_json()

    # Update the power's description if provided in the request
    if 'description' in data:
        power.description = data['description']

    # Validate and update the power in the database
    try:
        db.session.commit()
        # Return the updated power data
        result = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        return jsonify(result)

    except Exception as e:
        # Return an error response if the update fails
        return make_response(jsonify({"errors": ["Validation errors"]}), 400)

@app.route('/hero_powers', methods=['POST'])
def hero_powers():
    data = request.get_json()
    
    if data:
        # Check if the 'strength' value is valid
        valid_strengths = ['Strong', 'Weak', 'Average']
        if data['strength'] not in valid_strengths:
            return make_response(jsonify({"errors": ["Invalid strength value"]}), 422)
        else:
            hero_power = HeroPowers(strength=data["strength"], power_id=data["power_id"], hero_id=data["hero_id"])
            db.session.add(hero_power)
            db.session.commit()

        my_hero = Hero.query.filter_by(id=hero_power.hero_id).first()
        response = make_response(jsonify(my_hero))

        return response
    else:
        return make_response(jsonify({"errors": ["Validation errors"]}), 400)

    


if __name__ == '__main__':
    app.run(port=5000)

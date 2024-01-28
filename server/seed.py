from app import app

from models import Hero, Power, db

# app = create_app()
# db = SQLAlchemy(app)

with app.app_context():
    # Seeding logic for Powers
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for power_info in powers_data:
        power = Power.query.filter_by(name=power_info["name"]).first()
        if not power:
            power = Power(name=power_info["name"], description=power_info["description"])
            db.session.add(power)

    db.session.commit()

    # Seeding logic for Heroes
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    for hero_info in heroes_data:
        hero = Hero.query.filter_by(name=hero_info["name"]).first()
        if not hero:
            hero = Hero(name=hero_info["name"], super_name=hero_info["super_name"])
            db.session.add(hero)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")

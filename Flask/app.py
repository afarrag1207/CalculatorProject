import json

from flask import request

from . import create_app
from .models import Cats, db




app = create_app() # this command creates our app by calling the 'create_app()' function from __init__.py


@app.route('/', methods=['GET'])
def fetch():
    cats = Cats.Query.all() # This command retrieves every row in the table 'cats'.
    all_cats = []  # This creates a string
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    cat = Cats(name=name, price=price, breed=breed)
    db.session.add(cat)
    db.session.commit()
    return json.dumps("Added"), 200


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    Cats.query.filter_by(id=cat_id).delete()
    db.session.commit()
    return json.dumps("Deleted"), 200

@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    cat_to_update = Cats.query.filter_by(id=cat_id).all()[0]
    cat_to_update.price = new_price
    db.session.commit()
    return json.dumps("Edited"), 200

# this also defines four functions:
# GET: get information about all the cats
# POST: Add a new cat
# DELETE: Remove a cat
# Patch: Edit a cat's price


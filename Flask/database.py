from .models import db

# this model is created so we can abstract away from how we interact with the database.
# this function is used to interact with the database.
# this also means that if we need to change how we interact with the database.
# we only have to change it in a this module.

def get_all(model):
    data = model.query.all()
    return data

def add_instance(model, **kwargs):  # some functions use **kwargs(keyword arguments) could be called anything
    instance = model(**kwargs)      # could be called anuthing but its best practice to call it 'kwargs'.
    db.session.add(instance)        # **kwargs allows the caller of the function to pass in an arbitrary number of keyword arguments.
    commit_changes()

# NOTE: The kwargs just stores the argument as a dictionary, the '**' operator unpacks our dictionary and passes them as key arguments


def delete_instance(model, id):
    model. query.filter_by(id=id).delete()
    commit_changes()

def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    commit_changes()

def commit_changes():
    db.session.commit()

# the app.py module calls functions in this file to interact with database.py
# GET: get_all()
#POST: add_instance()
#Delete: delete_instance()
#PUT: edit_instance()

# Creating enteries into the tables
from model import db, Puppy, Owner, Toy, app
# creating two puppies
with app.app_context():
    rufus = Puppy('Rufus')
    fido = Puppy('fido')

    # add puppies to db
    db.session.add_all([rufus, fido])
    db.session.commit()

    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name='Rufus').first()

    # creating owner object
    jose = Owner('Jose', rufus.id)

    # give rufus some toys
    toy1 = Toy('Chew Toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([jose, toy1, toy2])
    db.session.commit()

    # grab rufus after those additions
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    rufus.report_toys()

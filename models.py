from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Drug(db.Model):
    __tablename__ = 'drugs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    # many to one with price


class Pharmacy(db.Model):
    __tablename__ = 'pharmacies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, unique=True)

    address = db.Column(db.Text)

    # many to one with price


class Price(db.Model):
    __tablename__ = 'prices'

    drug_name = db.Column(db.Text, db.ForeignKey(
        'drugs.name'), primary_key=True)

    pharmacy_name = db.Column(db.Text, db.ForeignKey(
        'pharmacies.name'), primary_key=True)

    price = db.Column(db.Integer, nullable=False)

    drugs = db.relationship("Drug", backref="price")
    pharmacies = db.relationship("Pharmacy", backref="price")
    # put relationships here
    # one to many with other tables

    """ def serialize(self):
        return {
            'name': self.drug_name,
            'pharmacy': self.pharmacy_name,
            'price': self.price
        } """


""" class User(db.Model):
    

    __tablename__ = 'users'

    username = db.Column(db.String, nullable=False,
                         unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        
        hashed = bcrypt.generate_password_hash(pwd)

        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, pwd):
        

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False """

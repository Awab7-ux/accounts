"""Account model"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """Initialize database"""
    db.init_app(app)
    with app.app_context():
        db.create_all()


class Account(db.Model):
    """Account table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    address = db.Column(db.String(256))
    phone_number = db.Column(db.String(32), nullable=True)
    date_joined = db.Column(db.String(32))

    def serialize(self):
        """To dict"""
        return {
            "id": self.id, "name": self.name, "email": self.email,
            "address": self.address, "phone_number": self.phone_number,
            "date_joined": self.date_joined,
        }

    def deserialize(self, data):
        """From dict"""
        self.name = data["name"]
        self.email = data["email"]
        self.address = data["address"]
        self.phone_number = data.get("phone_number")
        self.date_joined = data.get("date_joined")

from base import db


class Parts(db.Model):
    __tablename__ = "Parts"

    id = db.Column(db.Integer, primary_key=True)
    serial_num = db.Column(db.String)
    order_num = db.Column(db.String)
    quality = db.Column(db.Integer)
    date = db.Column(db.String)
    plant = db.Column(db.String)


class ParameterList(db.Model):
    __tablename__ = "ParameterList"

    id = db.Column(db.Integer, primary_key=True)
    id_parts = db.Column(db.Integer, db.ForeignKey('Parts.id'))
    actual_value = db.Column(db.String)
    unit = db.Column(db.String)
    description = db.Column(db.String)
    quality = db.Column(db.Integer)
    station = db.Column(db.String)
    type = db.Column(db.Integer)


def create_tables():
    db.create_all()

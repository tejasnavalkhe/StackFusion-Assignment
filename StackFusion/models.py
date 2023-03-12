from StackFusion import db
import pytz

tz = pytz.timezone("Asia/Calcutta")

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)

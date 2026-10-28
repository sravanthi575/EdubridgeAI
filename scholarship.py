from extensions import db


class Scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    provider = db.Column(db.String(200), default="")
    category = db.Column(db.String(40), default="Scholarship", index=True)
    eligibility = db.Column(db.Text, default="")
    deadline = db.Column(db.String(120), default="")      # free text, e.g. "See official site"
    link = db.Column(db.String(500), nullable=False)       # official application / info link
    last_verified = db.Column(db.Date, nullable=True)      # None = not verified yet

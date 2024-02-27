from cfg import db
from flask_login import UserMixin


class Brief(db.Model):
    __tablename__ = "brief"
    id = db.Column(db.Integer, primary_key=True)
    text1 = db.Column(db.String(50), nullable=True, default="")
    text2 = db.Column(db.String(100), nullable=True, default="")
    text3 = db.Column(db.String(50), nullable=True, default="")
    text4 = db.Column(db.String(100), nullable=True, default="")
    text5 = db.Column(db.String(100), nullable=True, default="")

    prod = db.Column(db.Boolean, nullable=True, default=False)
    posl = db.Column(db.Boolean, nullable=True, default=False)
    rek = db.Column(db.Boolean, nullable=True, default=False)
    pokr = db.Column(db.Boolean, nullable=True, default=False)
    seo = db.Column(db.Boolean, nullable=True, default=False)
    rebr = db.Column(db.Boolean, nullable=True, default=False)

    text9 = db.Column(db.String(100), nullable=True, default="")
    text10 = db.Column(db.String(100), nullable=True, default="")
    text11 = db.Column(db.String(100), nullable=True, default="")
    text12 = db.Column(db.String(100), nullable=True, default="")

    brand = db.Column(db.String(100), nullable=True, default="")

    text14 = db.Column(db.String(100), nullable=True, default="")

    korp = db.Column(db.Boolean, nullable=True, default=False)
    yask = db.Column(db.Boolean, nullable=True, default=False)
    poz = db.Column(db.Boolean, nullable=True, default=False)
    zobr = db.Column(db.Boolean, nullable=True, default=False)
    dinam = db.Column(db.Boolean, nullable=True, default=False)
    stat = db.Column(db.Boolean, nullable=True, default=False)
    mini = db.Column(db.Boolean, nullable=True, default=False)
    funk = db.Column(db.Boolean, nullable=True, default=False)

    text16 = db.Column(db.String(100), nullable=True, default="")
    text17 = db.Column(db.String(100), nullable=True, default="")
    text18 = db.Column(db.String(100), nullable=True, default="")

    feedb = db.Column(db.Boolean, nullable=True, default=False)
    pop = db.Column(db.Boolean, nullable=True, default=False)
    nov = db.Column(db.Boolean, nullable=True, default=False)
    faq = db.Column(db.Boolean, nullable=True, default=False)
    analit = db.Column(db.Boolean, nullable=True, default=False)
    crm = db.Column(db.Boolean, nullable=True, default=False)
    mon = db.Column(db.Boolean, nullable=True, default=False)

    napov = db.Column(db.Boolean, nullable=True, default=False)

    text21 = db.Column(db.String(100), nullable=True, default="")

    dom = db.Column(db.Boolean, nullable=True, default=False)

    text23 = db.Column(db.String(100), nullable=True, default="")
    text24 = db.Column(db.String(100), nullable=True, default="")
    text25 = db.Column(db.String(100), nullable=True, default="")
    text26 = db.Column(db.String(100), nullable=True, default="")


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(24), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

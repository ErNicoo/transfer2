from app.extensions.database import db, CRUDMixin

class Project(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    picture_url = db.Column(db.String(260))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id', name='member_of_project'))

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
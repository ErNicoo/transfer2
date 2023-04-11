from app.extensions.database import db

class UserAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    page_name = db.Column(db.String(100))
    page_views = db.Column(db.Integer)
    time_spent_on_page = db.Column(db.Integer)
from flask import Blueprint, render_template, request
from .models import UserAnalytics
from app.extensions.database import db

blueprint = Blueprint('analytics', __name__)

@blueprint.route('/analytics', methods=['POST'])
def store_user_analytics():
    user_id = request.form['user_id']
    page_name = request.form['page_name']
    page_views = request.form['page_views']
    time_spent_on_page = request.form['time_spent_on_page']
    user_analytics = UserAnalytics(user_id=user_id, page_name=page_name, page_views=page_views, time_spent_on_page=time_spent_on_page)
    db.session.add(user_analytics)
    db.session.commit()
    return 'User analytics data stored successfully!'
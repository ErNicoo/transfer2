from dotenv import load_dotenv
import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# PROJECTS_PER_PAGE = 4

load_dotenv()
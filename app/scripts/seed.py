from app.app import create_app
from app.pages.models import Project
from app.extensions.database import db

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

projects_data = {
  'cream-design' : {'name': 'cream design'},
  'ebay-kleinanzeigen' : {'name': 'ebay kleinanzeigen'},
  'design-research' : {'name': 'design research'}
}

for slug, project in projects_data.items():
    new_project = Project(slug=slug, name=project['name'])
    db.session.add(new_project)

db.session.commit()
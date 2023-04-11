from app.extensions.database import db
from app.pages.models import Project

def test_project_update(client):
    project = Project(slug='cream-design', name='cream design')
    db.session.add(project)
    db.session.commit()

    project.name = 'design research'
    project.save()

    updated_project = Project.query.filter_by(slug='cream-design').first()
    assert updated_project.name == 'design research'

def test_project_delete(client):
    project = Project(slug='cream-design', name='cream design')
    db.session.add(project)
    db.session.commit()

    project.delete()

    deleted_project = Project.query.filter_by(slug='butter').first()
    assert deleted_project is None
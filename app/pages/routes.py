from flask import Blueprint, render_template, request, redirect, url_for
from .models import Project
from app.extensions.database import db

blueprint = Blueprint('pages', __name__)

@blueprint.route('/projects')
def projects():
  all_projects = Project.query.all()
  return render_template('pages/index.html', projects=all_projects)

@blueprint.route('/projects/<slug>')
def project(slug):
  project = Project.query.filter_by(slug=slug).first_or_404()
  return render_template('pages/projects-page.html', project=project)

@blueprint.route('/create', methods=['GET', 'POST'])
def create_project():
  if request.method == 'POST':
    name = request.form['name']
    slug = request.form['name']
    creation = Project(name=name, slug=slug)
    db.session.add(creation)
    db.session.commit()
    return redirect(url_for('pages.projects'))
  return render_template('pages/create.html')

@blueprint.route('/edit/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
  creation = Project.query.get(project_id)
  if request.method == 'POST':
    creation.name = request.form['name']
    creation.slug = request.form['name']
    db.session.commit()
    return redirect(url_for('pages.projects'))
  return render_template('pages/edit.html', creation=creation)

@blueprint.route('/delete/<int:project_id>', methods=['GET', 'POST'])
def delete_project(project_id):
    cancell = Project.query.get(project_id)
    if request.method == 'POST':
      db.session.delete(cancell)
      db.session.commit()
      return redirect(url_for('pages.projects'))
    return render_template('pages/delete.html', cancell=cancell)

@blueprint.route('/run-seed')
def run_seed():
    if not Project.query.filter_by(slug='cream-design').first():
      import app.scripts.seed
      return 'Database seed completed!'
    else:
      return 'Nothing to run.'
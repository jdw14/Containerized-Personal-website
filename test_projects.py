import os
import sqlite3

import pytest

import DAL
from app import app as flask_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Point DAL.DB_PATH to a temp DB so tests are isolated
    temp_db = tmp_path / "test_projects.db"
    monkeypatch.setattr(DAL, 'DB_PATH', temp_db)
    DAL.init_db()

    flask_app.config['TESTING'] = True
    with flask_app.test_client() as c:
        yield c


def test_projects_page_shows_no_projects(client):
    rv = client.get('/projects')
    assert rv.status_code == 200
    # When no projects, the template should still render; look for 'projects' word
    assert b"projects" in rv.data.lower() or b"project" in rv.data.lower()


def test_add_project_route(client):
    # Post minimal valid data
    rv = client.post('/add_project', data={
        'projectTitle': 'NewProj',
        'projectDescription': 'Desc',
        'projectImageFile': 'img.png'
    }, follow_redirects=True)

    assert rv.status_code == 200
    # After adding, projects page should contain the title
    assert b'NewProj' in rv.data

import os

import pytest

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    # Use a separate DB for tests by setting environment before import in app if needed
    with flask_app.test_client() as c:
        yield c


def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome" in rv.data or b"Home" in rv.data or b"About" in rv.data


def test_about_and_resume(client):
    for route in ('/about', '/resume', '/contact', '/thankyou'):
        rv = client.get(route)
        assert rv.status_code == 200

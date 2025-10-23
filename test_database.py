import os
import tempfile
import sqlite3
from pathlib import Path

import pytest

import DAL


def test_init_db_creates_file(tmp_path, monkeypatch):
    # Use a temp DB file path so we don't touch the real one
    temp_db = tmp_path / "test_projects.db"
    monkeypatch.setattr(DAL, 'DB_PATH', temp_db)

    # Ensure file does not exist yet
    assert not temp_db.exists()

    # Initialize DB
    DAL.init_db()

    # File should now exist
    assert temp_db.exists()

    # Table should exist and accept inserts
    conn = sqlite3.connect(temp_db)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
    assert cur.fetchone() is not None
    conn.close()


def test_add_and_get_project(tmp_path, monkeypatch):
    temp_db = tmp_path / "test_projects.db"
    monkeypatch.setattr(DAL, 'DB_PATH', temp_db)
    DAL.init_db()

    # Add a project
    DAL.add_project('T1', 'D1', 'img.png')

    projects = DAL.get_all_projects()
    assert isinstance(projects, list)
    assert len(projects) == 1
    p = projects[0]
    assert p['title'] == 'T1'
    assert p['description'] == 'D1'
    assert p.get('imagefile') == 'img.png'

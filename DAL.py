import sqlite3
from pathlib import Path

# Path to database file next to this module
DB_PATH = Path(__file__).parent / 'projects.db'


def get_connection():
    """Return a sqlite3 connection with row access by name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the projects table if it does not exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
        '''
    )

    # Ensure imagefile column exists (add if missing) - simple migration
    cur.execute("PRAGMA table_info(projects)")
    cols = [r[1] for r in cur.fetchall()]
    if 'imagefile' not in cols:
        try:
            cur.execute('ALTER TABLE projects ADD COLUMN imagefile TEXT')
        except Exception:
            # if alteration fails for some reason, ignore - table may already be correct
            pass
    conn.commit()
    conn.close()


def get_all_projects():
    """Return a list of projects as dictionaries ordered by id desc."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, imagefile FROM projects ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    out = []
    for r in rows:
        # Normalize keys to lowercase expected names (handle existing DBs with different casing)
        d = {}
        for k in r.keys():
            lower = k.lower()
            if lower == 'title' or lower == 'title':
                d['title'] = r[k]
            elif lower == 'description':
                d['description'] = r[k]
            elif lower == 'imagefile' or lower == 'image_file':
                d['imagefile'] = r[k]
            else:
                d[lower] = r[k]
        out.append(d)
    return out


def add_project(title, description, imagefile=None):
    """Insert a new project record."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO projects (title, description, imagefile) VALUES (?, ?, ?)', (title, description, imagefile))
    conn.commit()
    conn.close()

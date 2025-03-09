import psycopg2
from config import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)
c = conn.cursor()

def init_db():
    c.execute("""
        CREATE TABLE IF NOT EXISTS standup_responses (
            id SERIAL PRIMARY KEY,
            user_id TEXT,
            date DATE,
            yesterday_tasks TEXT,
            today_tasks TEXT,
            pending_tasks TEXT,
            difficulty_level TEXT,
            status TEXT,
            jira_ticket TEXT
        )
    """)
    conn.commit()

init_db()


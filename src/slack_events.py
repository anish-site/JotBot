from slack_bolt import App
from config import SLACK_BOT_TOKEN
from ai_analysis import analyze_task
from database import conn, c
from datetime import datetime

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mention(event, say):
    say("Hey there! I'm JotBot ✏️. I'll help with daily standups!")

@app.message("standup")
def ask_standup_questions(message, say):
    user_id = message['user']
    say(f"<@{user_id}> What did you complete yesterday?")

def store_response(user_id, yesterday_tasks=None, today_tasks=None, pending_tasks=None, difficulty_level=None, status=None, jira_ticket=None):
    date = str(datetime.today().date())
    c.execute("SELECT * FROM standup_responses WHERE user_id = %s AND date = %s", (user_id, date))
    existing_entry = c.fetchone()
    
    if existing_entry:
        c.execute("""
            UPDATE standup_responses
            SET yesterday_tasks = COALESCE(%s, yesterday_tasks),
                today_tasks = COALESCE(%s, today_tasks),
                pending_tasks = COALESCE(%s, pending_tasks),
                difficulty_level = COALESCE(%s, difficulty_level),
                status = COALESCE(%s, status),
                jira_ticket = COALESCE(%s, jira_ticket)
            WHERE user_id = %s AND date = %s
        """, (yesterday_tasks, today_tasks, pending_tasks, difficulty_level, status, jira_ticket, user_id, date))
    else:
        c.execute("""
            INSERT INTO standup_responses (user_id, date, yesterday_tasks, today_tasks, pending_tasks, difficulty_level, status, jira_ticket)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, date, yesterday_tasks, today_tasks, pending_tasks, difficulty_level, status, jira_ticket))
    
    conn.commit()


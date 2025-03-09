import logging
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_events import app
from config import SLACK_APP_TOKEN

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


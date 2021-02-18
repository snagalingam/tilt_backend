import os
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError


#Initialize a Web API client
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


################################################################################
# Standard message
################################################################################
try:
    response = client.chat_postMessage(channel='#eng', text="Hi World! I'm the new Tilt bot")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")

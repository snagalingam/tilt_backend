import os
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError


#Initialize a Web API client
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


################################################################################
# Sends a notification to Slack when an award letter has been uploaded
# THis helps us track if the Lambda function runs successfully
################################################################################
def send_award_letter_uploaded_notification(
    channel,
    documents,
    graphql_endpoint,
    table_job_ids,
    text_job_ids
):
    try:
        response = client.chat_postMessage(
            channel=channel,
            blocks=[
                {
        			"type": "header",
        			"text": {
        				"type": "plain_text",
        				"text": ":tada: A new award letter was uploaded",
        				"emoji": True
        			}
        		},
        		{
        			"type": "section",
        			"text": {
        				"type": "mrkdwn",
        				"text": f"*Graphql Endpoint*: {graphql_endpoint}\n*Documents:* {documents}\n*Table_job_ids:* {table_job_ids}\n*Text_job_ids:* {text_job_ids}\n",
        			}
        		}
            ]
        )

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

################################################################################
# Sends a notification to Slack when an award letter has been processed
################################################################################
def send_award_letter_reviewed_notification(
    channel,
    college_name,
    college_status_id,
    documents,
    final_check_errors,
    user_email
):

    # divider section
    divider_section = {
	   "type": "divider"
    }

    # create the message
    # main information
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":tada: A new award letter was reviewed",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*User*: {user_email}\n*College:* {college_name}\n*College Status ID:* {college_status_id}\n",
            }
        },
    ]

    # document information
    for document in documents:
        blocks.append(divider_section)

        document_details = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Document Name:* {document['document_name']}\n*Sent to Textract:* {document['sent']}\n*Table Succeeded:* {document['table_succeeded']}\n*Text Succeeded:* {document['text_succeeded']}\n*Automated Review Succeeded:* {document['automated_review_succeeded']}\n",
            }
        }
        blocks.append(document_details)

        if document['errors'] is not None:
            for error in document['errors']:
                print(error['message'])
                error_section = {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Error Type:* {error['type']}\n*Error Message:* {error['message']}\n",
                    }
                }
                blocks.append(error_section)

        if document['aid_data'] is not None:
            for data in document['aid_data']:
                aid_data_section = {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Aid Category:* {data['aid_category']}\n*Name:* {data['name']}\n*Amount:* {data['amount']}\n*Row Text:* {data['row_text']}\n",
                    }
                }
                blocks.append(aid_data_section)

    blocks.append(divider_section)

    if final_check_errors is not None:
        for error in final_check_errors:
            error_section = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Final Check Error Type:* {error['type']}\n*Final Check Error Message:* {error['message']}\n",
                }
            }
            blocks.append(error_section)

    # send the message
    try:
        response = client.chat_postMessage(channel=channel, blocks=blocks)

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

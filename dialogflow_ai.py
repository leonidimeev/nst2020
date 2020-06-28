"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
"""
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/leonidimeev/Desktop/nefu/kursovaya3kurs/nst2020/nst2020-khqpqh-4091dfcabd3f.json'

DIALOGFLOW_PROJECT_ID = 'nst2020-khqpqh'
DIALOGFLOW_LANGUAGE_CODE = 'ru-RU'
SESSION_ID = 'TEST'

def send_to_dialogflow(text_to_be_analyzed):

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return(response.query_result.query_text, response.query_result.intent.display_name, response.query_result.intent_detection_confidence, response.query_result.fulfillment_text)    # Original :
    # print("Query text:", response.query_result.query_text)
    # print("Detected intent:", response.query_result.intent.display_name)
    # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    # print("Fulfillment text:", response.query_result.fulfillment_text)
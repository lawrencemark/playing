import pytest
import os,sys
import requests
import json
sys.path.append('/srv/www/todo_app')
from app import app as flask_app

token = os.getenv('token')
key = os.getenv('key')
slackurlpram = os.getenv('slackuripram')

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


######################PYTEST SESSION FINISH SCRIPTS######################

"""Exit code 0
All tests were collected and passed successfully

Exit code 1
Tests were collected and run but some of the tests failed

Exit code 2
Test execution was interrupted by the user

Exit code 3
Internal error happened while executing tests

Exit code 4
pytest command line usage error

Exit code 5
No tests were collected"""


webhook_url = f'https://hooks.slack.com/services/{slackurlpram}'

def sendRequestToSlack(slack_data):
      
    response = requests.post(
    webhook_url, data = json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    else: 
        print(f'payload: {slack_data} status_code: {response.status_code}')

def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        message = "All tests were collected and passed successfully"
    elif exitstatus == 1:
        message = "Tests were collected and run but some of the tests failed"
    elif exitstatus > 1:
        message = "An unexpected pytest operation was encountered during execution"
           
    slack_data = {'text': message}
    
    sendRequestToSlack(slack_data)


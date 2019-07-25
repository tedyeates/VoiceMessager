import json


def save_session(client):
    """Open session file and write session dict to it"""
    with open('../resources/session.json', "w") as s:
        json.dump(client.getSession(), s)


def get_session():
    """Get session dict"""
    with open('../resources/session.json') as s:
        try:
            return json.load(s)
        except ValueError:
            return None

from time import time
from fbchat.models import *
import re


def send_message(client, message, thread_id, thread_type):
    """Send a message from users facebook account to a thread with id thread_id and type USER/GROUP"""
    client.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)

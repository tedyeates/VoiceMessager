from fbchat import log, Client
from fbchat.models import *
import MessageHandler
from FileHandler import save_session, get_session
from MessageSpeechConverter import message_to_speech
from easygui import passwordbox


class RecieveMessage(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        """Called when message received"""
        self.markAsDelivered(thread_id, message_object.uid)

        message = message_object.text
        author_name = self.fetchUserInfo(author_id)[author_id].name
        message_media = message_object.attachments

        # If not the author of message
        if author_id != self.uid and message is not None:
            say_this_string = author_name + " said " + message
            message_to_speech(say_this_string)

        # If user has sent a message containing media other than text
        if message_media:
            say_this_string = author_name + " posted an attachment"
            message_to_speech(say_this_string)

    def onLoggedIn(self, email=None):
        """Called on successful log in, store session for easy login"""
        save_session(self)


def start_client():
    """Try to login with same session, if session is expired ask for credentials then start listening for messages"""
    try:
        client = RecieveMessage("", "", session_cookies=get_session())
    except FBchatUserError:
        username = input("Enter Your Username:")
        password = passwordbox('Enter Your Password: ')
        client = RecieveMessage(username, password)

    return client


def start_auto_reader():
    """Listen for messages"""
    client = start_client()

    client.listen()


if __name__ == "__main__":
    start_auto_reader()

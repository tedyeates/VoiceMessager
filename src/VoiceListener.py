import speech_recognition as sr
import re
from MessageHandler import send_message
from MessageSpeechConverter import speech_to_message, message_to_speech, message_emojifier
from FacebookMessageListener import start_client
from fbchat import log, Client
from fbchat.models import *
import sys


def select_device():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found, device_id={0}".format(index, name))

    return int(input("Please enter the device_id of the microphone you would like to use"))


def command_match(command, client, microphone, recognizer):
    """Regex matching of text to find and execute users commands"""
    
    # Check if user wants to send a message
    message_pattern = \
        re.search(r'send (?P<type>\w*) message to (?P<name>(\w+\s?)+) saying (?P<message>(.+\s?)+$)', command)
    if message_pattern:
        # Split up message and into components and send
        process_message(message_pattern, client, microphone, recognizer)
    elif command == "exit":
        sys.exit(0)
    elif command == "help":
        help_message()


def help_message():
    help_text = "PROGRAM COMMANDS\n"\
                "     exit        Closes the program\n"\
                "     help        Show all available voice commands\n"\
                "\nFACEBOOK MESSENGER COMMANDS\n"\
                "     send <type> message to <name> saying <message>      send a message <message> of <type> "\
                "('user'/'group') to user with a name closest to the <name> specified\n\n"

    print(help_text)
    message_to_speech(help_text)


def process_message(message_pattern, client, microphone, recognizer):
    name = message_pattern.group("name")
    message = message_pattern.group("message").lower()

    # Try to find target user and set message type to group or user
    try:
        if message_pattern.group("type") == "group":
            target_user = client.searchForGroups(name)[0]
            message_type = ThreadType.GROUP
        else:
            target_user = client.searchForUsers(name)[0]
            message_type = ThreadType.USER
    except (FBchatException, IndexError):
        print("User not found")
        return

    message = message_emojifier(message)
    print("Do you want to send message '" + message + "' to '" + target_user.name + "'")

    # Check if user wants to send message displayed above to target_user
    while True:
        response = speech_to_message(microphone, recognizer)
        if response == "yes":
            print("Sending message")
            send_message(client, message, target_user.uid, message_type)
            break
        elif response == "no":
            print("Canceling command")
            break
        else:
            print("I'm sorry I don't understand, please answer 'Yes' or 'No")


def listen_for_command(device_id):
    """Keep listening for new commands, set up voice recognition"""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=device_id)
    client = start_client()

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    while True:
        print("How can I help?")
        response = speech_to_message(microphone, recognizer)
        print(response + "\n")
        command_match(response, client, microphone, recognizer)


if __name__ == "__main__":
    mic_device = select_device()
    listen_for_command(mic_device)

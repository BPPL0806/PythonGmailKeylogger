# Python 3.11 Gmail keylogger
<img align="right" src="imgs/klggr.png">

### Keylogger written in Python 3.11 that sends logs to gmail account via smtplib.
By default keylogger sends all logs every 5 minutes. If nothing is captured after the last email, nothing will be sent as long as the program will detect another key being pressed.

#### pip requirements: 
- pynput
- email.mime.text
- socket
- platform
- requests
- time
- smtplib
- pyinstaller (building executables)

# Instructions <img align="right" src="imgs/manual.png">

### 1. Using gmail address and app password in keylogger.
You need generated gmail app password, just put it inside code of ```main.pyw``` with email address and app password (at lines 72-74).

![Image of function](imgs/func.png)

### 2. Building windows executable.

I've put ready batch script into this repository that creates executable of ```main.pyw``` using ```pyinstaller```.
If you want to change name of python script to something else you have to change name of file from "main.pyw" to your own inside ```buildExe.bat```.

![Image of code](imgs/build.png)

After script is done, it will copy ready .exe file into the same location as ```buildExe.bat``` and delete unneeded files created by ```pyinstaller```.

#### Program doesn't hide itself so it will run from where it's currently located.

# Example message sent by program.
![screenshot](imgs/klggr_example.png)

# VirusTotal analysis
![VT scan](imgs/vt.png)

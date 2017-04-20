# Twilio SMS Chat GUI

Debugging Twilio SMS chats can be a bit of pain. This tiny python app, will display your Twilio SMS logs to look like a chat.

![Alt](/demo.png "Preview of GUI")

#### Quick Start
1. Clone this repo
```
    > git clone git@github.com:TheSimplePostcard/twilio_chat_history.git
```
    
2. Create the virtualenv, and install the requirements
```
    > cd twilio_chat_history
    > virtualenv env
    > source env/bin/activate
    > pip install -r requirements.txt
```

3. Put your Twilio SID and auth token on lines 4, 5 of main.py
4.  Run the server
```
    > python main.py
```
    
5. Open your browser to http://127.0.0.1:8000



Made by [The Simple Postcard](https://www.TheSimplePostcard.com) - Text a photo to send it as a postcard

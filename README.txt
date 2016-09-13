A simple tool to view a Twilio SMS conversation with a specific number.

This is a small Flask/python app to look at Twilio logs as a chat. This
is not intended for production use!


To get set up:

  1. Clone this repo:
    > git clone git@github.com:TheSimplePostcard/twilio_chat_history.git

  2. Set up the virtual environment and requirements
    > cd twilio_chat_history
    > virtualenv env
    > source env/bin/activate
    > pip install -r requirements.txt

  3. Put your Twilio SID and auth token on lines 4, 5 of main.py

  4. Run the server
    > python main.py

  5. Open your browser to http://127.0.0.1:8000


Todo:

 - Show images and other media from Twilio


Send a postcard from your phone
Text a photo to (251)265-2848
https://TheSimplePostcard.com

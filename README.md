# update-ticket-priority

Steps to build <br>
1 - Run `python3 -m venv flask_env`;<br>
2 - Run `source flask_env/bin/activate`;<br>
3 - Run `pip install -r requirements.txt`;<br>
4 - set a `.env` file on the root folder with this data:<br>
    

    DEBUG=True
    FLASK_ENV=development
    FLASK_APP=app.py
    APP_SETTINGS=configuration.config.DevelopmentConfig
    ZD_AUTH_USER=your_zd_user
    ZD_AUTH_PASSWORD=your_zd_password
    
5 - Run `python3 app.py`;<br>
<hr>
Make a post call to localhost:6000/tickets/update-ticket-priority with the following payload:

{
    "ticket_id": your_ticket_id
}

# update-ticket-priority

Steps to build
1 - python3 -m venv flask_env;
2 - source flask_env/bin/activate;
3 - pip install -r requirements.txt;
4 - python3 app.py;

Make a post call to localhost:6000/tickets/update-ticket-priority with the following payload:

{
    "ticket_id": your_ticket_id
}

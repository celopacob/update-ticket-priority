# update-ticket-priority

Steps to build <br>
1 - python3 -m venv flask_env;<br>
2 - source flask_env/bin/activate;<br>
3 - pip install -r requirements.txt;<br>
4 - python3 app.py;<br>
<hr>
Make a post call to localhost:6000/tickets/update-ticket-priority with the following payload:

{
    "ticket_id": your_ticket_id
}

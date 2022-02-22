from flask import Flask, request, jsonify, abort
import json
from json import JSONDecodeError
import zendesk as zendesk_client


app = Flask(__name__)

@app.route('/tickets/update-ticket-priority/', methods=['POST'])
def update_ticket():
    try:
        data = json.loads(request.data)
        ticket_id = data['ticket_id']
        res = zendesk_client.update_ticket_priority(ticket_id)
        return jsonify({"data": res})

    except(JSONDecodeError):
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

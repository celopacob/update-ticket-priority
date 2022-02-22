import request_client as client


ZD_URL='https://conleafworks1635144020.zendesk.com/api'
ZD_TICKETS_URL = ZD_URL + '/v2/tickets'
ZD_SEARCH_TICKET_URL = ZD_URL + '/v2/tickets/{ticket_id}'
ZD_ORDERS_URL = ZD_URL + '/sunshine/objects/records?type=orders'
ZD_ORDER_SEARCH_URL = ZD_URL + '/sunshine/objects/query'
ZD_ORDER_CUSTOM_FIELD_ID = 4444667061138

def get_ticket_by_id(ticket_id):
    return client.get_call(ZD_SEARCH_TICKET_URL.format(ticket_id=ticket_id))

def get_order_id_by_ticket(ticket_id):
    ticket_data = get_ticket_by_id(ticket_id)
    custom_fields = ticket_data['ticket']['custom_fields']
    ticket_order_list = list(filter(lambda x:x["id"]==ZD_ORDER_CUSTOM_FIELD_ID, custom_fields))
    return ticket_order_list[0]['value']

def get_order_by_id(order_id):
    order_search_data = {
        "query": {
            "order_no": {"$eq": order_id}
        }
    }
    res = client.post_call(ZD_ORDER_SEARCH_URL, order_search_data)
    return res['data'][0]

def get_order_value(order_id):
    order_data = get_order_by_id(order_id)
    return order_data['attributes']['order_value']

def get_ticket_priority_by_order_value(order_value):
    if order_value > 2000:
        return "urgent"
    elif order_value > 1000:
        return "high"
    elif order_value > 300:
        return "normal"
    else:
        return "low"

def update_ticket_priority(ticket_id):
    order_id = get_order_id_by_ticket(ticket_id)
    order_value = get_order_value(order_id)
    ticket_priority = get_ticket_priority_by_order_value(order_value)
    ticket_update_data = {
        "ticket": {
            "priority": ticket_priority
        }
    }

    return client.put_call(
        ZD_SEARCH_TICKET_URL.format(ticket_id=ticket_id),
        ticket_update_data
    )

from flask import request
import requests
import json
from util.common import zoom_endpoint, zoom_token

def PostAlertZoom(data):
    alert_message = data["message"]
    alert_title = data["title"]
    alert_color = dict(alerting = "#e49137", nodata = "#3c78d8", error = "#cc0001", ok = "#69a84f")
    if data["state"] in alert_color:
        sidebar_color = alert_color[data["state"]]
    else: 
        sidebar_color = "#3c78d8"
        print(data["state"])
    
    zoom_message_headers = {'Authorization' : 'Bearer {}'.format(zoom_token)}
    zoom_send_msg_payload = {
    "head": {
        "text": "{}".format(alert_title),
        "is_markdown_support": "true"
    },
    "body": [
        {
        "type": "section",
        "sidebar_color": "{}".format(sidebar_color),
        "sections": [
            {
            "type": "message",
            "text": "{}".format(alert_message),
            "is_markdown_support": "true"
            }
        ]
        }
    ]
    }
    print(zoom_send_msg_payload)
    zoom_response = requests.post('{}?format=full'.format(zoom_endpoint), headers=zoom_message_headers, json=zoom_send_msg_payload, verify=False)

    if (zoom_response.status_code != 200):
        print(zoom_response)
        print(zoom_response.content)
        return "Error"
    else:
        return "Ok"

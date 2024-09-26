import requests
import json

# Zendesk credentials
subdomain = 'your_zendesk_subdomain'
email = 'your_email@example.com'
api_token = 'your_api_token'
url = f"https://{subdomain}.zendesk.com/api/v2/tickets/update_many.json"

# Authentication
auth = (f"{email}/token", api_token)

# List of ticket IDs to update
ticket_ids = [123, 456, 789]  # Add your ticket IDs here

# Public reply and pending status payload
data = {
    "tickets": [
        {
            "id": ticket_id,
            "status": "pending",
            "comment": {
                "body": "This is a public reply.",
                "public": True
            }
        } for ticket_id in ticket_ids
    ]
}

# Sending the request
response = requests.put(url, auth=auth, json=data)

# Check the response status
if response.status_code == 200:
    print(f"Successfully updated tickets: {ticket_ids}")
else:
    print(f"Failed to update tickets. Status Code: {response.status_code}")
    print(response.text)

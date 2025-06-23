import requests

# URL of the node's API endpoint
API_URL = "http://127.0.0.1:5000/nodes/register"

# List of nodes to register
nodes_to_register = ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]

# Create the data to send in the POST request
data = {
    "nodes": nodes_to_register
}

# Send the POST request to register the nodes
try:
    response = requests.post(API_URL, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        print("Nodes successfully registered!")
        print("Registered nodes:", response.json()['nodes'])
    else:
        print(f"Failed to register nodes: {response.status_code}")
        print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error while registering nodes: {e}")
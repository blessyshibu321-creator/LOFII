import json
from datetime import datetime

LOG_FILE = "incident_history.json"

def log_incident(data):

    data["logged_time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    try:
        with open(LOG_FILE, "r") as file:
            incidents = json.load(file)

    except:
        incidents = []

    incidents.append(data)

    with open(LOG_FILE, "w") as file:
        json.dump(incidents, file, indent=4)

    print("Incident Logged!")

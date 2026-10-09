import json

from isolation_simulator import get_blocked_sources
from monitoring import get_monitored_sources

def show_dashboard():

    print("\n===== DASHBOARD =====")

    print("\nBlocked Sources:")
    print(get_blocked_sources())

    print("\nMonitored Sources:")
    print(get_monitored_sources())

    try:

        with open("incident_history.json", "r") as file:
            history = json.load(file)

        print("\nRecent Incidents:")

        for incident in history:
            print(incident)

    except:
        print("No incident history found.")
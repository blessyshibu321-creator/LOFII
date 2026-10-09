from isolation_simulator import isolate_source
from monitoring import monitor_source

def process_risk(data):

    risk = data["risk_level"]

    if risk == "High":
        return isolate_source(data)

    elif risk == "Medium":
        return monitor_source(data)

    elif risk == "Low":

        return {
            "incident_id": data["incident_id"],
            "source_ip": data["source_ip"],
            "risk_level": risk,
            "action": "No Action",
            "status": "Completed"
        }

    else:

        return {
            "incident_id": data["incident_id"],
            "source_ip": data["source_ip"],
            "risk_level": risk,
            "action": "Unknown Risk",
            "status": "Failed"
        }
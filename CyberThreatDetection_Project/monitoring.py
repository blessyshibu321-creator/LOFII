monitoring_list = {}

def monitor_source(data):

    ip = data["source_ip"]

    if ip not in monitoring_list:
        monitoring_list[ip] = "Monitoring"

    return {
        "incident_id": data["incident_id"],
        "source_ip": ip,
        "risk_level": data["risk_level"],
        "action": "Monitoring Enabled",
        "status": "Completed"
    }

def get_monitored_sources():
    return monitoring_list
blocked_sources = {}

def isolate_source(data):

    ip = data["source_ip"]

    if ip not in blocked_sources:
        blocked_sources[ip] = "Blocked"
        action = "Source Isolated"
    else:
        action = "Already Blocked"

    return {
        "incident_id": data["incident_id"],
        "source_ip": ip,
        "risk_level": data["risk_level"],
        "action": action,
        "status": "Completed"
    }

def get_blocked_sources():
    return blocked_sources
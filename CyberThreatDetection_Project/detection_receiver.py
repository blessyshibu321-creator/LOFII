import ipaddress

def receive_detection_output(data):

    required_fields = [
        "incident_id",
        "source_ip",
        "risk_level",
        "timestamp"
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    # Validate IP address
    ipaddress.ip_address(data["source_ip"])

    return data
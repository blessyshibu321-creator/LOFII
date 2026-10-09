from response_controller import automated_response
from dashboard_view import show_dashboard

sample_data = [

    {
        "incident_id": "INC001",
        "source_ip": "192.168.1.10",
        "risk_level": "High",
        "timestamp": "2026-10-09"
    },

    {
        "incident_id": "INC002",
        "source_ip": "192.168.1.20",
        "risk_level": "Medium",
        "timestamp": "2026-10-09"
    },

    {
        "incident_id": "INC003",
        "source_ip": "192.168.1.30",
        "risk_level": "Low",
        "timestamp": "2026-10-09"
    }

]

for item in sample_data:

    result = automated_response(item)

    print(result)

show_dashboard()
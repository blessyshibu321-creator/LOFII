from detection_receiver import receive_detection_output
from decision_engine import process_risk
from incident_logger import log_incident

def automated_response(data):

    validated_data = receive_detection_output(data)

    result = process_risk(validated_data)

    log_incident(result)

    return result
# Cyber Threat Detection System

## Part 2: Automated Response Module

This module receives threat detection results from the AI Detection Module and automatically performs actions based on risk levels.

## Features

- High Risk → Source Isolation
- Medium Risk → Monitoring
- Low Risk → No Action
- Incident Logging
- Dashboard View
- Timestamp Recording

## Technologies Used

- Python
- JSON
- VS Code

## Project Structure

```text
detection_receiver.py
decision_engine.py
isolation_simulator.py
monitoring.py
incident_logger.py
dashboard_view.py
response_controller.py
test_part2.py
incident_history.json
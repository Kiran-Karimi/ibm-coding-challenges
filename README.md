# IBM Coding Challenge Solutions (Python)

This repository contains my Python solutions to IBM-style coding problems, similar to those found in HackerRank and online coding assessments.

Each problem tests algorithmic thinking, efficiency, and clean Python coding skills.

# Problem 1 — Call Volume Alerts

File:`call_volume_alerts.py`(./call_volume_alerts.py)

# Description
Implements a compliance system that monitors incoming and outgoing call volumes and sends an alert whenever the *average* number of calls over a trailing number of minutes exceeds a given threshold.

Example:
numCalls = [2, 2, 2, 2, 5, 5, 5, 8]
precedingMinutes = 3
alertThreshold = 4
→ Alerts sent = 2


# Problem 2 — Service Timeout Monitor

File: `service_timeout_monitor.py`(./service_timeout_monitor.py)

# Description
Analyzes heartbeat logs from multiple services to detect any that timed out.  
A timeout occurs when the gap between two consecutive heartbeats exceeds a given threshold.

Example:
timestamps = [10, 20, 80, 10, 65]
serviceIds = ["svc1", "svc1", "svc1", "svc2", "svc2"]
threshold = 30
→ Timed out services = ["svc1", "svc2"]

#How to Run
Run the programs locally using Python 3:
```bash
python3 call_volume_alerts.py
python3 service_timeout_monitor.py

#Notes

* Written in Python 3
* Designed for HackerRank-style input/output
* Each solution passes both visible and hidden test cases
* Clean, readable code with O(n) or O(n log n) efficiency

# Author
Kiran Reddy Karimireddy
Aspiring AI Engineer | Python & Java Developer
GitHub:https://github.com/Kiran-Karimi

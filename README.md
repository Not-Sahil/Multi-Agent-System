#Multi-Agent AI Document Processor

This project is a modular **Multi-Agent AI System** that accepts input in **PDF**, **JSON**, or **Email** format, automatically detects the format and intent, and routes the data to the appropriate agent for further processing.

#Features

- Accepts PDF, JSON, or plain text (Email) as input
- Classifies:
  - Format : PDF / JSON / Email
  - Intent : Invoice, RFQ, Complaint, Regulation, etc.
- Routes input to the correct agent:
  - Email Agent – Extracts sender, intent, urgency
  - JSON Agent – Parses structured payloads, flags anomalies
- Uses **SQLite-based shared memory** to store:
  - Source info, type, intent, extracted fields, timestamp
- Log viewer to inspect all saved entries

#Project Structure

multi_agent_system/
│
├── agents/
│ ├── classifier_agent.py # Classifies format + intent and routes
│ ├── email_agent.py # Processes email content
│ └── json_agent.py # Processes JSON input
│
├── memory/
│ └── memory_store.py # Shared context (SQLite)
│
├── utils/
│ └── intent_detector.py # Intent detection logic
│
├── main.py # Entry point
└── view_logs.py # View stored logs

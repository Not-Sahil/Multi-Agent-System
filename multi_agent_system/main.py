from agents.classifier_agent import ClassifierAgent
from memory.memory_store import MemoryStore

memory = MemoryStore()
classifier = ClassifierAgent(memory)

json_input = {
    "company" : "XYZ ltd",
    "request_type" : "Invoice",
    "details" : {
        "items" : 3,
        "amount" : 250
    }
}

email_text = """
Subject: Request for Quotation

Dear team,
We need pricing details for 5 units of product A.
Please respond urgently.

Regards,
ABC ltd
"""

classifier.classify_and_route(json_input, source = "XYZ ltd")
classifier.classify_and_route(email_text, source = "ABC ltd")
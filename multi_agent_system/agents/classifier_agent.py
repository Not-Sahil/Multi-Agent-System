from agents.json_agent import process_json
from agents.email_agent import process_email
from utils.intent_detector import detect_intent
from datetime import datetime

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
    
    def classify_and_route(self, input_data, source = "unknown", thread_id = None):
        if isinstance(input_data,dict):
            data_format = "JSON"
        elif isinstance(input_data, str):
            if "Subject:" in input_data or "Dear" in input_data or "Regards" in input_data:
                data_format = "Email"
            else:
                data_format = "Text"
        else:
            data_format = "Unknown"

        intent = detect_intent(input_data if isinstance(input_data, str) else str(input_data))

        print(f"Classifier Agent: Detected formar = {data_format}, intent = {intent}")

        if data_format == "Email":
            print("Routed to Email Agent...")
            process_email(input_data, self.memory, source = source, thread_id = thread_id)
        elif data_format == "JSON":
            print("Routed to JSON Agent...")
            process_json(input_data, self.memory, source = source, thread_id = thread_id)
        else:
            print("Unknown format... Cannot route...")
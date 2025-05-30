from utils.intent_detector import detect_intent

def process_email(email_text, memory, source = "unknown", thread_id = None):
    lines = email_text.split('\n')
    sender = source
    urgency = "High" if "urgent" in email_text.lower() else "Normal"
    intent = detect_intent(email_text)

    extracted = {
        "sender" : sender,
        "urgency" : urgency,
        "summary" : lines[:2]
    }

    memory.save({
        'source' : source,
        'type' : 'Email',
        'intent' : intent,
        'extracted_fields' : extracted,
        'thread_id' : thread_id,
        'timestamp' : None
    })

    print("Email Agent processed input.....")
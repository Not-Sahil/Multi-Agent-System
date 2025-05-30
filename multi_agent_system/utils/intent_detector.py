def detect_intent(text):
    text = text.lower()
    if "invoice" in text:
        return "Invoice"
    elif "quote" in text or "rfq" in text:
        return "RFQ"
    elif "complaint" in text:
        return "Complaint"
    elif "regulation" in text:
        return "Regulation"
    else:
        return "General"
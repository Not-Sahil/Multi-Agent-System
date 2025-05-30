def process_json(json_data, memory, source = "unknown", thread_id = None):
    required_fields = ["id", "date", "amount"]
    missing = [f for f in required_fields if f not in json_data]
    anomalies = [k for k, v in json_data.items() if v in [None, ""]]

    extracted = {
        "valid" : len(missing) == 0,
        "missing_fields" : missing,
        "anomalies" : anomalies,
        "normalized" : json_data
    }

    memory.save({
        'source' : source,
        'type' : 'JSON',
        'intent' : "Processed JSON",
        'extracted_fields' : extracted,
        'thread_id' : thread_id,
        'timestamp' : None
    })

    print("JSON Agent processed input.....")
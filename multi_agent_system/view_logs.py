from memory.memory_store import MemoryStore
import json
memory = MemoryStore()
logs = memory.load_all()

for log in logs:
    print(json.dumps(log, indent = 2))
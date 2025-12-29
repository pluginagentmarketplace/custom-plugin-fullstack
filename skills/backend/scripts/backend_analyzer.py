#!/usr/bin/env python3
import json
def analyze(): return {"languages": ["node", "python", "go"], "databases": ["postgres", "mongo", "redis"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))

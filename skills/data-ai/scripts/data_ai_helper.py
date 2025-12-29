#!/usr/bin/env python3
import json
def helper(): return {"data": ["etl", "analytics"], "ai": ["ml", "llm", "embeddings"]}
if __name__ == "__main__": print(json.dumps(helper(), indent=2))

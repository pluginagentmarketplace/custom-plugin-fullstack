#!/usr/bin/env python3
import json
def track(): return {"areas": ["docs", "community", "dx"], "metrics": ["adoption", "engagement"]}
if __name__ == "__main__": print(json.dumps(track(), indent=2))

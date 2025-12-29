#!/usr/bin/env python3
import json
def check(): return {"containers": ["docker", "k8s"], "cloud": ["aws", "gcp", "azure"]}
if __name__ == "__main__": print(json.dumps(check(), indent=2))

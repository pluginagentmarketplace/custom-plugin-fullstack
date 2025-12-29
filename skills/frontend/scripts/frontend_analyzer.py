#!/usr/bin/env python3
import json
def analyze(): return {"frameworks": ["react", "vue", "angular"], "bundlers": ["vite", "webpack"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))

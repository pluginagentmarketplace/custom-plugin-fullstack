#!/usr/bin/env python3
import json
def manage(): return {"processes": ["agile", "scrum"], "tools": ["jira", "linear", "notion"]}
if __name__ == "__main__": print(json.dumps(manage(), indent=2))

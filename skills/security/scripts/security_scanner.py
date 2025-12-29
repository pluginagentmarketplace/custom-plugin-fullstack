#!/usr/bin/env python3
import json
def scan(): return {"auth": ["jwt", "oauth2"], "vulnerabilities": ["injection", "xss", "csrf"]}
if __name__ == "__main__": print(json.dumps(scan(), indent=2))

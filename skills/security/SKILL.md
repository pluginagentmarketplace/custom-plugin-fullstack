---
name: security-systems
description: Master cybersecurity, system design, software architecture, and design patterns. Use when designing secure systems, architecting applications, or implementing security best practices.
sasmp_version: "1.3.0"
bonded_agent: 01-frontend-mobile
bond_type: PRIMARY_BOND
---

# Security & Systems Design

## Quick Start

Security and Systems Design involves protecting systems from attacks and designing scalable architectures. The roadmap covers:

### Core Competencies
- **Security**: OWASP, cryptography, authentication, authorization
- **System Design**: Scalability, databases, caching, load balancing
- **Architecture**: Design patterns, microservices, serverless
- **Networking**: TCP/IP, DNS, HTTP/HTTPS, SSL/TLS
- **Tools**: OWASP, Burp Suite, Metasploit, nmap
- **Databases**: PostgreSQL, MongoDB, Redis, Elasticsearch
- **Cloud**: AWS, Azure, GCP

### Security Fundamentals

**OWASP Top 10 Vulnerabilities**:
1. Broken Access Control
2. Cryptographic Failures
3. Injection (SQL, Command)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Software Supply Chain
9. Logging & Monitoring Failures
10. SSRF (Server-Side Request Forgery)

**Secure Password Hashing**:
```python
import bcrypt

# Hash password
password = b"user_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Verify password
is_correct = bcrypt.checkpw(password, hashed)
```

**System Design Example - User Service**:
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼──────────┐
│  Load Balancer  │
└──────┬──────────┘
       │
┌──────▼──────────────────────┐
│  API Servers (multiple)     │
└──────┬──────────────────────┘
       │
   ┌───┴───┬─────────┐
   │       │         │
   ▼       ▼         ▼
 Cache  Database   Search
(Redis) (PgSQL)   (Elastic)
```

## Study Path

1. **Networking Basics** (1-2 weeks): TCP/IP, DNS, HTTP/HTTPS
2. **Security Fundamentals** (2-3 weeks): Crypto, OWASP, threats
3. **System Design** (3-4 weeks): Scalability, databases, caching
4. **Architecture Patterns** (2-3 weeks): Microservices, design patterns
5. **Advanced Topics** (ongoing): Threat modeling, compliance

## Key Topics

- OWASP Top 10 vulnerabilities and prevention
- Encryption and cryptography
- Authentication and authorization mechanisms
- System scalability and performance
- Database design and optimization
- Caching strategies
- Load balancing
- Microservices architecture
- Design patterns (creational, structural, behavioral)
- API design and security

## Resources
- Developer Roadmap: https://roadmap.sh/system-design
- OWASP: https://owasp.org
- Security Testing: https://owasp.org/www-project-web-security-testing-guide

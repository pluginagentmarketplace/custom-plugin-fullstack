---
name: backend-development
description: Master backend technologies including Node.js, Python, Java, API design, databases, and server architecture. Use when building server applications, designing APIs, or managing databases.
sasmp_version: "1.3.0"
bonded_agent: 01-frontend-mobile
bond_type: PRIMARY_BOND
---

# Backend Development

## Quick Start

Backend development focuses on server-side applications, APIs, and database management. The roadmap covers:

### Core Competencies
- **Languages**: Node.js, Python, Java, Go
- **Web Frameworks**: Express, Django, FastAPI, Spring Boot, NestJS
- **Databases**: PostgreSQL, MongoDB, MySQL, Redis
- **APIs**: REST, GraphQL, gRPC, SOAP
- **Authentication**: OAuth, JWT, SAML, Session-based
- **Testing**: Jest, Pytest, JUnit, Postman, REST Assured
- **Caching**: Redis, Memcached, HTTP caching

### Language Selection

**Node.js**: JavaScript for backend, event-driven, great for APIs
```javascript
const express = require('express');
const app = express();

app.get('/api/users', async (req, res) => {
  const users = await User.find();
  res.json(users);
});

app.listen(3000);
```

**Python**: Versatile, readable, excellent for APIs and data
```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/users")
async def get_users():
    users = await User.find()
    return JSONResponse(users)
```

**Java**: Enterprise-grade, high-performance
```java
@SpringBootApplication
public class Application {
    @GetMapping("/api/users")
    public List<User> getUsers() {
        return userService.findAll();
    }
}
```

## Study Path

1. **Language Fundamentals** (2-3 weeks): Choose primary language
2. **Web Framework** (2-3 weeks): Master chosen framework
3. **Databases** (2-3 weeks): SQL and NoSQL integration
4. **APIs** (2-3 weeks): REST design, GraphQL basics
5. **Advanced** (ongoing): Caching, authentication, testing

## Key Topics

- RESTful API design and best practices
- Database design and normalization
- Authentication and authorization
- Error handling and logging
- Testing strategies
- Performance optimization
- Security best practices
- Microservices basics

## Resources
- Developer Roadmap: https://roadmap.sh/backend
- Node.js: https://nodejs.org
- Python FastAPI: https://fastapi.tiangolo.com
- Spring Boot: https://spring.io/projects/spring-boot

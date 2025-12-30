---
name: backend-development
description: Backend development - APIs, authentication, business logic
sasmp_version: "1.3.0"
bonded_agent: 03-backend-development
bond_type: PRIMARY_BOND

# Skill Configuration
atomic: true
single_responsibility: backend_implementation

# Parameter Schema
parameters:
  type: object
  required: [action]
  properties:
    action:
      type: string
      enum: [create_endpoint, implement_auth, build_service, integrate_external]
      description: The specific backend action to perform
    runtime:
      type: string
      enum: [nodejs, python, go, rust]
      default: nodejs
    framework:
      type: string
      enum: [express, fastify, nestjs, fastapi, django, flask]
    api_style:
      type: string
      enum: [rest, graphql, grpc]
      default: rest

# Return Schema
returns:
  type: object
  properties:
    success: { type: boolean }
    code: { type: string }
    files: { type: array, items: { type: object } }
    api_spec: { type: object }
    security_notes: { type: array, items: { type: string } }

# Retry Configuration
retry:
  max_attempts: 3
  backoff: exponential
  initial_delay_ms: 1000
  jitter: true

# Observability
logging:
  level: INFO
  events: [endpoint_created, auth_configured, service_built]
  metrics: [api_complexity, security_score]
---

# Backend Development Skill

Atomic skill for backend development including API creation, authentication, and service implementation.

## Responsibility

**Single Purpose**: Implement backend services, APIs, and business logic

## Actions

### `create_endpoint`
Create a new API endpoint with validation and error handling.

```typescript
// Input
{
  action: "create_endpoint",
  runtime: "nodejs",
  framework: "express",
  api_style: "rest"
}

// Output
{
  success: true,
  code: "router.post('/users', validate(schema), async (req, res) => {...})",
  files: [
    { path: "routes/users.ts", content: "..." },
    { path: "routes/users.test.ts", content: "..." }
  ],
  api_spec: { openapi: "3.0.0", paths: {...} },
  security_notes: ["Rate limiting recommended", "Input validation applied"]
}
```

### `implement_auth`
Implement authentication and authorization.

### `build_service`
Build a business logic service.

### `integrate_external`
Integrate with external APIs.

## Validation Rules

```typescript
function validateParams(params: SkillParams): ValidationResult {
  if (!params.action) {
    return { valid: false, error: "action is required" };
  }

  if (params.action === 'implement_auth' && !params.runtime) {
    return { valid: false, error: "runtime required for auth implementation" };
  }

  return { valid: true };
}
```

## Error Handling

| Error Code | Description | Recovery |
|------------|-------------|----------|
| INVALID_RUNTIME | Unsupported runtime | Check supported runtimes |
| AUTH_PATTERN_INSECURE | Security vulnerability detected | Apply secure pattern |
| API_DESIGN_VIOLATION | REST/GraphQL best practice violation | Suggest correction |

## Logging Hooks

```json
{
  "on_invoke": "log.info('backend-development invoked', { action, runtime })",
  "on_success": "log.info('Endpoint created', { files, api_spec })",
  "on_error": "log.error('Backend skill failed', { error })"
}
```

## Unit Test Template

```typescript
import { describe, it, expect } from 'vitest';
import { backendDevelopment } from './backend-development';

describe('backend-development skill', () => {
  describe('create_endpoint', () => {
    it('should create REST endpoint with validation', async () => {
      const result = await backendDevelopment({
        action: 'create_endpoint',
        runtime: 'nodejs',
        framework: 'express',
        api_style: 'rest'
      });

      expect(result.success).toBe(true);
      expect(result.code).toContain('validate');
      expect(result.api_spec.openapi).toBe('3.0.0');
    });

    it('should include security middleware', async () => {
      const result = await backendDevelopment({
        action: 'create_endpoint',
        runtime: 'nodejs'
      });

      expect(result.code).toMatch(/authenticate|rateLimiter/);
    });
  });

  describe('implement_auth', () => {
    it('should implement JWT auth with refresh tokens', async () => {
      const result = await backendDevelopment({
        action: 'implement_auth',
        runtime: 'nodejs'
      });

      expect(result.success).toBe(true);
      expect(result.security_notes.length).toBeGreaterThan(0);
    });
  });
});
```

## Integration

- **Bonded Agent**: 03-backend-development
- **Upstream Skills**: fullstack-basics
- **Downstream Skills**: database-integration, fullstack-testing

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-01 | Initial release |
| 2.0.0 | 2025-01 | Production-grade upgrade with security patterns |

---
name: devops-infrastructure
description: Master DevOps, containerization, cloud platforms, and infrastructure automation. Use when deploying applications, managing infrastructure, or setting up CI/CD pipelines.
sasmp_version: "1.3.0"
bonded_agent: 01-frontend-mobile
bond_type: PRIMARY_BOND
---

# DevOps & Infrastructure

## Quick Start

DevOps combines development and operations to automate deployment and infrastructure management. The roadmap covers:

### Core Technologies
- **Containers**: Docker, Docker Compose, Podman
- **Orchestration**: Kubernetes, Docker Swarm, Nomad
- **Cloud Platforms**: AWS, Azure, Google Cloud
- **Infrastructure as Code**: Terraform, CloudFormation, Ansible
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **Monitoring**: Prometheus, Grafana, ELK Stack
- **Scripting**: Bash, Python, Go

### Container Basics

**Docker**: Package applications in containers
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

**Docker Compose**: Define multi-container applications
```yaml
version: '3.9'
services:
  app:
    build: .
    ports:
      - "3000:3000"
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
```

**Kubernetes**: Orchestrate containerized applications
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: app:latest
        ports:
        - containerPort: 3000
```

## Study Path

1. **Linux Fundamentals** (1-2 weeks): Essential OS knowledge
2. **Docker Mastery** (2-3 weeks): Container creation and management
3. **Container Orchestration** (2-3 weeks): Kubernetes basics
4. **Cloud Platforms** (2-3 weeks): AWS, Azure, or GCP
5. **Infrastructure as Code** (2-3 weeks): Terraform, Ansible
6. **CI/CD Pipelines** (1-2 weeks): Automation workflows

## Key Topics

- Container design and optimization
- Kubernetes architecture and management
- Cloud service selection and optimization
- Infrastructure as Code best practices
- Monitoring and observability
- Security in infrastructure
- Auto-scaling and high availability
- Disaster recovery and backup

## Resources
- Developer Roadmap: https://roadmap.sh/devops
- Docker: https://www.docker.com
- Kubernetes: https://kubernetes.io
- Terraform: https://www.terraform.io

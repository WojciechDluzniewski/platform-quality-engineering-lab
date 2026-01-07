# Platform Quality Engineering Lab

## Overview
This project demonstrates a **Quality Engineering approach** to testing a digital platform composed of multiple services.

Instead of focusing primarily on UI-based end-to-end tests, the project emphasizes:
- early risk detection,
- contract validation between services,
- API-level functional and non-functional testing,
- quality gates integrated into CI/CD pipelines.

The goal is to show how quality can be **designed into the system**, not added at the end.

---

## Platform Context
The platform represents a simplified digital foundation used to build end-user products.

It consists of:
- multiple backend services,
- service-to-service communication,
- an API gateway layer,
- downstream consumers (UI, other services).

This structure reflects common real-world digital platforms.

---

## Quality Engineering Goals
The main quality risks addressed in this project are:

- Breaking changes between services
- Undetected integration issues
- Performance degradation under load
- Over-reliance on fragile UI end-to-end tests
- Late detection of critical defects

---

## Testing Strategy

### API Testing (Core Layer)
- Functional and negative testing at API level
- Validation of business behavior, not only status codes
- Fast feedback and high reliability

### Contract Testing
- Consumer-driven contracts between services
- OpenAPI schema validation
- Early detection of breaking changes

### Non-Functional Testing
- Performance smoke tests
- Stability and timeout scenarios
- Quality thresholds used as delivery gates

### UI Testing (Minimal)
- UI tests are limited to critical smoke flows
- UI is treated as a verification layer, not a foundation

---

## CI/CD & Quality Gates
All tests are integrated into the CI pipeline.

Quality gates are applied to:
- contract validation,
- API regression,
- performance thresholds.

A failed quality gate blocks delivery.

---

## AI-Assisted Quality
AI tools are used to:
- generate edge-case scenarios,
- analyze test failures,
- refactor and improve test code,
- reduce flaky tests.

AI is treated as a **quality accelerator**, not a replacement for engineering judgment.

---

## Tech Stack (planned)
- Python / pytest
- FastAPI (services)
- Playwright (UI smoke)
- Pact / OpenAPI
- k6 or Locust (performance)
- Docker & Docker Compose
- GitHub Actions

---

## Project Status
The project is developed incrementally.
Each commit represents a specific quality engineering capability.

See commit history for the evolution of the testing strategy.
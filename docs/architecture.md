# Platform Architecture (High-Level)

The platform is composed of independent services communicating over HTTP APIs.

Client requests are routed through an API gateway to backend services.

The architecture is intentionally simple to focus on quality concerns such as:
- service contracts,
- integration boundaries,
- failure modes,
- performance characteristics.

Testing strategy aligns with the architecture by shifting validation as close as possible to service boundaries.
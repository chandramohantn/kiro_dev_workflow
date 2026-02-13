# Security Guidelines

## Purpose
These rules define how we protect:
- Data
- Credentials
- Systems
- Users

They apply to **all** code: APIs, pipelines, ML jobs, scripts, and infra tooling.

---

## 1. Core Principles

- Assume all inputs are untrusted
- Minimize blast radius of failures
- Follow least-privilege access
- Prefer defense-in-depth over single controls

---

## 2. Secrets & Credentials

- NEVER:
  - Commit secrets to git
  - Log secrets
  - Hardcode secrets
- Always:
  - Use environment variables, vaults, or secret managers
  - Pass secrets via secure config mechanisms
- Rotate secrets if:
  - They are exposed
  - You suspect compromise

---

## 3. Input Validation

- All external input must be validated:
  - API inputs
  - File inputs
  - Message queue inputs
  - Config inputs
- Use:
  - Pydantic or schema validation
  - Explicit checks for ranges, formats, sizes
- Reject invalid input early and clearly

---

## 4. Authentication & Authorization

- Do not assume:
  - “Internal” means “trusted”
- Enforce:
  - AuthN at boundaries
  - AuthZ at resource or action level
- Never rely on:
  - Client-side checks alone
- Log:
  - Auth failures
  - Permission denials (without leaking sensitive info)

---

## 5. Data Access & Storage

- Apply least privilege:
  - DB users should only have required permissions
- Avoid:
  - Overly broad queries
  - Exposing internal IDs or sensitive fields
- Be careful with:
  - PII
  - Credentials
  - Tokens
  - Logs and traces

---

## 6. Injection & Unsafe Execution

- Never:
  - Build SQL with string concatenation
  - Execute shell commands with untrusted input
- Always:
  - Use parameterized queries
  - Use safe APIs for subprocess execution
- Treat:
  - SQL injection
  - Command injection
  - Template injection
  as critical vulnerabilities

---

## 7. Serialization & Deserialization

- Be cautious when:
  - Loading pickle
  - Parsing YAML
  - Deserializing arbitrary JSON into objects
- Prefer:
  - Safe loaders
  - Explicit schemas
- Never deserialize untrusted data into executable objects

---

## 8. Logging & Observability

- Do NOT log:
  - Passwords
  - Tokens
  - Secrets
  - Full sensitive payloads
- Mask or redact sensitive fields
- Logs should help:
  - Investigate incidents
  - Not create new ones

---

## 9. Dependencies & Supply Chain

- Keep dependencies:
  - Up to date
  - From trusted sources
- Avoid:
  - Unmaintained libraries
  - Copy-pasting code from unknown sources
- If a vulnerability is found:
  - Patch or mitigate quickly
  - Document in notes or ADR if impact is large

---

## 10. Security Review Checklist

Before shipping:

- [ ] No secrets in code or logs
- [ ] All inputs validated
- [ ] AuthN/AuthZ enforced where needed
- [ ] DB and service permissions are minimal
- [ ] No obvious injection vectors
- [ ] Sensitive data is handled carefully

---

## 11. When to Make Exceptions

- Only with:
  - Explicit justification
  - Documented risk
  - Preferably an ADR
- Temporary exceptions must have:
  - A follow-up task
  - A removal plan

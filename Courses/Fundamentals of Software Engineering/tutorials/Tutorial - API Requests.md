---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - http
  - api
  - rest
  - tutorial
type: tutorial
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# Tutorial — API Requests

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week1-apirequests>
> Postman walkthrough (Spring 2026): <https://neu-se.github.io/CS4530-Spring-2026/tutorials/week1-apirequests-postman>

**Assigned in**: [[Module 01 - Orientation and User Stories]]
**Needed for**: [[Individual Project 1]] — Task 3 requires you to submit **cURL commands** demonstrating API bugs

## Topics to Cover

### Request Types
- [ ] GET — retrieves, must not change state
- [ ] POST — submits new data, may change state
- [ ] The wider [vocabulary of HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) — PUT, DELETE

### Anatomy of a Request
- [ ] URL — protocol / domain / port / endpoint
- [ ] Method
- [ ] Query parameters (GET) vs. body (POST)
- [ ] Headers — `Content-Type`, `Authorization`, `Accept`
- [ ] Response — [status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) and response body

### Authentication
- [ ] [API key](https://www.ibm.com/think/topics/api-key)
- [ ] [Bearer token / JWT](https://www.okta.com/identity-101/what-is-token-based-authentication/)
- [ ] Basic auth
- [ ] OAuth 2.0

### Practices
- [ ] [Environment variables](https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa) for secrets and repeated values
- [ ] [Request/response validation](https://medium.com/@theqachronicles/validating-api-responses-8ee9df01ef26) — how GameNite's shared zod schemas do this
- [ ] [Server-side error handling](https://blog.postman.com/best-practices-for-api-error-handling/)

### Testing Endpoints
- [ ] In the browser (GET only)
- [ ] [cURL](https://curl.se/docs/tutorial.html) — required for IP1
- [ ] Postman

## Notes

## Related

- [[Individual Project 1]]
- [[Tutorial - Unit Testing with Vitest]] — testing async HTTP code
- [[Module 01 - Orientation and User Stories]]

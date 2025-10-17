Hyper Text Transfer Protocol

Client-Server protocol where the client sends a request to the server and a response is sent back to that request from the server.

---

## The Request

**URL (Host/Path)**
- The Uniform Resource Locator needed to locate the specific service provided by the server

**Method**
- The way for the request to specify what it generally wants to do
- GET
- POST
- PUT
- DELETE

**Headers**
- Additional data that helps a website determine what response to make for a given request

**Query String**
- Part of the URL and provide parameters to the request
- Example: `?q=test&state=MA`
  - 2 parameters passed: `q` and `state`
  - Key-Value Pairs separated by ampersand (`&`)

---

## The Response

**Status Code**
- Indicates whether a specific HTTP request has been completed

| Range   | Type                | Description                    |
| ------- | ------------------- | ------------------------------ |
| 100-199 | Informational       | Needs more info from client    |
| 200-299 | Success             | Request successful             |
| 300-399 | Redirects           | Server moved                   |
| 400-499 | Client Errors       | Invalid request                |
| 500-599 | Server Error        | Valid request, server fault    |

**Body**
- Where the server provides data back to client

**Headers**
- Additional data sent from server to client
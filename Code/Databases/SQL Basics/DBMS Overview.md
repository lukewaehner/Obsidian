
---

## DBMS Overview

**DBMS** - Database Management System

A financial information system that provides data storage, retrieval, and management.

---

## Logical Schema

Describes the structure of data in terms of relations (tables).

**Example:**

```
Students(sid: string, name: string, gpa: float)
Courses(cid: string, cname: string, credits: int)
Enrolled(sid: string, cid: string, grade: string)
```

Questions the schema can answer:
- Who takes what courses?
- What grades do students have?

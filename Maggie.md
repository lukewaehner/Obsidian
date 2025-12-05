## Summit CRM
Acuity Squarespace
Relay -> Onboarding form, copies to google sheets
Two full time teachers

---

First tools:
- Email automation:
	- needs review send to consultant
		- Can this also be added to click up
	- reviewed -> email to student
	- Send notes upon request
		- Meeting notes in a cell, specific sends for specific meeting notes
		- Send from broadcast sheet
	- Different emails for each consultant
- New tasks resources are automatically copied and shared to students spreadsheet, then put in their student folder

- Grab meetings from Acuity - Need API key from 
- Maggie


---

Links:
- [Student Sheet - Template](https://docs.google.com/spreadsheets/d/16sXvwNSC2-0dNuDdmRdzJvxOil2C0YqPFanC_fPmqTA/edit?gid=1570327885#gid=1570327885)
- [Master Sheet](https://docs.google.com/spreadsheets/d/1lLnHazBVkzL2ajKObtHqNCK0nEW3bCX3I8mDCquoEgw/edit?gid=55296015#gid=55296015)
- [Meetings Data](https://docs.google.com/spreadsheets/d/1P5RoKtaRaj6AXCnyZOqFr_hSZShFkj6kF8vT8SjGh6Q/edit?gid=0#gid=0)

---
Work:

| Date  | Time Logged | Completion                                                           |
| ----- | ----------- | -------------------------------------------------------------------- |
| 12/25 | 2:30        | JS Typing, Global Config Setup, Set StudentData, Upload Meeting data |
|       |             |                                                                      |

Todo:
- Email Latest Progress + Menu Bar Activaiton
	- Hook all students off StudentData Sheet -> push to menu bar
	- Pass URL of student sheet through menu bar to sendMeetingNotesEmail function
	- Open student sheet, grab date / time + meeting notes, format into email, send to email associated with StudentSheet F5
- Review Work / Reviewed emails. Review Work to designated consultant, Reviewed to student + parents

Add extra features:
- Make student sidebar manager sorted alphabetically
- Add in ApplicationTracker: Check supplemental status for Needs Review
- Setup outbound email template to match student meeting notes template
- Share resources (google docs) from Tasks -> Your Shared Folder on Home Page, overwrite with <Name - Document> on tasks page, stop new overwrites with this

Done
- [x] Email Automation ✅ 2025-12-03
- [ ] Share tools with students
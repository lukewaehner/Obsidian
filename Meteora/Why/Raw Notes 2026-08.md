---
tags: [meteora, why, raw]
sources: []
verified: 2026-08-27
---
Zoom:
https://us06web.zoom.us/j/86793827078

If we get updated information for a specific ticker / email chain, or they go in claude and tell 'SVAC email chain, look at the email chain and update the S-4'.

1. Scan brain stuff to email through vdb@

Last Q/K date
Cash held in the trust account
Last reported CIT per Q/K
Sit w/ Shiv and work on this

Have a heatmap hashset track w/ covered email from merger arb, and the type of thing that was ingested, basically just throwing a log in. @ rishi shiv on this

Balanc sheet date
Last report
Cash in trust
Tax
Shares oustanding


Update CIT Bot:

No need for BS, CIT, Column 3, column 2, filing type

Take yield model and run a V-lookup for all the names

AK -> AO VLOOKUP from Yield Model v124 yield model page. (Use ticker on column C?)
9-11 cents trust accrue, shouldn't be off by that much unless working capital withdraws (should note if this is the case)

The other case if is there are taxes (95% are Cayman or BVI with no tax, 5% are Delaware / Nevada w/ taxes but are old). Note this as well.

If we have 12/31 Q and they file a 3/31 Q it should flag itself

Verbiage points:

https://www.sec.gov/ix?doc=/Archives/edgar/data/0002073515/000149315226035959/form10-q.htm

Trust:
Cash and marketable securities held in trust account
500kk auth, 12kk outstanding

121464805/12075000 = 10.06

Cash withdrawn from Trust Account as tax and regulatory withdrawal - The company may withdraw up to 10% of the earnings in the Trust Account ... the comapny withdrew $xxx,xxx.

(search for this wording to check working capital withdraws)


Why are some of the Date of last report CIT different from balance sheet date
Separate the Vlookup from Edgar lookup on the sheet

Last reported CIT from Yield Model & New value fro mEdgar w/ Date, value, cash in trust, tax, shares outstanding


Same data set
But w/ new from edgar old from yield model.
Needed: Date, CIT Value, Cash in trust, Income Tax, Shares Outstanding
New set as of 6/30 old set from 3/31 or from before.
We should see the new values increasing from 9-11%

Ticker, <Dataset1>, <Dataset2>, Status, Range note.

**Website w/ snapshot:**
Scatter plots
Zoom in, expand, etc.
Change the VWOP (against 1 week vs intra day, etc)

Yield plots, median yields.

Live refreshing?

Top moves, etc as tabs.

Make it all one table so we don't lose the numbers when filtering.

Delta in days + CIT value on column P/Q
Should all be a standard sloping line for the most part (graph for this?)

All taxes come strictly from the balance sheet



*Skill Auto Drafter*
Vik emails about a new skill, and provides what it needs to do.
We can poll the email on a schedule with the MCP tooling, looking for relevant hits, if a new skill request is hit and looks to be valid, claude will initiate a first draft, iterate on it whatever, and ping us an email.


Since the workflow is mainly: spec hits, we build it out, send it back for feedback, Vik will give feedback. Most overnighting of 'new skill request @ 8pm' can be done overnight.

Spac yield to treasury
What line of best fit
Market reward to short duration risk vs long duration risk

Cash and Investment Held in Trust Account
As of the Q date, write down if held in US Treasury bills or demand deposits
New page in the spac yield sheet


Graph:
'What spacs are related to this'
Link docs over target company, or stated mandate of the team or qualification of the team & ties to the industry
over memory docs ONLY

Price data - pre market and post market to hitch results off of
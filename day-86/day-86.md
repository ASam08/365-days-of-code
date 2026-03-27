#  Drizzle - Part 2
Welcome to **day 86** of 365 days of code - coding every day for a year, little and often

I'm sort of waiting for the other shoe to drop...converting these SQL queries to drizzle syntax queries is...straight forward? Honestly, the syntax is logical, and I guess I wasn't expecting it to all just work.

I've spent my time today working through my select queries and starting to update them all across. So far the only issue I've come across is of my own making, where I had typed a column for day_of_week as a varchar type in the DB originally, and then just used it as integers, and had the type for the return just expect a number. I suspect if I'd had drizzle going from the start, I probably would have caught it, but it also meant I got to work out doing a migration for the first time as I've gone through and changed the column type to an integer and converted the data.

I will need to work out how I apply that migration to the dockerfile when it comes time to actually release this, but that's a future me problem (or learning opportunity, depending opn how you see it).

Anyway, that's it, it's easy (so far), I fixed an earlier oversight on my part, everyone's a winner? Really hoping these easy comments don't come back to bite me later.

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/2444d7f46861cf67539addfc6d1a12c8cabf1ad7) if someone wants to go have a look at that point in time.


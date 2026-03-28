#  Drizzle - Part 3
Welcome to **day 87** of 365 days of code - coding every day for a year, little and often

I think I'm starting to sound more and more like a [Drizzle](https://orm.drizzle.team/) fanboy at this point, but it is awesome. Today whilst converting my SQL queries over to Drizzle, I came across a few queries where I was converting the input to a time type as part of the query. Yes, it's probably not best practice, but it was the best way I could think to do it at the time, given that the typescript variable is a string type. Anyway, it's a bit left field, and Drizzle doesn't natively support it, but no worries, you can just write normal SQL anywhere yo want in your Drizzle query, so I just chuck in a ```sql`${time}::time``` and we're all good, no big dramas. 

It. 

Just. 

Works.

Honestly, massive props to the devs for it, it's been awesome so far.

It has actually been quite good reviewing all the queries, it's given me a chance to look over them again, and simplify things in a few places, and also return the actual type specified in a few others, saving me from future headaches.

Anyway, I managed to get all the rest of the actions.ts queries cut over today, so that's all the "SELECT" queries done. I guess that means tomorrow I start on the "INSERT" and "UPDATE" ones in my actions.ts file. Should be some interesting learnings then...

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/1e513b7149642910f8ba493ae9a8d5b21e8d64ea) if someone wants to go have a look at that point in time.


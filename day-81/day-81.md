#  Sometimes It's Simple
Welcome to **day 81** of 365 days of code - coding every day for a year, little and often

Ahhh the lessons we learn about typing. Yes I'm still going on about the typing stuff from yesterday, why? Because today my time was spent trying to work out why my build was failing from an overload, the culprit? Typing, of course.

It turns out when I wrote the data function to check for conflicts, I had added the wrong type for the outcome of the SQL query. Basically I had only typed for the ID and nothing else, so when it started getting back the subject, start and end times, problem. Anyway, that is fixed and the feature for the conflict check is now live (hooray!).

I think (I know I've said this before), I'm at the point of just needing to do the rebrand stuff, and then I will have enough together for a proper MVP release, ready for some real test users.

I know, the list of things to do is long, and probably in this order:
- A thorough check through of all of the typing
- Add in some sort of ORM, probably drizzle, but that will be a learn from scratch experience for me
- Add in some sort of testing so that I can...
- ...Sort out some propert CI/CD workflows
- Everything and anything else

Seems like a lot when it's written down like that, but we all know you can only eat an elephant one bite at a time (metaphorically of course, not advocating for actually eating an elephant).

Anyway, I guess the fun continues tomorrow...

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/69395d18db3583baf2631ad69394265693f9f125) if someone wants to go have a look at that point in time.


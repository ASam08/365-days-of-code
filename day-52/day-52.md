#  Auth Time - Part 7
Welcome to **day 52** of 365 days of code - coding every day for a year, little and often

Ok, so today I started working on the backend logic for the signup form. I started by adding a column to the users field for enabled. I've set this to true by default, but when I'm piloting this, I want to limit the user base a little if I'm offering it out wider, so I'll use env variables to set it to false and then load users in as false. It means I'll be manually editing the DB to enable them, probably not ideal, but it's just for now.

Anyway, it meant I found out about postgres handling "ADD COLUMN IF NOT EXISTS" which is super handy for this sort of thing, definitely a win for postgres.

I also then got started on the backend of the form, including field validation, checking that the two entered passwords match, and then adding the user to the DB. I have come unstuck with something somewhere, an error that is being thrown that I have just run out of time to debug today, so not quite complete, but I guess that just gives me something to focus on for tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/64d2de5b00a06ae8a0c4d64cdb7de5e349091bfb) if someone wants to go have a look at that point in time.


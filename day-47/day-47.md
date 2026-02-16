#  Auth Time - Part 2
Welcome to **day 47** of 365 days of code - coding every day for a year, little and often

Another day, another bit of auth... I believe I have all the building blocks in place for the auth now, I have the ui ready, and in theory the auth flow is working, I just haven't tested it yet. I kinda need to create a user to be able to try it, and I'm not super keen on seeding a user, so I need to get the signup flow going in order to get to where I need to be.

One thing I did have to think about was self-hosting. In the end I want to make this self-hostable, and in a lot of situations it doesn't make sense to have auth set up if it's just running in a home lab, with one user etc. so I wanted to be able to turn it on or off. I've chosen for now to make it an optional feature to ***turn on*** as opposed to turning it off, so you have to declare the "AUTH_ON" environment variable as true in order to turn auth on (this definitely also needs testing).

That's the task for tomorrow, get sign up in place, or at least on it's way. I might give in and just seed a user to be able to test things (I probably should do this), but who knows, it's a fun discovery for tomorrow.

Anyway, not too much to show off just yet, hopefully soon! More tomorrow

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/2f60c9ca9206e42cb9f3e7cbc3ee355ca855951e) if someone wants to go have a look at that point in time.


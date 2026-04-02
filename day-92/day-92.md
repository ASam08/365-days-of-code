#  Update Everything
Welcome to **day 92** of 365 days of code - coding every day for a year, little and often

Today is probably another one of those days where I've tried to do too much on an already busy day, but I have got the uuid piece from yesterday working now. First I went and removed the generate uuid for new instances with no auth from the get user id flow, and added it into the add timetable set flow, seeing as how that was the only time it would ever be used, it just felt cleaner that way.

Then, surprise surprise, it still wasn't working...and the deeper I looked, I realised that none of my updates were flowing through to my docker image, even when I was forcing the workflow on the feature branch...then I realised, even when I was choosing the feature branch, it was still just packaging main, d'oh! So I made a change to the packaging workflow, and fixed that issue, and lo and behold, the uuid issue was fixed too.

Anyway, then I wanted to start on the dependancies/package updates, but I also wanted a small safety net on these, so I added a workflow that just builds the app when a pull request is generated, and checks for any failures. That at the very least should stop me in my tracks before I get any deeper into testing, and guess what, it already saved me a bunch of work once.

Anyway, one of the big updates I had to do was update Next.js to 16.2.2, so I've done that and tested it, but still a few smaller ones to do tomorrow, then it will *finally* be time to create the release for this.

Phew! More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/1a42eb63fb525c5e58af41840773de5b99d867c2) if someone wants to go have a look at that point in time.


#  Testing - Day 1
Welcome to **day 96** of 365 days of code - coding every day for a year, little and often

Well, I guess you can see that we're kicking off a new "series" (sounds like some sort of youtuber...), Testing (hooray?). I'm not sure that this is going to be super thrilling, but it is definitely going to be a learning journey, I can see that already just from day 1. It's also not going to be as straightforward as implementing Drizzle, but hopefully just as good when it's done.

Today was just about choosing a test framework, getting the ground work done, and getting a successful test. Right off the bat I will say I encountered a bunch of errors today, and I did end up using my friend Claude quite a bit to decode and understand them. It was mostly to do with getting my config right, but also a bit of understanding the limitations of testing suites. For starters I was going down the path of Vitest, but I just ran in to so many issues that I decided to abandon that and go with Jest. I'm not convinced I fully understand the Vitest issues, and maybe it will come back another time, but for now Jest is actually working, so I'm sticking with that.

Anyway, the tests I generated were just two simple ones, check the login page renders the logo, and check that it redirects to the dashboard page when AUTH_ON is false. And what do you know, they both passed (funny that).

Tomorrow will be diving a bit more into understanding the testing framework, how to better write the tests, and then I guess putting that all into practice, wish me luck! More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/5521c25c47c0ab9c4d01f8d8c63e690f9d3de4d8) if someone wants to go have a look at that point in time.


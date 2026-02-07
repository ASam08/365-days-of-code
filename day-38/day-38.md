# TODO - Tidy Up
Welcome to **day 38** of 365 days of code - coding every day for a year, little and often

Today I wanted to keep on the tidy up train, and get rid of the last of my hardcoded details, the user ID UUID's. The current plan is still to implement auth, but to make it optional if you are self-hosting this, and at the moment the auth doesn't exist so it was a good time to test that things will work with the no-auth flow.

Having the ability to spin this up in docker, blow it away and try again has come in hugely handy, as I could test it both on my testing version which already has data, and on a blank version with no data, i.e. a new install state. Given that I'm getting the UUID by querying the timetable_set owner_id, seeing this on a fresh install definitely uncovered some issues that I could remediate. I don't know if this is the best way to do this type of auth flow/no-flow, but it's working for me, so I'll run with that unless I discover it's a really bad idea.

Anyway, more tomorrow, maybe some work on the auth stuff, who knows

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/f14989f8024caa62d2d8644f062de78f0547adc2) if someone wants to go have a look at that point in time.

*It would be a pretty boring screenshot today sorry folks*
#  Auth Time - Part 3
Welcome to **day 48** of 365 days of code - coding every day for a year, little and often

After yesterday, I kept on thinking about the fact that I probably should seed a user and test the auth stuff through, so I did, and I am happy for it...

Yes, I found some issues, in particular I hadn't added names to the inputs in the sign-in form, so the formdata for user and password wasn't going back to the auth process, so no signin. I fixed that up and things started coming right straight away. I'm honestly pretty happy with how the auth piece is going, but...

...It has revealed some issues with the timetable page. In particular, with a fresh new user, even after creating a timetable set, nothing shows up, and of course I've hidden the add a new block button if there is no set detected (facepalm), so now I have that to fix.

It's not going to happen today, it's a fix it tomorrow issue, then I'll be able to test through the auth better for sure, then I can do the sign up. It might mean another day before I get back to sign up, but good to be finding these issues and being able to fix them.

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/9fbde3e40abdee48b6efea4c1b80e46469bf1a49) if someone wants to go have a look at that point in time.


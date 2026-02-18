#  Auth Time - Part 4
Welcome to **day 49** of 365 days of code - coding every day for a year, little and often

If I'm honest the auth stuff is starting to feel like a bit of a drag, alot of two steps forward one step back, but it is progressing. Today was a chance to fix up the issues I found yesterday, and on the face of it, it was a pretty simple fix, I had put some placeholder stuff in the getuserid action, and just needed to go there and get the user ID from the auth session. Except, the auth session didn't have the user ID in there yet, so I had to fix that. 

And then I realised that I was passing the userID from the formdata client side, which isn't great for security, so I've now spent some time removing all of that. It's caused one or two issues of it's own, and I've had to call it a day for today, something to come back to tomorrow. The main thing is I was using the presence (or lack thereof) of the user ID as an indicator to show something specific on the dashboard cards (i.e. you don't have anything set up yet). That's all well and good, but because I've removed the user ID from the component, I'm now using the fact of whether or not there is a next block, or current block, or current break (depending on the card), and that's not working perfectly. I think the fix is pretty easy, I just need to go do it, so hopefully that's some low hanging fruit for me to resolve tomorrow.

Boy am I starting to see the value in doing all this work in a separate branch... tune in again tomorrow folks.

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/e86f4d27bd536675de7652cf6b16344baf85a67b) if someone wants to go have a look at that point in time.


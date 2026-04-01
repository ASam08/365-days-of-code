#  Drizzle - Part 7
Welcome to **day 91** of 365 days of code - coding every day for a year, little and often

Ok, it seems like Drizzle is done! I went with the option of converting over to gen_random_uuid as it just seemed cleaner in so many ways, except for moving my test instances over, that was a bit of a pain, but it's done now, so happy days.

I did uncover a small issue in my testing, whereby a new instance, with auth off, couldn't create a first timetable set because there was no user and no existing sets to pull the user from. I admit my solution here isn't elegant, and I probably just need to set up a random uuid and user as part of the first set up, but that's something to look at later. For now, I think I decided to make it so that if it couldn't find a user, it would generate a random uuid to use as the user. However that's not working either, so I need to dig into that tomorrow I think.

Anyway, I was hoping to create a release for the drizzle stuff, but on top of the issue above, I've noticed some package updates that I need to do (and test) before I do, as it wouldn't really be good manners to create a release with known issues, so will get that done tomorrow and then will start looking at creating some test scripts, so that I don't have to manually do it every time!

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/a0dc02ef0a4cfc2ffa61796f3fa842f79ca5d895) if someone wants to go have a look at that point in time.


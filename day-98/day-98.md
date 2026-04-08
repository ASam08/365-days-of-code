#  Testing - Day 3 - And More
Welcome to **day 98** of 365 days of code - coding every day for a year, little and often

Well today has had some successes. I managed to get more of an understanding (as hoped) of Jest, and figured out the issue with the dashboard tests, which are now all working. I decided to bite the bullet and jump into some of the bigger stuff with the data.ts file, effectively all my server side data fetches. I know, I'm note really following a logical order here, and I should, and I will, at some point.

Anyway, working out Drizzle and Jest is a bit of a mission. I have leaned on some help from my friend Claude, and haven't got all of the tests working quite yet, but a good chunk of them are and so I'm feeling pretty pleased with the progress there.

I then had to switch things up a bit and address some vulnerabilities in a few packages used in the main build. This was a good chance to use test some of my git knowledge, stash, switch branches, create a new one, apply the updates, update the pnpm packages on my local machine to run through testing (without the scripts), push the branch, merge it, then merge main into the testing branch, reapply the pnpm updates as the dev packages for Jest had disappeared, then finanlly pop the stash (realising I really should have named it...). But it all went well and it actually felt pretty good to have the confidence to do all of that.

Anyway, more tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/846ff7ce2545a27524d84a4490d1be956039e18a) if someone wants to go have a look at that point in time.


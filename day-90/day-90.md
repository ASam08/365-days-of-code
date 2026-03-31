#  Drizzle - Part 6
Welcome to **day 90** of 365 days of code - coding every day for a year, little and often

Honestly I was really hoping today would be the last drizzle day, but alas, it's not to be. I spent a bunch of time working through the options to run the migrations through the dockerfile, but after a few false starts, I came across the instrumentation.ts file option in nextjs, and...it worked! A few minor issues to work through, like making sure I had a health check in docker compose, so that the instrumentation didn't try to run before the DB was created (I'm not 100% convinced that's the right call, maybe I should be doing the healthcheck in the instrumentation function, but I can change that later on).

Anyway, we were there, I had merged the PR, because I thought I needed to do that to get the github workflow to create the container (sidenote, no, you can run the workflow manually on any branch, always learning), and despite testing it on my local test version, which was an already established DB, it didn't work properly. Drizzle hadn't picked up that I was generating UUID's via uuid_generate_v4, which requires adding the uuid-ossp extension, so that wasn't in the initial schema or migration.

I ran out of time again today to fix that, but as I see it I have two options, either add in the extension or use gen_random_uuid. I think I'm probably going to go with the latter, if I don't need to add the extension then why should I? But I will think about it and make a call before implementing tomorrow, then hopefully(!) we will be done with the drizzle piece.

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/b63eaa9f16aab953685f0d01a6ffedeaef1cb755) if someone wants to go have a look at that point in time.


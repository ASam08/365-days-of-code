#  I Knew It Would Be Basic
Welcome to **day 67** of 365 days of code - coding every day for a year, little and often

You just don't know what you don't know...I knew the issue I was having yesterday with the userId not being triggered properly on the docker build would be something small, one line of code somewhere, and it turns out it was.

So yesterday, I couldn't get anywhere, GH Copilot was trying to help, but no joy. Today I turned to my good friend ChatGPT for a second pair of eyes.

The solution it provided, and that I've used, is to force the page to be dynamic. I hadn't really understood how the caching worked, but I know understand it goes a little like this (correct me if I'm wrong). At build time in docker, using the dockerfile, it doesn't have access to the env variables, or really the DB, so when it does it's initial page builds, it's going in based on no users etc. That page is then cached and used when it's called, as there is no dynamic content being rendered on the page at that point in the code, no need to re-render everything. By forcing the page/component to be dynamic, it is being re-rendered every time it's called. According to ChatGPT "Pages involving auth or per-user data should almost always do this."

Now, I don't know for certain that any of the above is correct, or best-practice, or any of it. All I know is that it worked. It goes back to the idea of using AI as a second pair of eyes, not the master of the universe. In this case, that second pair of eyes found the issue and a result. From the basic research I've done outside of AI, it does appear that "export const dynamic = "force-dynamic";" will increase server load (makes sense) and possibly slow things down/cost more to host, but is a bit of a neccesary evil, just use it sparingly.

Anyway, I'm glad to have that out of the way and working, it makes me feel better about carrying on with sharing the app and the journey.

More tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/7b44ce11ece21b6fa1a8fe659d8f6c5a42613718) if someone wants to go have a look at that point in time.


# Clean Up, Tidy Up 
Welcome to **day 35** of 365 days of code - coding every day for a year, little and often

Today was a bit of a tidy up day, relatively unremarkable, but important to do. In amongst the tidy up, the big ticket items was to remove all hardcoded references to setID. Everything now uses a hardcoded User ID until auth is implemented. This means that once I have auth in, I just need to use the user UUID in place of the hardcoded variable.

I also did a bit of work to start getting the app ready to be containerised, via Docker. This feels like the natural next step, as a self-hosted version probably doesn't need auth out of the box, and if I'm honest, I think it would be cool to share if someone else found it helpful and wanted to self host easily. So today I did a bit of work to sort out creating the DB URL from .env variables for the various components, which will be needed if running from docker, as who wants to make sure they get their DB URL correct manually...

Anyway, that's it, not glamorous, but neccessary today. More tomorrow!


> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/63d62f3d4c0f194a589d8f5dde3d992faac1e64a) if someone wants to go have a look at that point in time.

*Nothing for the screenshot fans today sorry, hope to have something for you tomorrow*
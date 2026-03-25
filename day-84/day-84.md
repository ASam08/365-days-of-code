#  Package It Up
Welcome to **day 84** of 365 days of code - coding every day for a year, little and often

Ok, so today I worked on the github workflow to get a docker image published to ghcr everytime I release(?) a release (that felt like a weird phrase...). All in all, the actual action of creating the workflow seems to have worked pretty well. I added in the ability to manually run the flow and as far as I can see, we're in business.

The only problem comes with the the DB. I have been relying on a db.init script to run when postgres boots for the first time, to initialise the DB with all the tables etc., and that works great when your users are cloning the whole repo and it's just there, but when you're building from an image, without all the files being local to the user, it all breaks down. I have looked at it a few ways, and I could create a custom postgres db image, but that's a pain to maintain. I could add a dockerfile.db to the repo and get that built locally, but also not great. I think in the end, the way to go is to actually implement an ORM solution, so I guess I know what I'll be doing for the next few days.

Not ideal to have the docker image published and not really workable, but I haven't updated the README to show that it's there, so as far as anyone knows, it's not, and it shouldn't trip anyone up (look at me, talking as it people are using this app already, even though I haven't advertised that it exists anywhere, except here...).

Oh, I also added in a redirect to the root page, because I realised that if you just went to the root URL, it still went to the nextjs example component. Not anymore, that now redirects to login, which itself redirects to the dashboard if you're already logged in, or have auth off.

Anyway, more tomorrow...

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/ed727773f2139428619c7c4f373d7cffef2811fe) if someone wants to go have a look at that point in time.


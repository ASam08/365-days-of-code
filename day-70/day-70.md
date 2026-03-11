#  Groundhog Day?
Welcome to **day 70** of 365 days of code - coding every day for a year, little and often

Quite a big day today all told. In sorting out this day of week stuff, it's triggered me to tidy things up a bit better for the future. Yesterday I created the defaults file, today it's the constants file. Basically somewhere I can house any constants that I want to be the same across the app. I've started off with adding a few constants for day of week arrays and tuples. Having these in one place allows me to reference the same constants from both the settings page and the timetable page, meaning I *shouldn't* get these out of sync with each other in the future.

Aside from that, I now have:
- The checkboxes on the settings page are now saving true/false values for each day of the week when saved.
- The timetable grid is now getting the day of week headings from the constants file mentioned above, this will allow me to filter these in the future when a user has hidden a day of week.
- The timetable grid now adjusts the number of columns dynamically based on how many days are to be displayed.

A few things still to fix up here:
- The checkboxes revert back to their previous state on the settings page when saving until you hit the refresh button - Not ideal...
- When adjusting the number of columns on the timetable grid to less than the full week, the column sizing becomes inconsistent - Not great UI...

Aside from those things, I'm pretty happy with the progress, it will be a slower day tomorrow, but good to have some good progress. I do need to get better at making smaller commits for each part of a feature I deliver, I realised when writing the commit message for today's work that it wasn't really ideal to try and cram all of this into one commit, a lesson I need to learn.

Anyway, more tomorrow!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/1e170d613da7b17b4dc9ff01117dab00aabf7367) if someone wants to go have a look at that point in time.


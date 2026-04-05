#  Fix It Up
Welcome to **day 95** of 365 days of code - coding every day for a year, little and often

Just a short one today, but back into actual code again. I had noticed an issue with the add timetable when using a new instance that had no settings yet. Effectively the "Unhide Day" prompt was always coming up for the first block added to each day, not a great user experience, so something to fix.

Anyway, a little bit of diagnosis later, and it was really quite simple, I had multiple ifs following each other, but what I really needed was to change the second one to an else if. Like I said, not a big piece of work, but good bug fixing practice, and something that needed to be sorted.

I think I'll bite the bullet in the next few days and start working on the test pieces, but while I'm thinking about it, probably good to re-do my list from a few weeks ago of my priorities:
- Add in some sort of testing so that I can...
- ...Sort out some more thorough CI/CD workflows
- I'm considering replacing the data/actions files with actual API flows, which means I can possibly test in a different way, but I guess I should really make that call before I do a large amount of test writing
- I'm also considering swapping from auth.js to better-auth. It seems to have a lot more functionality out of the box, something to look into anyway. It would also open the gate towards password resets/changes as well
- Maybe internationalisation
- Multiple timetable sets for a user. Some of the readiness for this exists, but not implemented. Coming with that might also be sharing timetable sets across users...
- Edit a timetable block, instead of having to delete it and create a new one

I am also thinking of taking some of the learnings from this project, and getting into a new project that has been going around in my head, but will give that a bit of thought.

Anyway, more tomorrow, who knows what it will be from the list above!

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/7134378197b4e05827d7caafc84d8f28de5cad60) if someone wants to go have a look at that point in time.


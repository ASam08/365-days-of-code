# Habits Integration
Welcome to **day 12** of 365 days of code - coding every day for a year, little and often

More work on the running tracker today. This time, integrating it into the habits tracking app that I use, an open source self hosted tool [Beaver Habit](https://github.com/daya0576/beaverhabits). I've been using this app for a while, it's uncluttered, does what it says on the tin, but surprisingly customisable in terms of setting habit repetition etc. It's perfect for tracking my running (which I want to aim for 3x per week).

This was a case of using [this handy guide](https://github.com/daya0576/beaverhabits/wiki/Beaver-Habit-Tracker-API-How%E2%80%90to-Guide) to produce the API calls, and I thought given it was a bit of an add on feature, I'd try writing it in a different file and importing it in, a new thing for me. I also had to use my versioning table that I put in previously to "migrate" to this new version, create the table etc.

A cool success for today for sure. There are a few things I want to tidy up and they are on the to-do list now:
1. Add in a settings type menu where I can give the user the option to either reconnect or connect for the first time if they skipped previously.
2. At the moment every time it creates a run, it's authorising to the API again. This probably isn't a major issue given that I'm rarely going to be entering more than one run at a time, but it would be good manners to try first, and if a 401 is returned, then auth and try again.
As always, something for another day.
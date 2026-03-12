#  Learning Learning Learning
Welcome to **day 71** of 365 days of code - coding every day for a year, little and often

Another day, another lesson. Today I discovered controlled and uncontrolled inputs... It turns out that the way I have the checkboxes set up, they are uncontrolled inputs, and defaultChecked only has an effect when the input is first mounted, so the router refresh and revalidate path had no effect.

Anyway, it was a simple fix, to add the state.timetable key to the form, and voila, when the state changes, the form reloads in it's entirety and defaultChecked runs again.

I also added the behaviour behind defaultChecked into it's own function, I did it when I was troubleshooting, but it's probably tidier to have it there anyway.

And that's it, not a big day today, but one of the two issues from the day of week settings I wanted to resolve, I guess that means I'm working on the timetable formatting tomorrow...

> [!NOTE]
> For this timetable project I won't be copying the whole codebase into this repo every time I work on it, instead I'll just [link to the repo](https://github.com/ASam08/timetable-app) and even link [direct to the commit here](https://github.com/ASam08/timetable-app/commit/f70056f8e2ef9b1cd234eb734947bddee3920f37) if someone wants to go have a look at that point in time.


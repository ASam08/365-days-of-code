# Show & Tell
Welcome to **day 11** of 365 days of code - coding every day for a year, little and often

After a few days away from it, I went back to the running tracker today, with a feature add that I've been thinking about the last few days. I already have the overall stats, now I want to be able to see the detail on each run, so I've added in a "View Running Logs" option.

When it's early in the year, this is going to be a nice small list that can fit on one screen, I didn't want to get a few weeks down the track though and be seeing a massive long list to scroll through, so I included pagination, 10 runs per page. When I was looking at the best way to do this, I knew I needed some better structured data, and I didn't want to make a DB call every time a new page loads, so I went straight to a pandas dataframe. Using the loc function, I could specify which rows to show on each page in a loop, and I'm really happy with the results.

While I was tinkering, I also spotted a potential issue where if a choice wasn't given for the type of goal in the goal setting function, it would error out, I fixed that by checking the input and looping until a correct input is given. Probably something I need to be more aware of and look out for elsewhere.

Having this feature in place will let me work on something else in the future, editing and deleting logs, but that's a task for another day.

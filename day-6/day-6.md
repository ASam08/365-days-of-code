# Contain It
Welcome to **day 5** of 365 days of code - coding every day for a year, little and often

In my home lab, I have a *ton* of docker containers running, I'm sure lots of folk can relate to that. I can run them, update them etc. but I've never tried to make one, so that was today's goal.

It's a super simple python script, that just pulls from [itsthisforthat.com](https://itsthisforthat.com), a fun project worth checking out.

If you want to run it, pull the files down, run "docker build -t {give it a name here} ." (newbie learn, the "." is important), then "docker run --rm {the name you gave it in the last step}". It just spits out into the command line, nothing fancy in the script, today was all about containerising it.
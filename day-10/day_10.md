# Github Actions - Daily Upload Check
Welcome to **day 10** of 365 days of code - coding every day for a year, little and often

So today I spent time working something that has been rattling around in my head for the last few days, and it gave me a chance to try out some new tooling, Github Actions. The basic idea is that each time I push a commit to this repo, it will check to see if it includes the creation of a new daily folder, that is the correct folder for that day. After not too much wrangling I got the check working, the next step was to do something with it...

End goal, I'd love to have this auto updating my habits tracker that I tick off each day to say I've done this, but that felt like a bridge too far today, so I settled on getting a notification through my self-hosted NTFY service...big mistake.

For the life of me, I cannot get it to connect through to my NTFY server, I'm 99% sure it's something in a setting buried deep in cloudflare, which I use to expose NTFY publicly, but I'll be damned if I can find the right setting there. So with frustration setting in, I've made the call to leave that particular battle for today, and try again with a fresh head another day. Not the success I was hoping for, but a good chance to learn the actions piece and get the logic working for the check.

---
*Update - 20 minutes later*
Ok, I found it, Cloudflare's logs finally updated and it was being blocked by "Bot Fight Mode", once I turned that off, I could re-run the workflow and lo and behold, all is happy :)

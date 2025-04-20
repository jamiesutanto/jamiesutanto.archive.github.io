---
aliases: 
type: note
cssclasses:
  - img-grid
  - embed-strict
  - wide-page
  - max
date: 2025-04-16
tags:
  - 2025/Apr
title: Tutorial - The Joy of Being Hacked
draft: "false"
---
# Lesson
Being hacked BEFORE your site is made public has been the best tutorial for the internet!
# Story
It's 6 AM in the morning, you wake up and appreciate the joy of a tutorial to introduce you to the internet.  This is my inspiration for my blog post today, much different then my much more panicky self yesterday!

So here's my story for today.
## The Night Before
It's 10 PM and after mulling ideas for your first post, you build up the willpower to actually start writing.  You log-in and are introduced to a spam site...  Welcome to the internet....

Your first thought is panic!  How could this be with such a fresh domain name that hasn't even been made public.  Post-Reflection ...*And then you realise that everything on the internet is public from the day it's published!*
## The Search
As with all problems, first stop search for an answer! 
- "Website replaced with spam site"
- "Website points to site I didn't make"
- "Porkbun site suddenly changed"
- "URL points to spam site"
- "Website hacked"
Then you realise there are A LOT of different ways all of the above could mean, but after much reading you learn the terms DNS Poisoning, URL Hijacking and URL Re-direction and so many other terms that you realise you may be out of your depth!
## Porkbun Adventures
Good news, you have Support, so a message to Porkbun and you realise you likely won't get a reply for 24 hours.....

So time to just experiment!  And see what actually causes the site to resolve incorrectly.  So delete all settings you aren't aware of.
- URL Forwarding..... Still there.
- DNS A Record.... Still there.
- DNS AAAA records.... Still there.
- DNS MX records..... Still there.
- DNS TXT records..... Still there.
- 
So sounds like it's time to go more nuclear, where you find the Porkbun Park command!  Reset to Factory Defaults exactly what I was looking for!  And.... still there.

Few more searches, and all these changes do take a while to apply... For me about 30 minutes, and finally arrived at a wonderful Parked page!  Time for some tea, and back to square one!  

Reconnect Github Pages on Porkbun.... and it came back!  Looks like it's actually a Github Pages issue, so onto the next rabbit hole.
## Github Pages Adventure
Back to Github Pages, apply your custom domain and greeted with the message of:

"The custom domain thesinglerun.com is already taken.  If you are the owner of this domain ..."

Follow the link, and didn't actually understand how to re-claim it (it was late!), so first stop Github Support!  Where the first thing you realise is that Free users can't actually create support....  

So instead a Virtual Assistant happily offers to check your domain name, and reports all is well!

Great!  Go back, and try to add the custom domain and still taken.

So, back to the support board with the many options to try and create a post!  Create Ticket was in the less obvious top right corner (away from the big squares) and once there punched in my description.

Github has a handy Co-Pilot check and try to address your problem BEFORE your ticket gets submitted, and strangely reading the exact same docs as the previous link in chat form made sense!  

With these new instructions setup my DNS TXT file, added my custom domain, and boom my site is back!

## Post the Actual Fix!
Strangely after realising the root cause I wanted to know how widespread this was!  (It's strange how the human brain works).

And I found the exact same issue documented here!
https://medium.com/@jehy/hijacking-domain-using-github-pages-41c80ac57523

And like *jehy* I also wanted to report the issue, but realised it was on a Private Repo.  So being a good citizen:
1. I let Porkbun Support know all is well and that it was a Github Pages issue!
2. I logged a Feature Request to Github to see if they could make Verifying Custom Domains mandatory (and if they could blacklist the hackers as well!)

With that all logged, I filled in my journal and surprisingly wrote:

"Got hacked!  Learnt Heaps"

40 minutes past midnight!  Time to sleep!

## Reflections!
Back to the present, I'm really am seeing the joy of being hacked!  (especially with timing!) so thanks for the tutorial!


---

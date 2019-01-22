---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04971DeepSpecsummerschool.html
---

## [general](index.html)
### [DeepSpec summer school](04971DeepSpecsummerschool.html)

#### [Simon Hudon (Mar 11 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577208):
The registrations are open for the DeepSpec summer school 2018: https://deepspec.org/event/dsss18/

Does anybody else intend to attend?

#### [Andrew Ashworth (Mar 11 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577499):
it looks interesting, but it seems participation is by invitation only, sadly

#### [Andrew Ashworth (Mar 11 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577539):
hopefully they will record lectures and post them online this year

#### [Simon Hudon (Mar 11 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577660):
But you can apply!

#### [Moses Schönfinkel (Mar 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577712):
Whoa... both Pierce and Chlipala, that's quite the "cast" they have :).

#### [Andrew Ashworth (Mar 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123577713):
I am not a researcher in software certification though. It is unlikely they would accept me. I don't think interested amateurs get grant money :)

#### [Simon Hudon (Mar 11 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123578698):
Is any of it relevant to your work? If the technology was mature enough, do you think you could make use of it?

#### [Andrew Ashworth (Mar 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579596):
as a programmer, when is software certification not relevant?

#### [Andrew Ashworth (Mar 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579660):
but yes, i first got interested in software certification when I was looking for help in automatically calculating  error bounds on numerical algorithms, and then promptly realized it is super hard to work with floating point numbers

#### [Andrew Ashworth (Mar 11 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579701):
not to mention the theory is supremely tedious, i don't think anybody uses interval arithmetic in practice

#### [Simon Hudon (Mar 11 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579752):
I agree :) Let's put my question differently: how hostile is your industry towards verification? I have come to see that most employers look at verification with a lot of suspicion

#### [Andrew Ashworth (Mar 11 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579761):
pretty hostile, because proving things takes up many hours of expensive engineer time

#### [Andrew Ashworth (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579806):
it's far cheaper to sprinkle a few asserts here and there and do testing after the fact

#### [Andrew Ashworth (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579809):
i don't work in a safety-critical industry

#### [Simon Hudon (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579810):
Sometimes, that argument sounds like "using a computer is too expensive because writing our own OS and our own compiler takes way too much time"

#### [Simon Hudon (Mar 11 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579854):
But you have a point there: it's great when you can find a compromise like that. When the technology is mature, it's no longer a cost to use it. It really pushes you forward. I'm trying to sell Haskell that way.

#### [Andrew Ashworth (Mar 11 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579911):
I wake up every day and offer a small prayer of thanks to the various research funding bodies out there that allow people to spend time thinking about these things :)

#### [Andrew Ashworth (Mar 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579972):
but i think it's telling verification has only taken off in the hardware industry where making a mistake costs millions of dollars

#### [Simon Hudon (Mar 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579974):
I also have the same prayer :) it funds a great hobby of mine

#### [Simon Hudon (Mar 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579980):
What do you conclude from that fact?

#### [Andrew Ashworth (Mar 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123579982):
a lot more work needs to go into automated theorem proving

#### [Andrew Ashworth (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580034):
also some mathematician somewhere needs to invent something more practical than interval arithmetic

#### [Andrew Ashworth (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580035):
these are both things I am wildly incapable of doing with my current skillset :)

#### [Moses Schönfinkel (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580036):
Careful about putting mathematician and practical in the same sentence! :)

#### [Kevin Buzzard (Mar 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580714):
What's interval arithmetic?

#### [Kevin Buzzard (Mar 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580753):
I don't think I've ever done anything practical.

#### [Simon Hudon (Mar 11 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580850):
Is it legal for mathematicians to do practical stuff? :stuck_out_tongue_closed_eyes:

#### [Simon Hudon (Mar 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580856):
Interval arithmetic is when you represent numbers as an upper bound and a lower bound on uncertainty and you do arithmetic on those bounds. When you need to round, you round down the lower bound and you round up the upper bound. That allows you to keep tack on the accumulated errors

#### [Moses Schönfinkel (Mar 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580898):
I think some take offense if you accuse them of doing something with practical applications.

#### [Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580907):
I don't take offense, I don't see what you mean.

#### [Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580908):
But I'm not a native English speaker

#### [Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580909):
Could you define "practical applications"?

#### [Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580910):
Never heard about this

#### [Moses Schönfinkel (Mar 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580955):
It's when your work is sub-par and not abstract enough.

#### [Moses Schönfinkel (Mar 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123580957):
That's when some call it "practical".

#### [Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581003):
I found it. I knew I already met this "applied" word.

#### [Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581004):
It was in https://indico.math.cnrs.fr/event/1865/

#### [Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581006):
" On the foundational side, this concerns basics on the etale cohomology of diamonds including smooth and proper base change and Poincare duality, leading up to a good notion of "constructible" sheaves on the stack of G-bundles on the Fargues-Fontaine curve. On the applied side, this concerns the construction of (semisimple) L-parameters, the conjecture of Harris (as modified by Viehmann) on the cohomology of non-basic Rapoport-Zink spaces, and the conjecture of Kottwitz on the cohomology of basic Rapoport-Zink spaces."

#### [Simon Hudon (Mar 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581146):
Too down-to-earth for me

#### [Simon Hudon (Mar 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581151):
But what does it say about theorem prover developers that their practical application is helping mathematicians draw pies in the sky?

#### [Patrick Massot (Mar 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581153):
Yeah, me too. That's why I'm not doing this arithmetic geometry stuff.

#### [Patrick Massot (Mar 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581198):
I've been explained that theorem provers helping mathematician is an unwanted accident

#### [Simon Hudon (Mar 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581199):
Haha!

#### [Simon Hudon (Mar 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581208):
Formal methods have a really fun position where they get contempt from both practitioners and academics

#### [Patrick Massot (Mar 11 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581300):
I don't have any contempt here

#### [Patrick Massot (Mar 11 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581315):
(I don't even know how to build an English sentence using that word, my attempt sounds weird)

#### [Patrick Massot (Mar 11 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581395):
And, in case it's not clear: the story behind the quote with "foundational side/applied side" is that this talk announcement by the most fashionable  abstract mathematician  made mathematician laugh out loud everywhere it was seen, because the application mentioned is totally inside the world of abstract useless math

#### [Simon Hudon (Mar 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123581950):
I don't see contempt here. It's just that I've been trying to promote the use of formal proofs for a while and I was expecting computer scientists to be excited to get rid of bugs and mathematicians to be excited to gain insight into their subject by the mere shape of their formulas but I've mostly been responded to by computer scientists like I was trying to build a perpetual motion system (unrealistic because of deep truths of the universe that they understand and that I don't) and by mathematician like I was building a huge steam powered machine to tie your shoes (overly grandiose and heavy handed approach to solve an easy problem)

#### [Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582000):
It's certainly true that the vast majority of mathematicians are not yet convinced that proof assistants can be of any use to them

#### [Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582001):
And it's true with the current state of proof assistants

#### [Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582002):
but I hope this is changing

#### [Patrick Massot (Mar 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582008):
They only need to wait for Lean 4

#### [Simon Hudon (Mar 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582190):
I think this is a revolution happening slowly. Lean 4 will help of course but with Lean 2 and 3, preparation has been done. Even before that, with Coq and Isabelle, impressive projects have done. And as time passes, the required degree of expertise goes down. You no longer need to be Bertrand Russel to do a completely formal proof. You can even do it without a PhD these days

#### [Simon Hudon (Mar 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582200):
I keep hearing that the goals are impossible but milestones keep being reached regardless.

#### [Patrick Massot (Mar 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582243):
I'm not sure what is the next currently planned milestone on the math side of proof assistants

#### [Patrick Massot (Mar 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582245):
As far as I know, the previous one was the odd order theorem proof

#### [Simon Hudon (Mar 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582291):
I'm curious about the next one too. It might about formalizing subjects rather than individual proofs next. I'm more familiar with the ones in computer science

#### [Patrick Massot (Mar 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582736):
Since we already completely spoiled this thread. Let me ask an almost irrelevant question. I clearly don't care about this DeepSpec summer school. But what about that Oxford conference? Do you think it would useful to go there? How many people around here will go there?

#### [Simon Hudon (Mar 11 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582796):
Can you share a link?

#### [Simon Hudon (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582803):
(we could rename this thread to conferences and meetups)

#### [Patrick Massot (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582805):
https://itp2018.inria.fr/

#### [Patrick Massot (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582806):
Looking at the program of previous years doesn't really help

#### [Patrick Massot (Mar 11 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582855):
because 2016 talks seem to be very different from 2017

#### [Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582861):
That is a ridiculously large committee.

#### [Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582863):
Is it really such a gigantic area that they need a committee that big?

#### [Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582865):
Or do most people just do nothing?

#### [Patrick Massot (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582870):
To me it looks like the 2016 program would have been interesting to me but 2017 was too much CS

#### [Patrick Massot (Mar 11 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582916):
Of course it would also be fun if this could the opportunity to actually meet people from this forum

#### [Patrick Massot (Mar 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582923):
The committee is gigantic indeed

#### [Patrick Massot (Mar 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123582926):
I've never heard of a conference with more organizers than speakers

#### [Simon Hudon (Mar 11 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583039):
That sounds like a really cool place to go. I wish I had a paper to present

#### [Kevin Buzzard (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583096):
It seems to me that this CS world is just the same people organising conference after conference

#### [Kevin Buzzard (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583099):
It seems very different to the maths world

#### [Andrew Ashworth (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583102):
```quote
That sounds like a really cool place to go. I wish I had a paper to present
```
```quote
In addition to regular papers, described above, there will be a section for shorter papers, which can be used to describe interesting work that is still ongoing and not fully mature. Such a preliminary report is limited to 6 pages and may consist of an extended abstract. Each of these papers should bear the phrase “(short paper)” beneath the title, and will be refereed and be expected to present innovative and promising ideas, possibly in early form. Accepted submissions in this category will be published in the main proceedings and will be presented as short talks.
```

#### [Kevin Buzzard (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583105):
Presumably you can go without presenting a paper?

#### [Kevin Buzzard (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583144):
Then you get the best of both worlds

#### [Patrick Massot (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583152):
It's easier when you go from London to Oxford than from Canada to Oxford

#### [Mario Carneiro (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583325):
I'm aiming for ITP 2018, if all goes well I will be in Oxford this summer

#### [Mario Carneiro (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583334):
(to present the Matiyasevich proof)

#### [Patrick Massot (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123583336):
nice

#### [Andrew Ashworth (Mar 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123586773):
what's more interesting to me is that they've rolled up 9 conferences into one. just how many people attend these things in person?

#### [Gabriel Ebner (Mar 12 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123597650):
I will (most likely) be in Oxford as well, though I haven't sent anything to ITP.

#### [Kevin Buzzard (Mar 12 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123597793):
We tend to have specialised algebraic number theory conferences around once every 2 years, and there tend to be hundreds of us that go.

#### [Kevin Buzzard (Mar 12 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123597838):
Is it the sort of thing where you can just not bother registering and then show up on the day and meet people and chat to them and gatecrash a few talks (like pretty much every pure maths conference would be)?

#### [Kevin Buzzard (Mar 12 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123597847):
My partner goes to medical conference which cost $100s to register and you can't get past security without a badge

#### [Kevin Buzzard (Mar 12 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123597848):
I go to maths conferences and the worst that can happen if you don't register is that you have to pay for your own lunch

#### [Gabriel Ebner (Mar 12 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123598591):
In my experience, you need to register if you 1) present a paper, 2) want lunch, or 3) want a lanyard.  I haven't seen strict badge controls so far.

#### [Johannes Hölzl (Mar 12 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123599721):
ITP and CPP are the biggest theorem proving conferences. If you go through the proceedings of the last years you can find some interesting stuff. Also, in computer science, publishing at a conference usually counts as a regular publication. But this means the program committees are bigger,  as people need to review the papers upfront. And of course, you can go there without presenting a paper.

#### [Assia Mahboubi (Mar 14 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123698330):
@**Patrick Massot** , I wish I could be more positive but it would not be honest: I do not think that it would be reasonable in your case to go from  Canada to Oxford specifically for that event (I hope that Jeremy is not reading...). 
It will be very much a CS-style event with short talks meant to be teasers for the paper in the proceedings. As it is part this year of the Federated Logic Conference, it will take place in parallel with other even larger events, and people will possibly spend time rushing between the parallel sessions of a rather dense agenda... Usually, only a fraction of these talks are about formalized maths (as opposed for instance to program verification in general). But I have high expectations for Dan Grayson's invited talk. He will deliver a talk in memoriam of Vladimir Voevodsky but we hope that he will also speak about his own opinion about formalizing mathematics.

#### [Assia Mahboubi (Mar 14 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123698551):
```quote
Or do most people just do nothing?
```
@**Kevin Buzzard** Again, it is very much a CS-style event... These people are reviewing the papers submitted for the proceedings of the conference. In the case of this conference, they had 2 months to read an average of 6 submitted papers. Each of this paper is at most 15 pages and in the case of ITP, papers are usually accompanied with code. So I find it quite demanding to serve on such a committee.

#### [Patrick Massot (Mar 14 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123699161):
I'm not the one traveling from Canada, that was a comment about Kevin's answer to Simon (Simon is from Canada). I would be travelling from Paris.

#### [Patrick Massot (Mar 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123699164):
I'll probably wait for the talk abstracts, but it seems I shouldn't be too optimistic

#### [Patrick Massot (Mar 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec summer school/near/123699174):
And now I have to teach finite fields


---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04971DeepSpecsummerschool.html
---

## Stream: [general](index.html)
### Topic: [DeepSpec summer school](04971DeepSpecsummerschool.html)

---


{% raw %}
#### [ Simon Hudon (Mar 11 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577208):
<p>The registrations are open for the DeepSpec summer school 2018: <a href="https://deepspec.org/event/dsss18/" target="_blank" title="https://deepspec.org/event/dsss18/">https://deepspec.org/event/dsss18/</a></p>
<p>Does anybody else intend to attend?</p>

#### [ Andrew Ashworth (Mar 11 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577499):
<p>it looks interesting, but it seems participation is by invitation only, sadly</p>

#### [ Andrew Ashworth (Mar 11 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577539):
<p>hopefully they will record lectures and post them online this year</p>

#### [ Simon Hudon (Mar 11 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577660):
<p>But you can apply!</p>

#### [ Moses Schönfinkel (Mar 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577712):
<p>Whoa... both Pierce and Chlipala, that's quite the "cast" they have :).</p>

#### [ Andrew Ashworth (Mar 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123577713):
<p>I am not a researcher in software certification though. It is unlikely they would accept me. I don't think interested amateurs get grant money :)</p>

#### [ Simon Hudon (Mar 11 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123578698):
<p>Is any of it relevant to your work? If the technology was mature enough, do you think you could make use of it?</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579596):
<p>as a programmer, when is software certification not relevant?</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579660):
<p>but yes, i first got interested in software certification when I was looking for help in automatically calculating  error bounds on numerical algorithms, and then promptly realized it is super hard to work with floating point numbers</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579701):
<p>not to mention the theory is supremely tedious, i don't think anybody uses interval arithmetic in practice</p>

#### [ Simon Hudon (Mar 11 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579752):
<p>I agree :) Let's put my question differently: how hostile is your industry towards verification? I have come to see that most employers look at verification with a lot of suspicion</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579761):
<p>pretty hostile, because proving things takes up many hours of expensive engineer time</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579806):
<p>it's far cheaper to sprinkle a few asserts here and there and do testing after the fact</p>

#### [ Andrew Ashworth (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579809):
<p>i don't work in a safety-critical industry</p>

#### [ Simon Hudon (Mar 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579810):
<p>Sometimes, that argument sounds like "using a computer is too expensive because writing our own OS and our own compiler takes way too much time"</p>

#### [ Simon Hudon (Mar 11 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579854):
<p>But you have a point there: it's great when you can find a compromise like that. When the technology is mature, it's no longer a cost to use it. It really pushes you forward. I'm trying to sell Haskell that way.</p>

#### [ Andrew Ashworth (Mar 11 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579911):
<p>I wake up every day and offer a small prayer of thanks to the various research funding bodies out there that allow people to spend time thinking about these things :)</p>

#### [ Andrew Ashworth (Mar 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579972):
<p>but i think it's telling verification has only taken off in the hardware industry where making a mistake costs millions of dollars</p>

#### [ Simon Hudon (Mar 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579974):
<p>I also have the same prayer :) it funds a great hobby of mine</p>

#### [ Simon Hudon (Mar 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579980):
<p>What do you conclude from that fact?</p>

#### [ Andrew Ashworth (Mar 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123579982):
<p>a lot more work needs to go into automated theorem proving</p>

#### [ Andrew Ashworth (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580034):
<p>also some mathematician somewhere needs to invent something more practical than interval arithmetic</p>

#### [ Andrew Ashworth (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580035):
<p>these are both things I am wildly incapable of doing with my current skillset :)</p>

#### [ Moses Schönfinkel (Mar 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580036):
<p>Careful about putting mathematician and practical in the same sentence! :)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580714):
<p>What's interval arithmetic?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580753):
<p>I don't think I've ever done anything practical.</p>

#### [ Simon Hudon (Mar 11 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580850):
<p>Is it legal for mathematicians to do practical stuff? <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Simon Hudon (Mar 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580856):
<p>Interval arithmetic is when you represent numbers as an upper bound and a lower bound on uncertainty and you do arithmetic on those bounds. When you need to round, you round down the lower bound and you round up the upper bound. That allows you to keep tack on the accumulated errors</p>

#### [ Moses Schönfinkel (Mar 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580898):
<p>I think some take offense if you accuse them of doing something with practical applications.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580907):
<p>I don't take offense, I don't see what you mean.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580908):
<p>But I'm not a native English speaker</p>

#### [ Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580909):
<p>Could you define "practical applications"?</p>

#### [ Patrick Massot (Mar 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580910):
<p>Never heard about this</p>

#### [ Moses Schönfinkel (Mar 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580955):
<p>It's when your work is sub-par and not abstract enough.</p>

#### [ Moses Schönfinkel (Mar 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123580957):
<p>That's when some call it "practical".</p>

#### [ Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581003):
<p>I found it. I knew I already met this "applied" word.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581004):
<p>It was in <a href="https://indico.math.cnrs.fr/event/1865/" target="_blank" title="https://indico.math.cnrs.fr/event/1865/">https://indico.math.cnrs.fr/event/1865/</a></p>

#### [ Patrick Massot (Mar 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581006):
<p>" On the foundational side, this concerns basics on the etale cohomology of diamonds including smooth and proper base change and Poincare duality, leading up to a good notion of "constructible" sheaves on the stack of G-bundles on the Fargues-Fontaine curve. On the applied side, this concerns the construction of (semisimple) L-parameters, the conjecture of Harris (as modified by Viehmann) on the cohomology of non-basic Rapoport-Zink spaces, and the conjecture of Kottwitz on the cohomology of basic Rapoport-Zink spaces."</p>

#### [ Simon Hudon (Mar 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581146):
<p>Too down-to-earth for me</p>

#### [ Simon Hudon (Mar 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581151):
<p>But what does it say about theorem prover developers that their practical application is helping mathematicians draw pies in the sky?</p>

#### [ Patrick Massot (Mar 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581153):
<p>Yeah, me too. That's why I'm not doing this arithmetic geometry stuff.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581198):
<p>I've been explained that theorem provers helping mathematician is an unwanted accident</p>

#### [ Simon Hudon (Mar 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581199):
<p>Haha!</p>

#### [ Simon Hudon (Mar 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581208):
<p>Formal methods have a really fun position where they get contempt from both practitioners and academics</p>

#### [ Patrick Massot (Mar 11 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581300):
<p>I don't have any contempt here</p>

#### [ Patrick Massot (Mar 11 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581315):
<p>(I don't even know how to build an English sentence using that word, my attempt sounds weird)</p>

#### [ Patrick Massot (Mar 11 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581395):
<p>And, in case it's not clear: the story behind the quote with "foundational side/applied side" is that this talk announcement by the most fashionable  abstract mathematician  made mathematician laugh out loud everywhere it was seen, because the application mentioned is totally inside the world of abstract useless math</p>

#### [ Simon Hudon (Mar 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123581950):
<p>I don't see contempt here. It's just that I've been trying to promote the use of formal proofs for a while and I was expecting computer scientists to be excited to get rid of bugs and mathematicians to be excited to gain insight into their subject by the mere shape of their formulas but I've mostly been responded to by computer scientists like I was trying to build a perpetual motion system (unrealistic because of deep truths of the universe that they understand and that I don't) and by mathematician like I was building a huge steam powered machine to tie your shoes (overly grandiose and heavy handed approach to solve an easy problem)</p>

#### [ Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582000):
<p>It's certainly true that the vast majority of mathematicians are not yet convinced that proof assistants can be of any use to them</p>

#### [ Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582001):
<p>And it's true with the current state of proof assistants</p>

#### [ Patrick Massot (Mar 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582002):
<p>but I hope this is changing</p>

#### [ Patrick Massot (Mar 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582008):
<p>They only need to wait for Lean 4</p>

#### [ Simon Hudon (Mar 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582190):
<p>I think this is a revolution happening slowly. Lean 4 will help of course but with Lean 2 and 3, preparation has been done. Even before that, with Coq and Isabelle, impressive projects have done. And as time passes, the required degree of expertise goes down. You no longer need to be Bertrand Russel to do a completely formal proof. You can even do it without a PhD these days</p>

#### [ Simon Hudon (Mar 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582200):
<p>I keep hearing that the goals are impossible but milestones keep being reached regardless.</p>

#### [ Patrick Massot (Mar 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582243):
<p>I'm not sure what is the next currently planned milestone on the math side of proof assistants</p>

#### [ Patrick Massot (Mar 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582245):
<p>As far as I know, the previous one was the odd order theorem proof</p>

#### [ Simon Hudon (Mar 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582291):
<p>I'm curious about the next one too. It might about formalizing subjects rather than individual proofs next. I'm more familiar with the ones in computer science</p>

#### [ Patrick Massot (Mar 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582736):
<p>Since we already completely spoiled this thread. Let me ask an almost irrelevant question. I clearly don't care about this DeepSpec summer school. But what about that Oxford conference? Do you think it would useful to go there? How many people around here will go there?</p>

#### [ Simon Hudon (Mar 11 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582796):
<p>Can you share a link?</p>

#### [ Simon Hudon (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582803):
<p>(we could rename this thread to conferences and meetups)</p>

#### [ Patrick Massot (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582805):
<p><a href="https://itp2018.inria.fr/" target="_blank" title="https://itp2018.inria.fr/">https://itp2018.inria.fr/</a></p>

#### [ Patrick Massot (Mar 11 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582806):
<p>Looking at the program of previous years doesn't really help</p>

#### [ Patrick Massot (Mar 11 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582855):
<p>because 2016 talks seem to be very different from 2017</p>

#### [ Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582861):
<p>That is a ridiculously large committee.</p>

#### [ Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582863):
<p>Is it really such a gigantic area that they need a committee that big?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582865):
<p>Or do most people just do nothing?</p>

#### [ Patrick Massot (Mar 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582870):
<p>To me it looks like the 2016 program would have been interesting to me but 2017 was too much CS</p>

#### [ Patrick Massot (Mar 11 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582916):
<p>Of course it would also be fun if this could the opportunity to actually meet people from this forum</p>

#### [ Patrick Massot (Mar 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582923):
<p>The committee is gigantic indeed</p>

#### [ Patrick Massot (Mar 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123582926):
<p>I've never heard of a conference with more organizers than speakers</p>

#### [ Simon Hudon (Mar 11 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583039):
<p>That sounds like a really cool place to go. I wish I had a paper to present</p>

#### [ Kevin Buzzard (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583096):
<p>It seems to me that this CS world is just the same people organising conference after conference</p>

#### [ Kevin Buzzard (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583099):
<p>It seems very different to the maths world</p>

#### [ Andrew Ashworth (Mar 11 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583102):
<blockquote>
<p>That sounds like a really cool place to go. I wish I had a paper to present</p>
<p>In addition to regular papers, described above, there will be a section for shorter papers, which can be used to describe interesting work that is still ongoing and not fully mature. Such a preliminary report is limited to 6 pages and may consist of an extended abstract. Each of these papers should bear the phrase “(short paper)” beneath the title, and will be refereed and be expected to present innovative and promising ideas, possibly in early form. Accepted submissions in this category will be published in the main proceedings and will be presented as short talks.</p>
</blockquote>

#### [ Kevin Buzzard (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583105):
<p>Presumably you can go without presenting a paper?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583144):
<p>Then you get the best of both worlds</p>

#### [ Patrick Massot (Mar 11 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583152):
<p>It's easier when you go from London to Oxford than from Canada to Oxford</p>

#### [ Mario Carneiro (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583325):
<p>I'm aiming for ITP 2018, if all goes well I will be in Oxford this summer</p>

#### [ Mario Carneiro (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583334):
<p>(to present the Matiyasevich proof)</p>

#### [ Patrick Massot (Mar 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123583336):
<p>nice</p>

#### [ Andrew Ashworth (Mar 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123586773):
<p>what's more interesting to me is that they've rolled up 9 conferences into one. just how many people attend these things in person?</p>

#### [ Gabriel Ebner (Mar 12 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123597650):
<p>I will (most likely) be in Oxford as well, though I haven't sent anything to ITP.</p>

#### [ Kevin Buzzard (Mar 12 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123597793):
<p>We tend to have specialised algebraic number theory conferences around once every 2 years, and there tend to be hundreds of us that go.</p>

#### [ Kevin Buzzard (Mar 12 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123597838):
<p>Is it the sort of thing where you can just not bother registering and then show up on the day and meet people and chat to them and gatecrash a few talks (like pretty much every pure maths conference would be)?</p>

#### [ Kevin Buzzard (Mar 12 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123597847):
<p>My partner goes to medical conference which cost $100s to register and you can't get past security without a badge</p>

#### [ Kevin Buzzard (Mar 12 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123597848):
<p>I go to maths conferences and the worst that can happen if you don't register is that you have to pay for your own lunch</p>

#### [ Gabriel Ebner (Mar 12 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123598591):
<p>In my experience, you need to register if you 1) present a paper, 2) want lunch, or 3) want a lanyard.  I haven't seen strict badge controls so far.</p>

#### [ Johannes Hölzl (Mar 12 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123599721):
<p>ITP and CPP are the biggest theorem proving conferences. If you go through the proceedings of the last years you can find some interesting stuff. Also, in computer science, publishing at a conference usually counts as a regular publication. But this means the program committees are bigger,  as people need to review the papers upfront. And of course, you can go there without presenting a paper.</p>

#### [ Assia Mahboubi (Mar 14 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123698330):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> , I wish I could be more positive but it would not be honest: I do not think that it would be reasonable in your case to go from  Canada to Oxford specifically for that event (I hope that Jeremy is not reading...). <br>
It will be very much a CS-style event with short talks meant to be teasers for the paper in the proceedings. As it is part this year of the Federated Logic Conference, it will take place in parallel with other even larger events, and people will possibly spend time rushing between the parallel sessions of a rather dense agenda... Usually, only a fraction of these talks are about formalized maths (as opposed for instance to program verification in general). But I have high expectations for Dan Grayson's invited talk. He will deliver a talk in memoriam of Vladimir Voevodsky but we hope that he will also speak about his own opinion about formalizing mathematics.</p>

#### [ Assia Mahboubi (Mar 14 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123698551):
<blockquote>
<p>Or do most people just do nothing?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Again, it is very much a CS-style event... These people are reviewing the papers submitted for the proceedings of the conference. In the case of this conference, they had 2 months to read an average of 6 submitted papers. Each of this paper is at most 15 pages and in the case of ITP, papers are usually accompanied with code. So I find it quite demanding to serve on such a committee.</p>

#### [ Patrick Massot (Mar 14 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123699161):
<p>I'm not the one traveling from Canada, that was a comment about Kevin's answer to Simon (Simon is from Canada). I would be travelling from Paris.</p>

#### [ Patrick Massot (Mar 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123699164):
<p>I'll probably wait for the talk abstracts, but it seems I shouldn't be too optimistic</p>

#### [ Patrick Massot (Mar 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/DeepSpec%20summer%20school/near/123699174):
<p>And now I have to teach finite fields</p>


{% endraw %}

---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05206Introductions.html
---

## Stream: [new members](index.html)
### Topic: [Introductions](05206Introductions.html)

---


{% raw %}
#### [ Xita Meyers (Sep 06 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439634):
<p>Hello, I have never asked a public question on Zulip before, and in order for me to get used to doing so, I have been ordered by <span class="user-mention" data-user-id="110064">@Kenny Lau</span>  to state the following in order to introduce myself: </p>
<p>"I am a proud student of Kevin Buzzard."</p>
<p>I look forward to learning much more about Lean through Zulip. </p>
<p>Thanks.</p>

#### [ Kenny Lau (Sep 06 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439648):
<p>Welcome!</p>

#### [ Xita Meyers (Sep 06 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439666):
<p>Thanks for welcoming me! This is my first time navigating Zulip, nice to meet you!</p>

#### [ Johan Commelin (Sep 06 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439730):
<p>Welcome Xita! Nice to meet you.</p>

#### [ Johan Commelin (Sep 06 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439735):
<p>What kind of stuff have you been looking at lately? Were you involved in UROP?</p>

#### [ Xita Meyers (Sep 06 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133439876):
<p>I've been involved in the UROP, but didn't learn very much by reading Theorem Proving in Lean; It was hard to understand to some extent. Currently I'm trying to prove a lemma in number theory that if p is a prime of form 4K + 3, then it cannot divide an integer of form x^2 + 1.</p>

#### [ Johan Commelin (Sep 06 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133440201):
<p>Ok, nice. Whenever you have questions, just ask! That's how we are all learning. (Most of us don't find the documentation sufficient, but we lack the time, energy, or courage to improve it.)</p>

#### [ Kenny Lau (Sep 06 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133440214):
<p>or motivation</p>

#### [ Kevin Buzzard (Sep 06 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133440757):
<p>Hey Su. Here would be a cheap way of doing this. If x^2=-1 mod p (p=4K+3) then x^{4K+2}=-1 mod p as well, contradicting Fermat's Little Theorem.</p>

#### [ Xita Meyers (Sep 06 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133450178):
<p>Yeah, that's how I've been trying to do it. It's taking longer than I expected.</p>

#### [ Harald Schilly (Sep 06 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133450780):
<p>Hi, I'm Harald, and I'm one of the devs behind CoCalc ... I've just worked on improving its syntax highlighter and well, I should also learn one or another detail about lean itself :-)</p>

#### [ Patrick Massot (Sep 06 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133451632):
<p>Welcome Harald!</p>

#### [ Kevin Buzzard (Sep 06 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133455563):
<p><span class="user-mention" data-user-id="128565">@Harald Schilly</span> here would be a good place to get information about where Lean is looking for files to import. At the minute I couldn't get mathlib imports working in CoCalc. This and the current inability to see the goal in tactic mode are in my mind the last two problems which need to be solved before lean is really usable. In particular, you guys are nearly there. I am hoping Gabriel Ebner gave you some hints about the latter goal, and the former goal can't be hard. I can't believe I'm saying this but actually just dumping the mathlib files into the lean core directory would probably work, although it's a horrible idea.</p>

#### [ Harald Schilly (Sep 06 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133457088):
<p>So, I know there is an env variable <code>LEAN_PATH</code> and we could set it to something. There is also a precompiled (but months old) mathlib in <code>/ext/lean/lean/mathlib/</code>. I bet it just depends on setting that lean path correctly to make it work. Should we discuss this in <a class="stream" data-stream-id="113488" href="/#narrow/stream/113488-general">#general</a> ?</p>

#### [ Johan Commelin (Sep 06 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133457128):
<p>Sure, I think we could move this discussion to the CoCalc thread.</p>

#### [ Johan Commelin (Sep 06 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133457191):
<p><a href="#narrow/stream/113488-general/topic/CoCalc" title="#narrow/stream/113488-general/topic/CoCalc">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc</a></p>

#### [ Mario Carneiro (Sep 06 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133457207):
<p><span class="user-mention" data-user-id="128565">@Harald Schilly</span> Don't use <code>LEAN_PATH</code>, it is deprecated since the <code>leanpkg</code> tool</p>

#### [ Kevin Buzzard (Sep 06 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133457458):
<p>There's something I don't understand about the set-up. At some point Lean will have to be told "look at <code>leanpkg.path</code>, that's where you should import stuff". How does that bit work? Aah, presumably this depends on the IDE. And because Harald is involved with writing a new IDE...maybe he needs to be told to look at <code>leanpkg.path</code>.</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133490898):
<p>Hey guys, just wanted to introduce myself as it seems to be a common habit here. Some of you may already have seen that I started to ask some smaller questions and also organize a theorem proving sozial at ETH.</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133490940):
<p>My background is mostly compilation, static analysis, loop transformations, often using Presburger arithmetic to get where I want to be.</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133490942):
<p>Since a year I look into theorem proving, and recently started to use lean.</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133490957):
<p>I work since maybe 10 years on LLVM and developed there the Polly loop optimizer</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491006):
<p>I am interested in using lean eventually for teaching and for some of my day-to-day work.</p>

#### [ Simon Hudon (Sep 07 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491016):
<p>Welcome to the Lean community! I hope it lives up to your expectations :)</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491062):
<p>Thanks. Until now everybody is very helpful. Looking forward to meet the first members in person next week.</p>

#### [ Simon Hudon (Sep 07 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491140):
<p>I wish I could attend. I'm no longer in Zurich but I'm sending a representative</p>

#### [ Simon Hudon (Sep 07 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491150):
<p>My friend Malte is a lecturer at ETH and I think he wants to attend</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491315):
<p>That's great.</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491317):
<p>Let me know when you are back in Zurich</p>

#### [ Simon Hudon (Sep 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133491337):
<p>I haven't been back in years but I think I'm due for a visit soon :)</p>

#### [ Corey Richardson (Sep 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/133555206):
<p>hi :) I'm coming back around to using Lean. previously I was an intern working on the seL4 verification, and a student doing research for cryptographic protocol analysis ATPs. good to see such a community has sprung up around lean!</p>

#### [ Ryan Smith (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134356472):
<p>Hi, I'm completely new to Lean. I come from an algebra and number theory background, and don't have much experience with formal logic beyond a course taken in undergrad a lot of years ago.</p>

#### [ Johan Commelin (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134356476):
<p>Cool, welcome! Where are you based?</p>

#### [ Johan Commelin (Sep 21 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134356480):
<p>I'm a postdoc in Freiburg, working in algebraic geometry.</p>

#### [ Tobias Grosser (Sep 21 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134358790):
<p>Welcome Ryan.</p>

#### [ Tobias Grosser (Sep 21 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134358793):
<p>Researcher at ETH Zurich here!</p>

#### [ Patrick Massot (Sep 21 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134361010):
<p>Hi Ryan! I'm a French mathematician working in Orsay. Would you care to tell us how you heard about Lean?</p>

#### [ Sebastian Graf (Sep 21 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134365477):
<p>Hi, I'm a PhD student in Karlsruhe with strong interest in functional programming. Although I'm mostly into GHC middle-end stuff, I really like type systems and would spend more time (well, if I had more time to spend) formalizing things, preferrably in Lean :)</p>

#### [ Johan Commelin (Sep 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134365877):
<p>Welcome! Karlsruhe is not too far from Freiburg (-; Have you seen <a href="#narrow/stream/113488-general/subject/LUG.20Freiburg.202018" title="#narrow/stream/113488-general/subject/LUG.20Freiburg.202018">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/LUG.20Freiburg.202018</a> ?</p>

#### [ Sebastian Graf (Sep 21 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134374044):
<p>Sounds interesting! I'm afraid I won't be able to make it due to the usual busy stuff during semester.</p>

#### [ Agnishom Chattopadhyay (Sep 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134380063):
<p>Hi;</p>
<p>I am Agnishom. I am an undergraduate student of Mathematics and Computer Science. I am interested in Logic in general.</p>
<p>Can somebody help me figure out how to install lean and configure emacs on my system?</p>

#### [ Alistair Tucker (Sep 21 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134380466):
<p>I suggest homebrew if you are on a mac</p>

#### [ Agnishom Chattopadhyay (Sep 21 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134380797):
<p>I am on linux mint</p>

#### [ Kevin Buzzard (Sep 21 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134392224):
<p><a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/</a></p>

#### [ Kevin Buzzard (Sep 21 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134392286):
<p>Does that help? Are there some instructions somewhere on github? I forget.</p>

#### [ Robert Kornacki (Sep 21 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134396506):
<p>Hi there, I've just started going through Theorem Proving In Lean and I've got to say I've really been enjoying using it. I come from a functional programming background, and when I tried out Idris earlier this year I really got a pull into the dependent type world. Lean has been a joy to use thus far in comparison to Idris for the very small reason that it's impeccably fast for displaying goals &amp; holes making the whole process feel really smooth rather than a little clunky (though I do enjoy Idris' ability to name holes). Out of curiosity, does anyone know of any performance comparisons of Lean vs Idris, would be neat to know.</p>

#### [ Andrew Ashworth (Sep 21 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134400827):
<p>Seeing as how Idris allows for code extraction to C, and is a language very much more focused on programming, I can't imagine the comparison being very favorable. When Lean 4 rolls around, that'll be a more interesting comparison since there will be easy interop with C++</p>

#### [ Reid Barton (Sep 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134403093):
<p>And ordinary lean programs will be compiled/JITted, as I understand it, rather than run in a VM like today</p>

#### [ Simon Winwood (Sep 25 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134559792):
<p>Hi All, I am a research engineer at Galois.  I am mainly used to Isabelle, and less-so Coq.  I am mainly interested in program verification, but also am keen on theorem proving in general.</p>

#### [ Simon Hudon (Sep 25 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134566178):
<p>Hi Simon! Welcome to Lean! I was an intern at Galois last year and that's actually where I first started using Lean. I got hooked.</p>

#### [ Simon Winwood (Sep 25 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134572150):
<p>Ah, I thought I recognised your name,</p>

#### [ David Michael Roberts (Sep 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134737991):
<p>Hello all. I've been following UF/HoTT/proof assistants as a lurker since the special year at the IAS. I'm in category theory/differential geometry/topos theory. I have some non-commutative algebra constructions (groupoid/category algebras) that I'd like to have a crack at formalising, as I warm up to learning about serious C*-algebra stuff (don't think I'd formalise that, but who knows...)</p>

#### [ Kevin Buzzard (Sep 27 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134739330):
<p>By far the best way to learn how to use the software is to just decide that you're going to try formalising X (rather than X and Y and Z and W) and then ask on the forum with a precise reference of what you're aiming at, and you'll get comments either of the form "this is done" or "this is feasible, start like this" or "this is way too hard, you'll first need to do X' so if you're still interested in then start there".</p>

#### [ David Michael Roberts (Sep 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134740913):
<p>OK, thanks. :-)</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134754218):
<p>...although probably reading Theorem Proving In Lean might help too. I was planning on writing docs for mathematicians over the summer, but my mathematicians didn't really seem to need docs, they asked each other questions (or me) and got stuck on things which wouldn't necessarily be covered in the docs I was planning on writing, so I didn't write them. I might have to write them next month when I have far more students than I can talk to individually.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134754259):
<p>I guess even if you don't plan on formalising something, you could still state more precisely what you might be interested in formalising and the community might offer comments.</p>

#### [ Scott Morrison (Sep 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134776123):
<p>Welcome, David! It's fun here. :-)</p>

#### [ David Michael Roberts (Sep 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778506):
<p>Well, given a small groupoid and a field, I want to construct the convolution algebra on the vector space with basis the arrows of that groupoid, and also construct the multiplier algebra of such a beast. I guess I would need:</p>
<p>fields<br>
vector spaces<br>
algebras<br>
small groupoids<br>
modules and their maps</p>
<p>I'll have to have a dig through mathlib to see what's there already, but I imagine a bunch of those (if not small groupoids) have been done.</p>

#### [ Mario Carneiro (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778666):
<p>We have all of those except algebras and groupoids, although we have categories so it's not hard to state what a groupoid is.</p>

#### [ Reid Barton (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778683):
<p>I have (small) groupoids in another project already which I could PR</p>

#### [ Reid Barton (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778701):
<p>It's the most basic possible thing, but should get you started</p>

#### [ Mario Carneiro (Sep 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778720):
<p>what is the convolution algebra?</p>

#### [ Mario Carneiro (Sep 28 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134778791):
<p>I guess the elements of the algebra are linear combinations of arrows of the groupoid, and multiplication involves the composition of arrows somehow?</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134808586):
<p>what is an <code>algebra</code> in this context? The word is used in so many ways. In commutative ring theory "A is a B-algebra" is simply a long-winded say of saying <code>f : B -&gt; A</code></p>

#### [ David Michael Roberts (Sep 28 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809225):
<p>Mario: Correct. Multiplication is the bilinear extension of f*g = f\circ g (if composable), 0 (if not)</p>

#### [ David Michael Roberts (Sep 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809282):
<p>Kevin:  a vector space with an associative bilinear multiplication—and I'm not going to assume unital.</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809370):
<p>Well making this definition is trivial, but Lean doesn't quite work like that; one also has to make a basic API for the definition, which means proving 20 trivial lemmas about it</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809379):
<p>and giving them names which computer scientists find acceptable</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809429):
<p>(something which I was initially skeptical about but now have very much come around to)</p>

#### [ Sean Leather (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809430):
<p><del>computer scientists</del> Mario and Johannes</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809443):
<p>Apologies for bad-mouthing the CS community in general :-)</p>

#### [ Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809452):
<p>Here a question that I don't know how to answer: are Lie algebras algebras?</p>

#### [ Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809460):
<p>Bourbaki says: yes</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809461):
<p>not in general I guess</p>

#### [ Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809465):
<p>But I think Lean will run into trouble with notation...</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809466):
<p>But it's completely consistent that Bourbaki have a different definition of algebra</p>

#### [ Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809544):
<p>I think if we want to use <code>has_mul</code> then the multiplication must be associative.</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809550):
<p>the word is used in so many ways. I think I once checked explicitly that the Lie bracket was not associative in general, even though there's a meta-proof of the form "if it were associative in general then someone would have pointed this out by now".</p>

#### [ Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809559):
<p>Otherwise brains will explode</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809563):
<p><code>has_mul</code> is just notation, it doesn't have to be associative by definition</p>

#### [ Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809568):
<p>associative Lie brackets are trivial, right? So you get abelian Lie algebras</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809613):
<p>Notation is a minefield and it's now my opinion that this is to a large extent the fault of mathematics.</p>

#### [ Johan Commelin (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809619):
<p>Sure, but non-associative <code>has_mul</code> might even create more problems then your <code>int</code> vs <code>nat</code> woes</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809628):
<p>We invented notation over the last few hundred years and some of it is awful. Quadratic Reciprocity is a statement about fractions in brackets.</p>

#### [ Johan Commelin (Sep 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809704):
<p>Somehow even Lean depends on notation. When I first understood that the simplifier relied on notation I was really disturbed.</p>

#### [ Johan Commelin (Sep 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809707):
<p>But notation seems to be more than just syntactic sugar</p>

#### [ Kevin Buzzard (Sep 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809815):
<p>Unfolding is an art, this is my understanding of it. If you unfold everything then you have a complete mess which you cannot work with. But <em>notation</em>? Doesn't that just get unfolded by the parser right at square 1 so <code>simp</code> can't even notice it is there?</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809871):
<p>there might be a terminological clash here - <code>has_mul</code> and such are often called "notation typeclasses" since they have a notation associated to them, but obviously <code>simp</code> knows about <code>has_mul</code>, even if it doesn't know that <code>*</code> is used to draw it</p>

#### [ Johan Commelin (Sep 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809884):
<p>Aaah, so we can drop the associativity condition</p>

#### [ Johan Commelin (Sep 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809890):
<p>And make <code>[X,Y]</code> notation for <code>Lie_algebra.mul X Y</code></p>

#### [ Johan Commelin (Sep 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134809940):
<p>It's really sad that we can't bind notation to namespaces...</p>

#### [ Johan Commelin (Sep 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810105):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you think this is a viable strategy? To have <code>algebra</code> and then <code>is_unital</code>, <code>is_assoc</code>, <code>is_comm</code>, etc...</p>

#### [ Johan Commelin (Sep 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810107):
<p>Where <code>algebra</code> just means bilinear multiplication on a module.</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810151):
<p>ironically, there is already <code>is_comm</code>, <code>is_assoc</code> etc in <code>@[algebra]</code></p>

#### [ Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810156):
<p>but I think that means something different</p>

#### [ Johan Commelin (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810158):
<p>What do they mean?</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810160):
<p>it is not bound to a notation</p>

#### [ Johan Commelin (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810162):
<p>Ok, but we could have <code>has_mul.is_assoc</code> etc, right?</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810169):
<p>what's the use case?</p>

#### [ Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810175):
<p>Well, there are entire fields of mathematics that work with associative algebras</p>

#### [ Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810181):
<p>But there are also entire books about non-associative algebras</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810182):
<p>but you don't want to use <code>*</code> for them, right?</p>

#### [ Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810191):
<p>Sometimes the associative algebras are unital, and/or commutative</p>

#### [ Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810194):
<p>Why not use <code>*</code>?</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810195):
<p>that's whatever</p>

#### [ Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810239):
<p>My proposal is to use <code>has_mul</code> for all of them</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810240):
<p>If you want to use <code>*</code>, go ahead and define your typeclass based on <code>has_mul</code></p>

#### [ Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810250):
<p>And then only for Lie algebras introduce a second notation, namely <code>[X,Y]</code> instead of <code>X * Y</code></p>

#### [ Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810251):
<p>the danger is if you need a conventional mul and also a lie bracket thing at the same time</p>

#### [ Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810256):
<p>I have never heard of that before</p>

#### [ Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810260):
<p>Ah, I do</p>

#### [ Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810263):
<p>Hmmm... that's nasty</p>

#### [ Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810271):
<p>Every ring gives a Lie algebra, via the commutator bracket</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810278):
<p>yeah you probably don't want to confuse those</p>

#### [ Johan Commelin (Sep 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810340):
<p>Hmmm... so we have <code>algebra</code> without notation. Just the <code>op</code>. And then <code>assoc_algebra</code> gets <code>has_mul</code>, and <code>Lie_algebra</code> gets <code>has_bracket</code>. Could that work?</p>

#### [ Johan Commelin (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810358):
<p>Hmm... but then there would still be two instances of <code>algebra</code> on every <code>ring</code>.</p>

#### [ Johan Commelin (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810363):
<p>And they aren't even equal.</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810370):
<p>What about a translation wrapper like <code>multiplicative</code>?</p>

#### [ Johan Commelin (Sep 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810414):
<p>What would that do?</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810431):
<p>change the notation</p>

#### [ Mario Carneiro (Sep 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810447):
<p>so you could develop the theory on <code>has_mul</code>, and then transfer any results to the <code>has_bracket</code> version</p>

#### [ Johan Commelin (Sep 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134810512):
<p>Ok, but then, suppose we have <code>[ring R]</code>, this would give <code>[algebra R]</code>. And then? Something like <code>[Lie_algebra (commutator R)]</code>?</p>

#### [ Chris Hughes (Sep 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134811201):
<p>Isn't semigroup has_mul.assoc?</p>

#### [ Kevin Buzzard (Sep 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134811280):
<p>Yeah but the Lie algebra associated to a ring is a second "multiplication", defined as <code>[a,b] = a*b-b*a</code>. This is not associative.</p>

#### [ Kevin Buzzard (Sep 28 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134811302):
<p>It's not even a multiplication really, this conversation was started by the observation that Bourbaki apparently claims that Lie algebras are "algebras", whatever that word means.</p>

#### [ Mario Carneiro (Sep 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134812486):
<p>I think this is the wrong thread</p>

#### [ Ryan Smith (Oct 01 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Introductions/near/134948015):
<p>Sorry for the slow response, went on vacation right after learning about Lean :). I read about the verification of Feit-Thompson and I was really impressed that compute checked proofs have come so far that such a thing was possible. That lead to doing a survey of proof checkers, and it seemed that Lean was a much more dynamic community than Coq and some of the others. If I needed any more proof that Lean is legit, seeing Kevin Buzzard here is a pretty strong endorsement.</p>
<p>I actually left academia a couple years ago for industry, and I've been thinking about find project that would allow me to be more involved with math and work on something that would useful to the community.</p>


{% endraw %}

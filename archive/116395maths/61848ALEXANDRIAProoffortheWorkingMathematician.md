---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61848ALEXANDRIAProoffortheWorkingMathematician.html
---

## Stream: [maths](index.html)
### Topic: [ALEXANDRIA: Proof for the Working Mathematician](61848ALEXANDRIAProoffortheWorkingMathematician.html)

---


{% raw %}
#### [ Sean Leather (May 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588456):
<p><strong><a href="https://www.cl.cam.ac.uk/~lp15/Grants/Alexandria/" target="_blank" title="https://www.cl.cam.ac.uk/~lp15/Grants/Alexandria/">ALEXANDRIA: Large-Scale Formal Proof for the Working Mathematician</a></strong></p>
<p><em>L. C. Paulson, Computer Laboratory, University of Cambridge</em></p>
<blockquote>
<p>Mathematical proofs have always been prone to error. Today, proofs can be hundreds of pages long and combine results from many specialisms, making them almost impossible to check. One solution is to deploy modern verification technology. Interactive theorem provers have demonstrated their potential as vehicles for formalising mathematics through achievements such as the verification of the Kepler Conjecture. Proofs done using such tools reach a high standard of correctness.</p>
<p>However, existing theorem provers are unsuitable for mathematics. Their formal proofs are unreadable. They struggle to do simple tasks, such as evaluating limits. They lack much basic mathematics, and the material they do have is difficult to locate and apply.</p>
<p>ALEXANDRIA will create a proof development environment attractive to working mathematicians, utilising the best technology available across computer science. Its focus will be the management and use of large-scale mathematical knowledge, both theorems and algorithms. The project will employ mathematicians to investigate the formalisation of mathematics in practice. Our already substantial formalised libraries will serve as the starting point. They will be extended and annotated to support sophisticated searches. Techniques will be borrowed from machine learning, information retrieval and natural language processing. Algorithms will be treated similarly: ALEXANDRIA will help users find and invoke the proof methods and algorithms appropriate for the task.</p>
<p>ALEXANDRIA will provide (1) comprehensive formal mathematical libraries; (2) search within libraries, and the mining of libraries for proof patterns; (3) automated support for the construction of large formal proofs; (4) sound and practical computer algebra tools.</p>
<p>ALEXANDRIA will be based on legible structured proofs. Formal proofs should be not mere code, but a machine-checkable form of communication between mathematicians.</p>
<p>The project will run for 60 months starting 1 September 2017.</p>
</blockquote>

#### [ Johan Commelin (May 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588533):
<p>Wow, those are big claims (-;</p>

#### [ Kevin Buzzard (May 15 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588843):
<p>Yeah exactly. So I emailed him saying "you're just up the road from me, how come you're not reaching out to mathematicians like me so we can talk about this sort of stuff?" and he said "yeah I'm just sitting in my office like usual really" so I said "OK so you can reach out to me by me coming to visit on Tuesday and you telling me what it's all about" and he said "OK"</p>

#### [ Kevin Buzzard (May 15 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588848):
<p>I mean, I guess he didn't say _exactly_ that...</p>

#### [ Kevin Buzzard (May 15 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588856):
<p>but he did remark that someone called Peter Koepke would also be there on Tuesday giving a talk...</p>

#### [ Gabriel Ebner (May 15 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588906):
<p>At the risk of sounding maybe a bit unimpressed, but I think that this proposal is not overly ambitious.  It's basically a continuation of current work in Isabelle.  The goals are pretty much 1) formalize some undergrad math, 2) improve the search function a bit, 3) add more refactoring tools, and 4) integrate and polish some computer algebra tactics.</p>

#### [ Kevin Buzzard (May 15 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588909):
<blockquote>
<p>Wow, those are big claims (-;</p>
</blockquote>
<p>It's also big money, right? Multi-million pound ERC grant. One of the last the UK will ever get, due to Brexit.</p>

#### [ Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588921):
<p>Such a shame to do this in Isabelle</p>

#### [ Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588922):
<p>He should have come here</p>

#### [ Kevin Buzzard (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588923):
<p>Thanks for this Gabriel. In mathematics it seems to be extremely difficult to get these big ERC grants, in the sense that the people I know who have got them recently have put in some very high-powered proposals.</p>

#### [ Kevin Buzzard (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588925):
<p>My impression is that he is really into the idea of formal proofs being readable.</p>

#### [ Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588927):
<p>As far as I can see there is no obstruction to having readable proofs in Lean</p>

#### [ Kevin Buzzard (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588964):
<p>I mean, human-readable source code</p>

#### [ Patrick Massot (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588970):
<p>It's only Mario and Johannes don't like them</p>

#### [ Patrick Massot (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588975):
<p>The sledgehammer thing is much more serious issue of course</p>

#### [ Kevin Buzzard (May 15 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588990):
<p>I sometimes write "low-level" proofs, and I find them very enjoyable (my instincts just tell me to press on instead of trying tactics), but I do feel at the end of it all that they are no more readable than any other Lean code, they are just intro, apply, intro, refine, intro, exact, cases, cases, rwa, done</p>

#### [ Kevin Buzzard (May 15 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588991):
<p><code>intros a Ha</code></p>

#### [ Kevin Buzzard (May 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588992):
<p>Maybe I should be writing <code>intros a proof_that_a_is_in_X</code></p>

#### [ Patrick Massot (May 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589037):
<p>I often try to do that</p>

#### [ Kevin Buzzard (May 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589093):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/d2f64a23d8e6347bde488de0b0a93be1b72f18d6/src/tag00E8.lean#L145" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/d2f64a23d8e6347bde488de0b0a93be1b72f18d6/src/tag00E8.lean#L145">https://github.com/kbuzzard/lean-stacks-project/blob/d2f64a23d8e6347bde488de0b0a93be1b72f18d6/src/tag00E8.lean#L145</a></p>

#### [ Kevin Buzzard (May 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589099):
<p>"I follow my nose, cases, rw, apply, cases, exact, intro, split, cases, apply, exact"</p>

#### [ Kevin Buzzard (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589106):
<p>and voila, Spec(R) is compact</p>

#### [ Patrick Massot (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589115):
<p>I don't think it would be hard to make it easier to read</p>

#### [ Patrick Massot (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589118):
<p>You already have a couple of explicit <code>have</code></p>

#### [ Kevin Buzzard (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589121):
<p>I agree</p>

#### [ Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589159):
<p>it was certainly easy to write :-)</p>

#### [ Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589162):
<p>but my point is that I didn't</p>

#### [ Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589163):
<p>make it easy to read</p>

#### [ Patrick Massot (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589164):
<p>You could add a few more, maybe with some <code>suffices</code></p>

#### [ Patrick Massot (May 15 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589241):
<p>Why "quasi-compact" if you prove compactness?</p>

#### [ Kevin Buzzard (May 15 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589308):
<p>I thought that this was the French's fault?</p>

#### [ Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589354):
<p>In the UK, compact := every cover has a finite subcover. In France it's Hausdorff + ...</p>

#### [ Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589357):
<p>but alg geom is a French subject</p>

#### [ Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589365):
<p>because schemes are typically not Hausdorff, it's quasi-compact</p>

#### [ Kevin Buzzard (May 15 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589425):
<p>PS <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> when writing grant proposals, you write what you think will get funded (so you get a promotion or pay rise when you get the grant), and then you just keep on doing what you were doing beforehand anyway (at least that's what happens in maths).</p>

#### [ Kevin Buzzard (May 15 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589440):
<p>One might also ask why computer scientists have been sitting on things like Coq / Isabelle for decades, and these are perfectly capable of formalising all of undergraduate pure mathematics, but nobody has done it yet.</p>

#### [ Patrick Massot (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589585):
<p>Oh, I understand: you mean mathlib's definition of compactness is the broken one (without Haussdorff)?</p>

#### [ Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589588):
<p>right</p>

#### [ Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589589):
<p>it's only broken because of your cultural upbringing</p>

#### [ Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589591):
<p>One could instead regard it as a translation issue</p>

#### [ Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589594):
<p>English "compact" := French quasi-compact</p>

#### [ Kevin Buzzard (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589639):
<p>Like UK N := France N^0 or N^* or whatever you call the thing without a zero.</p>

#### [ Patrick Massot (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589643):
<p>Anyway, I don't understand how proving quasi-compactness can be anything but trivial in algebraic geometry: any open set covers almost everything!</p>

#### [ Kevin Buzzard (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589646):
<p>well I did point out that my proof was just 50 lines of intro, apply, exact ;-)</p>

#### [ Patrick Massot (May 15 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589804):
<p>To be honest I have no idea where this difference comes from. All spaces I work with are obviously Haussdorff, so I never say or write quasi-compact</p>

#### [ Johan Commelin (May 15 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126590092):
<p>But then, you forget saying Haussdorff half the time!</p>

#### [ Kevin Buzzard (May 15 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126591097):
<p>He's using type class inference</p>

#### [ Kevin Buzzard (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964435):
<div class="codehilite"><pre><span></span>Did you get any insights with the ALEXANDRIA / Peter Koepke lecture person today?
</pre></div>


<p>yesterday</p>

#### [ Kevin Buzzard (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964438):
<p>That was an interesting day</p>

#### [ Kevin Buzzard (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964446):
<p>I'll talk about it later, I need to go and do family stuff for 30 minutes</p>

#### [ Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966431):
<p>So Koepke gave a nice talk about some system that they got going which checks ZFC proofs and whose parser parses statements which look like natural language</p>

#### [ Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966437):
<p>I personally don't know how much importance to attach to the concept that a computer-checked proof should be human-readable</p>

#### [ Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966438):
<p>And after that there was a long discussion</p>

#### [ Kevin Buzzard (May 23 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966481):
<p>for over 2 hours</p>

#### [ Kevin Buzzard (May 23 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966483):
<p>where we just talked about life and where all this was going</p>

#### [ Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966497):
<p>Koepke had taken someone else's Haskell code written in 2008 and got an MSc student to understand it and rewrite it better</p>

#### [ Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966500):
<p>Their system is called SAD</p>

#### [ Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966508):
<p>and they are producing "miniatures", i.e. relatively short proofs which rely on a lot of assumptions which are axioms</p>

#### [ Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966551):
<p>e.g. they proved something about successor cardinals being regular but assuming things like kappa x kappa = kappa etc</p>

#### [ Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966554):
<p>what his point was, was that the proof script is genuinely human-readable</p>

#### [ Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966556):
<p>and everyone dreamt about having all 1st and 2nd year UG maths in their system</p>

#### [ Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966564):
<p>but I think that only I have a coherent strategy for making this happen</p>

#### [ Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966567):
<p>i.e. getting 1st and 2nd year UGs to put it into the system themselves</p>

#### [ Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966571):
<p>and we all moaned about how the Cauchy Integral Formula was hard</p>

#### [ Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966616):
<p>and Paulson even had an anecdote about it</p>

#### [ Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966621):
<p>having translated Harrison's proof from (something) into (something)</p>

#### [ Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966622):
<p>maybe from HOL light into Isabelle?</p>

#### [ Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966630):
<p>and there was some subtlety about whether the curve you were integrating around was differentiable or continuously differentiable</p>

#### [ Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966632):
<p>that sort of thing</p>

#### [ Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966640):
<p>And Paulson wants to know what to do with this pot of euro money that he's sitting on</p>

#### [ Kevin Buzzard (May 23 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966698):
<p>but we didn't talk much about that</p>

#### [ Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966755):
<p>but one of his post-docs, Angeliki Koutsoukou-Argyraki, is speaking at Imperial College London in a few weeks' time so perhaps I should have a think about this and talk to her</p>

#### [ Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966761):
<p>My impression is that Paulson wants to reach out to mathematicians but doesn't actually want to go and meet any, he has plenty of more important things to do</p>

#### [ Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966764):
<p>but he has people who can go and meet them for him</p>

#### [ Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966804):
<p>but he is very open to ideas of how to give money to mathematicians</p>

#### [ Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966808):
<p>and turn them to his way of thinking</p>

#### [ Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966811):
<p>and I can definitely work with that</p>

#### [ Johan Commelin (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966866):
<p>This Haskell code producing human-readable proofs... was that from Tim Gowers?</p>

#### [ Johan Commelin (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966873):
<p>He had such a project, but I think it was more like 2012 or something...</p>

#### [ Patrick Massot (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966875):
<p>I'm pretty sure the best you could do now would be to document your journey towards that scheme milestone, then get Mario or Johannes to help you redoing it right, and document that second journey.</p>

#### [ Patrick Massot (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966884):
<p>To me it seems way more useful than adding some more undergrad maths to some new proofs assistant</p>

#### [ Patrick Massot (May 23 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966918):
<p>By the way, who is coming to Europe this summer in the end? I guess we all saw someone decided that ITP is not about maths (and it's not for lack of submissions). But maybe people still want to come?</p>

#### [ Patrick Massot (May 23 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966965):
<p>There is also this <a href="http://www.uc.pt/en/congressos/thedu/thedu18" target="_blank" title="http://www.uc.pt/en/congressos/thedu/thedu18">http://www.uc.pt/en/congressos/thedu/thedu18</a> which is intriguing but there is no program yet</p>

#### [ Mario Carneiro (May 23 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966985):
<p>I am going to Dagstuhl but not ITP this summer</p>

#### [ Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967028):
<p>Is the Dagstuhl the thing Assia is organising?</p>

#### [ Patrick Massot (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967029):
<p>What is Dagstuhl?</p>

#### [ Mario Carneiro (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967030):
<p>yes</p>

#### [ Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967032):
<p>Is that quite soon?</p>

#### [ Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967035):
<p>Last time I thought about that it seemed hopeless for me</p>

#### [ Mario Carneiro (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967039):
<p>no, it's in August I think</p>

#### [ Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967046):
<p>Nooo, why August?</p>

#### [ Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967049):
<p>August doesn't exist</p>

#### [ Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967050):
<p>The dreaded month</p>

#### [ Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967051):
<p>if you're French</p>

#### [ Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967054):
<p>les vacances</p>

#### [ Mario Carneiro (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967056):
<p>this <a href="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341" target="_blank" title="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341">https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341</a></p>

#### [ Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967058):
<p>Indeed, it's les vacances</p>

#### [ Mario Carneiro (May 23 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967102):
<p>what's all this</p>

#### [ Patrick Massot (May 23 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967109):
<p>In France attending a conference in mid-August pretty much automatically implies divorce</p>

#### [ Sean Leather (May 23 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967165):
<p>Huh, so August in the Netherlands is not quite as bad as it sounds like <a href="https://www.frenchtoday.com/blog/french-vocabulary/french-vacation-vocabulary-expressions-les-vacances" target="_blank" title="https://www.frenchtoday.com/blog/french-vocabulary/french-vacation-vocabulary-expressions-les-vacances">August in France</a> is, but I was always surprised how quiet it got.</p>

#### [ Johan Commelin (May 23 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967182):
<p>Yes, August is the only month where we have decent weather... so we all leave the country (-;</p>

#### [ Patrick Massot (May 23 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967226):
<p>I'm also pretty surprised this Dagstuhl thing was not advertised here before</p>

#### [ Patrick Massot (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967343):
<p>Do you think this will be all about Coq and Isabelle, or there could be some room for Lean?</p>

#### [ Mario Carneiro (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967406):
<p>Well, I'll be there...</p>

#### [ Mario Carneiro (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967417):
<p>You should have seen when I went to represent metamath at a conference where no one's ever heard of it</p>

#### [ Patrick Massot (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967462):
<p>I hope the case of Lean is different (metamath looks purely masochistic)</p>

#### [ Mario Carneiro (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967471):
<p>It's really not as bad as it looks</p>

#### [ Mario Carneiro (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967480):
<p>I would not have been so successful with it if it were not so ergonomic</p>

#### [ Patrick Massot (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967525):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> Did you discuss this conference with Assia?</p>

#### [ Patrick Massot (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967529):
<p>Do you know more about it?</p>

#### [ Patrick Massot (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967631):
<p>What about trying to gather either in London or Paris the week after Dagstuhl?</p>

#### [ Patrick Massot (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967641):
<p>That week has much more existence</p>

#### [ Sebastien Gouezel (May 23 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126968938):
<blockquote>
<p>Do you know more about it?</p>
</blockquote>
<p>You mean the conference in August? I already had to negotiate with my wife to go to ICM, another conference this summer is completely impossible. So no, I have not discussed it with Assia.</p>

#### [ Patrick Massot (May 23 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126968954):
<p>I can believe that ICM is already too much</p>

#### [ Patrick Massot (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126969019):
<p>But Assia not advertising this conference to the only mathematician at her university interested in formal proof probably means this conference is not intended at all for mathematicians</p>

#### [ Sebastien Gouezel (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126969050):
<p>Yes, ICM is long, and far away. We considered going there with the family, but Rio is not the safest city in the world for a woman alone and three children...</p>

#### [ Johannes Hölzl (May 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126974146):
<p>I will be in Dagstuhl and at ITP in Oxford. Going to Paris or London would be easy for me.</p>

#### [ Patrick Massot (May 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126974155):
<p>Ah! Do you like schemes or manifolds?</p>

#### [ Kevin Buzzard (May 23 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126977983):
<p>A related question -- what about going to Paris _and_ London :-)</p>

#### [ Assia Mahboubi (May 29 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/127247353):
<p>Hi, indeed I am (co)organizing this Dagstuhl <a href="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341" target="_blank" title="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341">stuff</a>, with 3 colleagues: <a href="http://www.andrej.com/research.html" target="_blank" title="http://www.andrej.com/research.html">Andrej Bauer</a>, <a href="http://peterlefanulumsdaine.com/research.html" target="_blank" title="http://peterlefanulumsdaine.com/research.html">Peter Lumsdaine</a> and  and <a href="http://www.cs.bham.ac.uk/~mhe/" target="_blank" title="http://www.cs.bham.ac.uk/~mhe/">Martin Escardo</a>.  Dagsthul is the CS's Oberwolfach so it is invitation only and  the application (including the list of invitees) has been crafted a long time ago. Before I was even aware that you guys could be interested in this kind of event...</p>


{% endraw %}

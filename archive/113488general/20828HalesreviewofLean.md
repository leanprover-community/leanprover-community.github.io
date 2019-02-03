---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20828HalesreviewofLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Hales' review of Lean](https://leanprover-community.github.io/archive/113488general/20828HalesreviewofLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 18 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182451):
<p>Johan mentioned this but I thought it deserved its own stream. I would like to hear the community's response to the negative points.</p>
<p><a href="https://jiggerwit.wordpress.com/2018/09/18/a-review-of-the-lean-theorem-prover/" target="_blank" title="https://jiggerwit.wordpress.com/2018/09/18/a-review-of-the-lean-theorem-prover/">https://jiggerwit.wordpress.com/2018/09/18/a-review-of-the-lean-theorem-prover/</a></p>
<p>I am not too bothered about the steep learning curve (point 3). This will change over time as more documentation becomes available. There are sporadic counterexamples to Tom's claim, e.g. <span class="user-mention" data-user-id="121918">@Edward Ayers</span> and others seem to have managed well just by asking questions (and indeed I guess technically I am not in any of the categories Hales mentions either, although it did take me a year of my life and I'm still not very good at it).</p>

#### [ Kevin Buzzard (Sep 18 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182648):
<p>As for 9 (diamonds), I know that Chris was finding these extremely frustrating and he was just goofing around with finite sets.</p>

#### [ Mario Carneiro (Sep 18 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182959):
<p>I think the story with diamonds is: there are workarounds, but they aren't particularly natural and you almost certainly won't get it right on your first attempt.</p>

#### [ Patrick Massot (Sep 18 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183534):
<p>Does anyone know what libraries are alluded to in Point 2: "Lean 3 broke the Lean 2 libraries, and old libraries still haven’t been ported to Lean 3. "?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183676):
<p>Chris' struggles were particularly vacuous -- my understanding was that he would end up with two instances of a subsingleton which were not defeq and it would break type class inference.</p>

#### [ Andrew Ashworth (Sep 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183691):
<p>I read over his negative points, but I don't see how they could be (1) fixed, or (2) fixed in a way that doesn't make another set of tradeoffs somewhere else down the line</p>

#### [ Kevin Buzzard (Sep 18 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183751):
<p>Well of course this is a perfectly valid point. One can take any thing, however wonderful, and list all the ways it could be even more wonderful, including problems which are basically known to be impossible to fix.</p>

#### [ Patrick Massot (Sep 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183800):
<p>I think Simon and Sean are working on point 4 (software engineering library)</p>

#### [ Kevin Buzzard (Sep 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183854):
<p>I sympathise with Hales' point 10 -- I did find it a bore during my brief dalliance with topological rings, that I had to write <code>ring</code> and <code>topological space</code> and <code>topological ring</code> everywhere. And it's absolutely true that one wants to take completed tensor products of topological modules when doing adic spaces.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183890):
<p>Is (8) fixed by these <code>additive</code> and <code>multiplicative</code> tricks, to a large extent?</p>

#### [ Patrick Massot (Sep 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183893):
<p>I think "It seems to me that a system designed for doing mathematics should do more than just declare them illegal." is Tom misunderstanding Lean's main goal</p>

#### [ Patrick Massot (Sep 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183971):
<p>Is point 7 (Ugly projection chains are required.) a problem in real situations?</p>

#### [ Patrick Massot (Sep 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183998):
<p>Of course 9, 10 and 11 are real problems, but I have no idea how to fix that</p>

#### [ Patrick Massot (Sep 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134184650):
<p>About point 10, why can't we define <code>topological ring</code> in a single line using class and extends?</p>

#### [ Simon Hudon (Sep 18 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185611):
<p>I think it would be useful to separate the pain points from the points of annoyance.  Point 10 seems to me to be a point of annoyance. In mathematics, you can underspecify your constructions. You can parameterize your constructions and say "the reader knows what I mean here". In formal language everything needs to be completely specified which is bound to cause annoying verbosity. Coq chooses to parameterize constructions using functors and modules which can make modules simple but their use complicated. Lean's adoption of type classes can make the specification of your mathematical concepts a bit more verbose but using them is extremely unintrusive.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185782):
<p>It's comments like this from the CS side which I was really hoping to elicit. Thanks Simon (and Mario!)</p>

#### [ Simon Hudon (Sep 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185871):
<p>You're welcome! I'm glad this is welcome. I sometimes have a hard time stopping myself for ranting and wouldn't want to annoy</p>

#### [ Simon Hudon (Sep 18 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186077):
<p>I'm really tempted to shrug off all those down sides to be honest. </p>
<p>His point 1. about being bloated doesn't make sense to me. Bloated compared to what? HOL-light? Isabelle? The logic aren't the same so it's hard to meaningfully compare. Compared to Coq? Absolutely not. Lean exorcised features like termination checking, coinductive types and pattern matching from the kernel to great benefit.</p>

#### [ Reid Barton (Sep 18 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186310):
<p>I also wondered how many of these cons were disadvantages of Lean compared to other theorem proving systems, versus just "formal methods are hard".</p>

#### [ Reid Barton (Sep 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186744):
<p>Actually point 10 about bundling and unbundling is the item on this list which has caused me the most grief</p>

#### [ Simon Hudon (Sep 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186891):
<blockquote>
<p>Actually point 10 about bundling and unbundling is the item on this list which has caused me the most grief</p>
</blockquote>
<p>Do you know if other provers address the problem better?</p>

#### [ Reid Barton (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187062):
<p>Nope, and I don't really have any idea what a better solution would look like.<br>
I guess a general method for unbundling is "a [type-with-structure] whose underlying type is equal to [T]", so I guess better support for handling equalities would ease the pain. (For example, I saw some slides about some theorem proving system whose name I forget in which if you had a proof of <code>p = q</code> in scope, then the types <code>p</code> and <code>q</code> would unify. I guess GHC works a bit like this as well. It has its own complications.)</p>

#### [ Simon Hudon (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187064):
<blockquote>
<p>I also wondered how many of these cons were disadvantages of Lean compared to other theorem proving systems, versus just "formal methods are hard".</p>
</blockquote>
<p>Good question. And I think the comparison can be broken down into two parts: </p>
<p>1. for someone who's about to start a short term project, is Lean a good choice?<br>
2. if you're willing to contribute libraries or other infrastructure, is Lean a good prover to invest in?</p>

#### [ Johan Commelin (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187072):
<p>I think it should be noted that Tom Hales is someone who has years and years of experience both as a user of theorem provers and as a "regular" research mathematician. This is not just someone listing a couple of annoyances. There probably is quite a lot of thought and experience behind this critique.</p>

#### [ Simon Hudon (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187984):
<p>That's actually the angle that I'm trying to take and I think that's the reason why we should look closely at the list. Individually, we may miss nuggets of insight but I'm hoping a discussion like this can dig them out.</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188213):
<blockquote>
<p>Does anyone know what libraries are alluded to in Point 2: "Lean 3 broke the Lean 2 libraries, and old libraries still haven’t been ported to Lean 3. "?</p>
</blockquote>
<p>I think Tom is wrong on this point. While it's true that we never actually ported the lean 2 libraries, they have been "morally" ported, and the reasons for not porting directly have more to do with the change in management and design decisions than backwards incompatibility on the part of lean</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188283):
<p>When Lean 4 hits, if it has no simplifier, am I right in thinking that porting mathlib will simply wait until it does?</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188292):
<p>more or less</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188308):
<p>mathlib will live wherever it is most well supported</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188311):
<p>Do you know why mathlib takes so long to compile?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188322):
<p>or more precisely why it takes so long for some people?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188329):
<p>For me it's fine but i have a relatively new machine</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188412):
<p>There are a lot of culprits to point at. Extensive use of tactics and slow elaboration are probably the main factors, if we're talking about compilation from scratch</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188432):
<p>Can we fix slow elaboration with cunning instance definitions?</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188453):
<p>Not really, at least not without sacrificing something far more important</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188496):
<p>that's something that needs to be tackled on the core side</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188501):
<p>and I don't even know if it can be improved</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188512):
<p><a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/f9e9bf90003f6a2b82196e60da0b14cc57c90c44/src/valuation_spectrum.lean#L17" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/f9e9bf90003f6a2b82196e60da0b14cc57c90c44/src/valuation_spectrum.lean#L17">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/f9e9bf90003f6a2b82196e60da0b14cc57c90c44/src/valuation_spectrum.lean#L17</a></p>

#### [ Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188526):
<p>but we've all seen examples of simple <code>exact</code> proofs that inexplicably take several seconds</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188531):
<p>Why did Patrick have to <code>set_option class.instance_max_depth 41</code>?<br>
`</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188548):
<p>that's a good question to ask Patrick</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188564):
<p>Is that related? Is thjs "exact proofs take several seconds" phenomenon understood?</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188576):
<p>not by me, not really</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188622):
<p>There was one that came up the other day, maybe Kenny had something which took 4 seconds and changing the elaboration strategy fixed it</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188674):
<p><a href="#narrow/stream/113488-general/topic/why.20is.20this.20slow.3F" title="#narrow/stream/113488-general/topic/why.20is.20this.20slow.3F">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why.20is.20this.20slow.3F</a></p>

#### [ Mario Carneiro (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188678):
<p>yes, that's the sort of thing I'm talking about</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188693):
<p>I'm pretty sure that there are several borderline proofs in mathlib that are just taking a long time to elaborate</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188757):
<p>when you multiply that by thousands it starts to contribute to global warming</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189015):
<p>out of curiosity if I wanted to write a tactic could I write it in C++ (like Coq does with OCaml?)</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189041):
<p>maybe a better question is: can I compile it into a library and dynamically link to it at runtime?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189046):
<p>I think you have to write it in Lean.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189098):
<p>but only because I've never heard anyone else talking about or doing this</p>

#### [ Reid Barton (Sep 18 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189940):
<p>I also wondered whether Lean has some kind of FFI.</p>

#### [ Reid Barton (Sep 18 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190001):
<p>I think there is such a thing as a "Lean extension" but I don't know anything more about that.</p>

#### [ Reid Barton (Sep 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190057):
<p>I don't see any reason why Lean couldn't adopt a Haskell-style FFI to C</p>

#### [ Reid Barton (Sep 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190085):
<p>I wonder what sort of existing libraries Tom Hales wants to use (or uses, in HOL light)</p>

#### [ Simon Hudon (Sep 18 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190267):
<p>I think a proper FFI is planned for Lean 4</p>

#### [ Reid Barton (Sep 18 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190785):
<p>If you want to write a tactic which uses a linear programming solver as an oracle, then a simple FFI is enough. If you want to write "simp, but different" in C++ (for performance or familiarity) then you need direct access to Lean internals.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218109):
<p>About a year ago when I first saw Lean (at the big proof conf) I had similar reservations.</p>
<p>I agree that the language is difficult to learn. There is just a lot of syntax and it is hard to tell if a piece of syntax is fundamental or just sugar. Some of the attributes do magic syntax things that aren't documented.  But the syntax is _way_ easier than Isabelle's.</p>
<p>I think that Lean has a chance of taking off because it is relatively simple and there is a strong focus on tooling support and because it is a fresh start that doesn't have to be backwards compatible.<br>
Eg the Isabelle source code is an intimidating sprawl of different projects and languages. </p>
<p>Complaining about a lack of library support is an inevitable complaint. Libraries for a new computer language always have to start somewhere. I also believe that the ultimate goal of interactive theorem proving should be that writing up a new mathematical theory in a formal system should (in the future)  take about the same amount of time as writing rigorous, informal notes. Formalising a theory for oneself, even a simple undergraduate one, is an extremely powerful way of learning about that theory. So I believe that mathlib should be more of a book of examples and standardisations that you can use to code up your own formalisations, rather than a monorepo of truth.</p>
<p>With the typeclass complaints (7 to 11), I have just come to accept that this is always a total nightmare no matter what system you use. Humans are very good at looking at (their own, internal) typeclasses and rapidly bundling, unbundling, identifying obvious coercions, diamonding, finding isomorphisms and so on. Computers need these spelled out to them, so libraries get cluttered with typeclass-plumbing lemmas. Oh well.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218516):
<blockquote>
<p>So I believe that mathlib should be more of a book of examples and standardisations that you can use to code up your own formalisations, rather than a monorepo of truth.</p>
</blockquote>
<p>I need to have my monorepo of truth because the sooner we can start saying "Look! We have a complete definition of perfectoid spaces! Look! We have a complete formulation of Langlands functoriality! Look! Here are the 6 Clay Problems which are actually mathematics!" the sooner mathematicians will sit up and take notice</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218564):
<p>I regard this as extremely high priority.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218579):
<p>I also, this time just for personal reasons, want to be able to say "Look! Our students are demanding problem sheets are set in Lean and you can't do that for them because you don't know it" to my colleagues, but I have a longer time frame for that goal.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218654):
<p>I think the book of standardisations and formalisations is something else. What would you imagine it looked like? No way are we going to get mathlib to define a compact space as "every open cover has a finite subcover" because they have their reasons for using filters etc. However we are equally unlikely to get the 2nd year metric spaces and topology person to switch to using filters, because most mathematicians never need them.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218666):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> tell me more about what you want. I have a bunch of undergraduates who are currently writing code which has nowhere to go.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219095):
<p>The main thing that I want (and am working on) is automation that is good enough that one doesn't need to clutter ones theory file with lots of lemmas that you wouldn't put in a maths textbook.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219289):
<p>I think it is critical to get formal documents to have the same terseness and readability as informal mathematics.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219315):
<p>Let's just say that in 5 years' time you get funded for some proposal to write an undergraduate mathematics textbook in Lean, and you have to prove that a compact metric space is complete.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219331):
<p>You look at mathlib and discover that there is already a proof in there, probably in the generality of pseudo-compact semi-metric spaces</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219376):
<p>and the proof is unreadable, and intended to be unreadable.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219411):
<p>Is the idea that you prove it again, using the standard filter-free proof presented to undergraduate mathematicians, and underlying it all is a really good interface which people have written so that it now reads like the maths proofs which I present to undergraduate mathematicians in lectures?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219477):
<p>If you did that, it would teach mathematicians how to use Lean I guess. But the proof will still be in mathlib and terse and incomprehensible, and devs would rather use the mathlib proof than the proof in the book.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219483):
<p>I'm just trying to understand how all this fits into the scheme of things.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219485):
<p>Yes the result in the library isn't good enough because it is over-generalised. It doesn't have to be in Latex and be all fancy, and the argumentation doesn't have to be exactly the same as how it is done in lectures. But it has to possible to follow the argument without unpacking lots of more general theories.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219490):
<p>So your goal is a <em>readable proof</em></p>

#### [ Edward Ayers (Sep 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219546):
<p>yes</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219550):
<p>I must be honest, I do not really understand enough about library maintenance to know why mathlib prefers what one might call "obfuscated proofs".</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219560):
<p>But I have no doubt that they have good reasons.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219564):
<p>It has to be a proof where you can read it and be able to see how to make similar arguments yourself.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219576):
<p>And I want to conclude from this that your readable proofs will not actually be useful in terms of library-building, for some reason that I don't understand but am arguing must exist</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219628):
<p>On the other hand it seems to me that your readable proofs will be essential for teaching mathematicians how to use formal proof verification systems.</p>

#### [ Edward Ayers (Sep 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219636):
<p>If you use the obfuscated approach I think you can save time because you only have to prove the super-general case.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219661):
<blockquote>
<p>It has to be a proof where you can read it and be able to see how to make similar arguments yourself.</p>
</blockquote>
<p>I specifically tried to write the definition of a perfectoid space in such a way that a mathematician who knows 0 about theorem provers and look at the code and think "oh yeah, I can see that this might well be a definition of a perfectoid space"</p>

#### [ Edward Ayers (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219666):
<p>It depends on what you want the library to do I guess.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219678):
<p>but I made no attempt to do so for some of the earlier files because I have dreams of getting at least some of this stuff into mathlib</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219682):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- A perfectoid ring, following Fontaine Sem Bourb-/</span>
<span class="n">class</span> <span class="n">perfectoid_ring</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">Tate_ring</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">complete</span> <span class="o">:</span> <span class="n">is_complete</span> <span class="n">R</span><span class="o">)</span>
<span class="o">(</span><span class="n">uniform</span>  <span class="o">:</span> <span class="n">is_uniform</span> <span class="n">R</span><span class="o">)</span>
<span class="o">(</span><span class="n">ramified</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">ϖ</span> <span class="o">:</span> <span class="n">units</span> <span class="n">R</span><span class="o">,</span> <span class="o">(</span><span class="n">is_pseudo_uniformizer</span> <span class="n">ϖ</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">((</span><span class="n">ϖ</span><span class="err">^</span><span class="n">p</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="err">∣</span> <span class="n">p</span><span class="o">))</span>
<span class="o">(</span><span class="n">Frob</span>     <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="err">ᵒ</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">b</span> <span class="o">:</span> <span class="n">R</span><span class="err">ᵒ</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">R</span><span class="err">ᵒ</span><span class="o">)</span> <span class="err">∣</span> <span class="o">(</span><span class="n">b</span><span class="err">^</span><span class="n">p</span> <span class="bp">-</span> <span class="n">a</span><span class="o">))</span>

<span class="n">class</span> <span class="n">perfectoid_space</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">adic_space</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">perfectoid_cover</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Huber_pair</span><span class="o">)</span> <span class="o">[</span><span class="n">perfectoid_ring</span> <span class="n">A</span><span class="bp">.</span><span class="n">R</span><span class="o">],</span>
<span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">is_preadic_space_equiv</span> <span class="n">U</span> <span class="o">(</span><span class="n">Spa</span> <span class="n">A</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219742):
<p>Mathematicians who know this area know that a perfectoid ring is a complete uniform ring satisfying some axioms, and that's what they see here.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219756):
<p>But if they look at the definition of complete, they see filter hell</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219775):
<p>So you see, I am trying to conform to mathlib's aims in some places and your aims in others.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219948):
<p>But in general I am very unclear about why Larry is so keen on human-readable code and given that mathlib is run by people who seem to know what they are doing, and who are intentionally accepting highly minimised code which is not at all optimised for readability, there are presumably arguments for both styles. Can I deduce from what you're saying that there should be a place for both?</p>

#### [ Patrick Massot (Sep 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220322):
<blockquote>
<p>But if they look at the definition of complete, they see filter hell</p>
</blockquote>
<p>That's actually a bad example. Uniform spaces are needed for topological rings (we can't assume the topology is metrizable here)</p>

#### [ Patrick Massot (Sep 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220635):
<blockquote>
<p>Why did Patrick have to <code>set_option class.instance_max_depth 41</code>?</p>
</blockquote>
<p>Because it won't compile with depth 40. Of course it almost certainly doesn't mean that one successful search has depth 41. Most likely it means Lean needs depth 41 before giving up on a bad idea and starting to backtrack. So what seems needed is a way to block stupid ideas in type class search. But this is clearly something for Leo and Sebastian to think about, we can't do anything about that (the same thing applies to the thread discussing proof cache yesterday, it's a bit ridiculous to discuss this as if Leo never thought about its...)  In the mean time we could try to carefully craft type class shortcuts in this specific case.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220691):
<p>complete rings: Yes that is true. But in general I guess one could do a "case study". Ed gets hold of some second year metric spaces and topology lecture course, and tries to write down the course <em>exactly as the lecturer wrote it</em> and see how much of it he could get Lean to swallow, filling in all the auxiliary boring stuff with the <code>by undergraduate_mathematician</code> tactic.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220693):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Why Larry is so keen on human-readable proof, and why we don't have them in mathlib:<br>
Isabelle's language (called Isar) was always intended to produce human readable proofs. A lot of document generation around it allows to produce TeX-documents. The automation is geard towards it. And type inference is much easier in the simple typed setting of Isabelle.</p>
<p>One important part in readable formal proofs is to repeat the statements you want to prove. But in DTT this is much harder, as type inference often fails, and the user needs to provide more information (or needs to add type class information <code>letI</code> and co). In Isabelle this is often not necessary. There, it is much easier just to copy your statement and it just works, without adding additional typing informations. Of course, this is all at the cost of a much simpler type system.</p>
<p>At least this is for me a reason, why I don't use <code>have</code> etc as much as I did in Isabelle. Also Isabelle has more automation like <code>auto</code> and <code>sledgehammer</code>, where it makes sense just to say what you want to prove, without stating how it is proved.</p>

#### [ Patrick Massot (Sep 19 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221026):
<blockquote>
<p>I think it should be noted that Tom Hales is someone who has years and years of experience both as a user of theorem provers and as a "regular" research mathematician. This is not just someone listing a couple of annoyances. There probably is quite a lot of thought and experience behind this critique.</p>
</blockquote>
<p>Yes, we need to be careful not to become a fanboy community. Everybody here love Lean, but it doesn't mean it can't be criticized. I've seen this with the Blender3D community, and I think it's pretty dangerous. And we can actually act on some of these bad points, especially the learning curve and libraries part. Of course many things are beyond our control, but I'm sure Leo will read it at some point, and although he probably knows all this, he may still get something out of it (but I'm afraid many things are very difficult to "fix" without breaking something else).</p>

#### [ Kevin Buzzard (Sep 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221352):
<p>Ed's comments make me think that he might be better off using Isabelle</p>

#### [ Kevin Buzzard (Sep 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221353):
<p>on the other hand it would be wonderful to do this sort of project in Lean for teaching purposes.</p>

#### [ Edward Ayers (Sep 19 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134224649):
<p>Don't make me go back to Isabelle!</p>

#### [ Scott Morrison (Sep 19 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134224759):
<p>:-)</p>

#### [ Edward Ayers (Sep 19 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225432):
<p>More seriously,<br>
I don't quite agree with <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  about readability.<br>
Firstly, most of the time you can avoid the 'dependent' part of DTT and write out proofs in the same way as Isar without too many problems.<br>
There is no reason why Lean can't have automation like sledgehammer and auto, it is just that Isabelle has been around longer.</p>
<p>Readability for me doesn't mean that it pretty prints to Latex and has plain english keywords. It means that what is written maps cleanly to an explanation at a level that a human would give.</p>
<p>Perhaps a good example is</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">add_comm</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">n</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">zero_add</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">(</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">suffices</span> <span class="n">succ</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">succ</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">),</span> <span class="k">from</span>
    <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">succ_add</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">congr_arg</span> <span class="n">succ</span> <span class="o">(</span><span class="n">add_comm</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
</pre></div>


<p>This would not look good in a maths textbook, but once you take time to understand the syntax, it matches what a human would write:</p>
<blockquote>
<p>Induct on <code>n</code>. In the zero case we have <code>n+0=0+n</code> which we proved in <code>nat.zero_add</code>.<br>
In the <code>m+1</code> case, it suffices to prove <code>succ (n + m) = succ (m + n)</code> since we have<br>
<code> ∀ (n m : ℕ), succ n + m = succ (n + m)</code>. But then we are done since <code>(n+m)=(m+n)</code> by the induction premiss.</p>
</blockquote>
<p>The proofs are totally different syntactically but they both share the same skeleton and go in to (roughly) the same level of detail. That's what I mean by readability.</p>
<p>So my complaint with mathlib is that often the lemmas and definitions will sometimes deviate from the level of explanation that a mathematician is after.<br>
Either spelling out simple lemmas that a mathemematician would not bother with, or appealing to some mysterious general lemma. </p>
<p>I think a good example of this is defining the lattice structure on filters using galois connections in mathlib (in <code>filter.lean</code>). Here, we take advantage of a general theory to define a lattice structure. But then if you read the code, after this we have to use <code>original_complete_lattice.copy</code> because we want non-general definitions of join and meet. So using the general theory introduced a lot of plumbing that makes it hard to follow.  (apologies to the authors of that file, I am not trying to be a  jerk and I don't have a better way of solving this)</p>

#### [ Edward Ayers (Sep 19 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225517):
<p>Perhaps that's not a good example, I don't know how the lattice structure on a filter would be introduced in a maths textbook.</p>

#### [ Edward Ayers (Sep 19 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225948):
<p>Isar syntax doesn't meet this definition of readability because you will often have to write out vastly more steps than a textbook proof would need, even with the help of Isabelle's powerful automation.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134226390):
<p>With readable I don't mean that it resembles readable English text. What I mean is that it is readable without looking at the tactic output. This is not only a technicality: When we have control how the proof is represented why have more control how to guide a user through the proof. Maybe we can call this <strong>explicit</strong> proofs?!</p>
<p>Your example of <code>add_comm</code> is an exception in mathlib. Often one wouldn't write the <code>suffices</code>. so the (second) central part to understand the proof is missing. The main part, the induction, is luckily easy to see.</p>
<p>Another difference is that Isar doesn't have a very powerful tactic mode (at least nothing comparable to Lean's). So people are much more eager to write down <code>have</code> with repeating a similar statements. This again helps a reader going through a proof and reading it. </p>
<p>I also hope that Lean will have in the non to distant future tactics similar to auto (tidy is a good candidate) and sledgehammer. But we will see if people start writing more explicit proofs.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134226465):
<p>I think currently it is not possible to find a theorem prover were you don't need to write vastly more steps than a textbook proof would need. Hopefully somewhere in the future this is possible. But we are far from this.</p>


{% endraw %}

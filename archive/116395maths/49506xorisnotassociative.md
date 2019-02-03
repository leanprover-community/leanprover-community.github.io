---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49506xorisnotassociative.html
---

## Stream: [maths](index.html)
### Topic: [xor is not associative](49506xorisnotassociative.html)

---


{% raw %}
#### [ Kenny Lau (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256439):
<p>Could someone prove that xor is not associative constructively, perhaps by constructing a Kripke model where this fails?</p>

#### [ Kenny Lau (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256453):
<p>here <code>xor</code> is defined as Lean defines it: <code>p xor q := (p and not q) or (not p and q)</code></p>

#### [ Kenny Lau (Apr 18 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256507):
<p>or maybe show that <code>xor</code> is associative implies LEM</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256694):
<p>if you defined <code>xor'</code> as <code>(p or q) and (not p or not q)</code> then can you constructively prove that this is the same as <code>xor</code>?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256703):
<p>I can't believe I'm thinking about such nonsense</p>

#### [ Kenny Lau (Apr 18 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256719):
<p>let's say you can. and then?</p>

#### [ Kenny Lau (Apr 18 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256762):
<p>I've convinced myself that you can</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256781):
<p>I guess distributivity is all fine constructively</p>

#### [ Patrick Massot (Apr 18 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256783):
<blockquote>
<p>I can't believe I'm thinking about such nonsense</p>
</blockquote>
<p>Kevin, I'm very disappointed</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256787):
<p>I'm trying to finish this affine scheme thing and he keeps pestering me!</p>

#### [ Patrick Massot (Apr 18 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256846):
<p>He should work on mechanics each time he is tempted by constructivist non-sense</p>

#### [ Patrick Massot (Apr 18 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256848):
<p>mechanics is super constructive</p>

#### [ Kenny Lau (Apr 18 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256851):
<p>you bunch are horrible people</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256852):
<p>with spanners and everything</p>

#### [ Patrick Massot (Apr 18 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256971):
<blockquote>
<p>you bunch are horrible people</p>
</blockquote>
<p>We are working on saving your soul</p>

#### [ Kenny Lau (Apr 18 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125256975):
<p>:(</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257018):
<p>Kenny, the only technique I know for this sort of thing is to imagine Prop is some topological space</p>

#### [ Kenny Lau (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257032):
<p>that's one interpretation</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257034):
<p>and then there's something with open sets</p>

#### [ Kenny Lau (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257036):
<p>but I like Kripke model more</p>

#### [ Patrick Massot (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257042):
<p>Imagining Prop is a topological space saves souls??</p>

#### [ Kenny Lau (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257043):
<p>since it's morally what's going on behind constructivism</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257044):
<p>where not p is something like the interior of the complement of p</p>

#### [ Kenny Lau (Apr 18 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257048):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> he's unsaving me</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257062):
<p>All I'm saying is that the one time in my life when I thought about this was a few months ago, when I proved that not not p implies p was not provable constructively</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257070):
<p>by making some trivial observation about topological spaces</p>

#### [ Kenny Lau (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257074):
<p>right, but the connection is not trivial at all :-)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257075):
<p>having just read some Wikipedia article about this sort of thing</p>

#### [ Patrick Massot (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257083):
<p>soon they will be using toposes...</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125257087):
<p>and it seems to me that your question might yield to the same strategy</p>

#### [ Mario Carneiro (Apr 18 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125264808):
<p>here is a simpler problem: if not (p xor q), is p decidable?</p>

#### [ Mario Carneiro (Apr 18 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125265116):
<p>ah, of course not: if p &lt;-&gt; q then not (p xor q) but then p may be some arbitrary nondecidable proposition</p>

#### [ Kenny Lau (Apr 18 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125265606):
<p>use non-well-founded recursion to prove that p is decidable :P <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Apr 18 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125265608):
<p>using p &lt;-&gt; q</p>

#### [ Gabriel Ebner (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266047):
<p>Maybe a better problem: if <code>xor p q</code>, is <code>p</code> decidable?</p>

#### [ Gabriel Ebner (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266061):
<p>BTW, this is a nice puzzle!  Thanks, <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266065):
<p>no problem</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266078):
<p>here's what inspired me</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266084):
<p>I wanted to prove that Prop is a group under xor</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266088):
<p>but if this is possible, then it would imply double negation elimination</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266089):
<p>so one of the group axioms must go wrong</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266091):
<p>who can possibly know that it is the associativity</p>

#### [ Kenny Lau (Apr 18 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266093):
<p>(well I eliminated the other trivial axioms though)</p>

#### [ Kenny Lau (Apr 18 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266148):
<blockquote>
<p>Maybe a better problem: if <code>xor p q</code>, is <code>p</code> decidable?</p>
</blockquote>
<p>technically, even <code>p or not p</code> doesn't mean <code>p</code> is decidable</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266159):
<p>Kenny did you try the topological space approach?</p>

#### [ Gabriel Ebner (Apr 18 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266173):
<p>Ah, you're right of course.</p>

#### [ Kenny Lau (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266216):
<blockquote>
<p>Kenny did you try the topological space approach?</p>
</blockquote>
<p>I'm busy getting free group to work</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266225):
<p>You need to check p xor not p is provable :-)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266232):
<p>OK let me just spend a few minutes doing the top space thing in case it clarifies anything</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266237):
<p>I don't remember the details</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266244):
<p>but is the idea somehow that we can think of a prop as being an open set in a topological space</p>

#### [ Kenny Lau (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266248):
<p>right</p>

#### [ Kenny Lau (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266250):
<p>not = exterior, or = union, and = intersection</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266254):
<p>not is what?</p>

#### [ Kenny Lau (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266255):
<p>exterior</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266256):
<p>Do I take the interior of the complement?</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266294):
<p>right</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266296):
<p>Is that what exterior means? I've never heard that</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266300):
<p>yes</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266303):
<p>interior + boundary + exterior = whole space</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266305):
<p>interior + boundary = closure</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266306):
<p>So are we 100 percent fixed on definition of xor?</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266309):
<p>what is xor here?</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266313):
<p>oh right, we already have everything</p>

#### [ Kenny Lau (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266316):
<p>yes then</p>

#### [ Mario Carneiro (Apr 18 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266318):
<p>so here is a proof of LEM from xor assoc:</p>
<div class="codehilite"><pre><span></span>example (h : ∀ p q r, xor p (xor q r) ↔ xor (xor p q) r) {p} : p ∨ ¬ p :=
have ¬ xor p p, from λ h, h.elim (λ ⟨hp, np⟩, np hp) (λ ⟨hp, np⟩, np hp),
have xor p (xor p true), from (h p p true).2 (or.inr ⟨trivial, this⟩),
this.imp and.left and.right
</pre></div>

#### [ Kevin Buzzard (Apr 18 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266332):
<p>great, Mario just saved me a job :-)</p>

#### [ Kenny Lau (Apr 18 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266341):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> muito obrigado</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266387):
<p>this is random but related to xor: has anyone seen a definition of one-hot encoding?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266388):
<p>now the other way!</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266391):
<p>Oh the other way is trivial, right?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266392):
<p>Just do cases</p>

#### [ Kenny Lau (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266396):
<p>right</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266400):
<p>so this is another way of formulating LEM :-)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266406):
<p>that Prop is a group :-)</p>

#### [ Kenny Lau (Apr 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266595):
<p>right</p>

#### [ Kenny Lau (Apr 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266598):
<p>and people won't guess that it is associativity that fails</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266605):
<p>I'll put it on next year's Christmas Quiz</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266655):
<p>I wonder if there is any group structure on Prop?</p>

#### [ Gabriel Ebner (Apr 18 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266662):
<p>The double-negation translation of <code>xor</code> should do the job.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266665):
<p>rofl</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266676):
<p>I am not so sure life is so easy</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266694):
<p>I don't think that will satisfy the cancellation laws on nondecidable props</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266697):
<p>I am not sure this has inverses.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266758):
<p>This question is related to putting a group structure on the set of open sets in a topological space I guess</p>

#### [ Gabriel Ebner (Apr 18 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266765):
<p>Mmh, the double-negation translation turns classical theorems into intuitionistic theorems.  So if <code>xor</code> is associative, etc., classicaly then <code>xor^N</code> should be intuitionistically associative, etc.</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266781):
<p>true, but the group has to include all props, not just the negative props</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266840):
<p>in my language, consider open sets which are dense. Their negation is empty</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266846):
<p>so you have lost information which is never coming back, and that's bad for groups</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266861):
<p>Does the following make sense:</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266864):
<p>there is a two-point space with one point open</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266869):
<p>and this space has three open sets</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266871):
<p>and so if it were a group it would be cyclic of order 3</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266923):
<p>and now I want to write down a map from bool to this set or from this set to bool</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266927):
<p>and argue that if Prop had a group structure it would have to be a group homomorphism</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266929):
<p>but things don't add up</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266957):
<p>Ah, how about this: every (definable in intuitionistic logic) one-arg operator is noninjective on some topological space or is the identity</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266960):
<p>because I am hoping I am writing down two incompatible "interpretations" of Prop somehow</p>

#### [ Gabriel Ebner (Apr 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125266964):
<p>Ah yes, everything goes through except <code>xor p false &lt;-&gt; p</code>...</p>

#### [ Kenny Lau (Apr 18 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267027):
<blockquote>
<p>Ah yes, everything goes through except <code>xor p false &lt;-&gt; p</code>...</p>
</blockquote>
<p>what do you mean?</p>

#### [ Kenny Lau (Apr 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267039):
<p>isn't that intuitionistically valid</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267057):
<p><code>xor</code> implies both its arguments are decidable</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267060):
<p>(in the LEM sense)</p>

#### [ Kenny Lau (Apr 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267075):
<p>does it?</p>

#### [ Kenny Lau (Apr 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267093):
<p>right, it does</p>

#### [ Kenny Lau (Apr 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267120):
<p>something is wrong with me</p>

#### [ Gabriel Ebner (Apr 18 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125267153):
<p><code>xor p false &lt;-&gt; p</code> fails for the double-negation translation.  It is true in the official version, though.</p>

#### [ Peter Jipsen (Apr 24 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624185):
<p>Can't one just check associativity of xor in Heyting algebras? It fails in the 3-element Heyting algebra where 0&lt;1&lt;2:  (2 xor 2) xor 1 \ne 2 xor (2 xor 1)    (assuming a xor b is defined as (a or b) and not (a and b)). Of course this would require quite some background work defining Heyting algebras etc.</p>

#### [ Kenny Lau (Apr 24 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624194):
<p>Is it the same thing as Kripke frames?</p>

#### [ Peter Jipsen (Apr 24 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624204):
<p>Yes, it's the algebraic version</p>

#### [ Kenny Lau (Apr 24 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624210):
<p>aha</p>

#### [ Kenny Lau (Apr 24 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624216):
<p>a xor b is defined as (a and not b) or (not a and b)</p>

#### [ Kenny Lau (Apr 24 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624225):
<p>would knowing about Kripke frames and boolean algebra make Heyting algebra easy to learn? if so, do you mind teaching me?</p>

#### [ Andrew Ashworth (Apr 24 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624285):
<p><a href="http://www.cri.ensmp.fr/classement/doc/E-372.pdf" target="_blank" title="http://www.cri.ensmp.fr/classement/doc/E-372.pdf">http://www.cri.ensmp.fr/classement/doc/E-372.pdf</a></p>

#### [ Kenny Lau (Apr 24 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624360):
<p>:o infinite logic?</p>

#### [ Andrew Ashworth (Apr 24 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624389):
<p>the paper is a little hard to read without a little more background</p>

#### [ Andrew Ashworth (Apr 24 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624390):
<p>but the coq code is nice</p>

#### [ Andrew Ashworth (Apr 24 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125624391):
<p><a href="https://github.com/SkySkimmer/NormalisationByCompleteness" target="_blank" title="https://github.com/SkySkimmer/NormalisationByCompleteness">https://github.com/SkySkimmer/NormalisationByCompleteness</a></p>

#### [ Peter Jipsen (Apr 24 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125625538):
<p>The definition (a and not b) or (not a and b) has the same counterexample.<br>
The equivalence between finite Heyting algebras and finite partially ordered Kripke frames is similar to the equivalence between finite Boolean algebras and finite sets, so you have all the necessary background. (In the general case Esakia spaces are a categorical dual of Heyting algebras.) Propositional intuitionistic logic is decidable, so questions like this can be answered algorithmically by a tableau prover or Gentzen's sequent calculus LJ.</p>

#### [ Kenny Lau (Apr 24 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125625548):
<p>thanks</p>

#### [ Peter Jipsen (Apr 24 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/xor%20is%20not%20associative/near/125626599):
<p>A interesting test problem is to decide if the two definitions of xor are intuitionistically equivalent. I would like to understand how one would use Lean to help prove or refute it. E.g. is there a tactic that implements tableau?</p>


{% endraw %}

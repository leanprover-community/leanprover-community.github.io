---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48449provingltfromdecidability.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [proving  lt from decidability](https://leanprover-community.github.io/archive/113488general/48449provingltfromdecidability.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Adam Kurkiewicz (Apr 05 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661129):
<p>I'd like to show the following lemma:</p>
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  &lt;  0, from eq.subst Pp P,
false.elim (nat.decidable_lt 1  0)
</pre></div>


<p>Concretely, I'd like to get a proof of false from <code>nat.decidable_lt 1 0</code>. But I don't understand how to use decidabilty in lean.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661254):
<p><code>example : 1  &lt;  0  → false := dec_trivial</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661257):
<p>I'm not saying these things are easy to use though :-)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661312):
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  &lt;  0, from eq.subst Pp P,
(show  1  &lt;  0  → false, by exact dec_trivial) olt0
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661314):
<p>and as you can see, I'm certainly no master of them myself.</p>

#### [ Kenny Lau (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661362):
<div class="codehilite"><pre><span></span>def big_not_zero (a : nat) (P : 1 &lt; a) : a ≠ 0 :=
λ h, nat.not_lt_zero 1 $ h ▸ P
</pre></div>

#### [ Kenny Lau (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661363):
<p>\&gt; implying I'm a master of them</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661364):
<p>:-)</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661365):
<p>Thank you! What is <code>exact</code>?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661370):
<p><code>by</code> puts me into tactic mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661371):
<p><code>exact</code> is a tactic</p>

#### [ Kenny Lau (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661372):
<p><span class="user-mention" data-user-id="111040">@Adam Kurkiewicz</span> just do <code>from dec_trivial</code> instead of <code>by exact dec_trivial</code></p>

#### [ Kenny Lau (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661373):
<p>there's no need to go into tactic mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661374):
<p>I have trouble getting out of tactic mode</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661415):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> not working <code> exact tactic failed, type mismatch, given expression has type </code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661418):
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  &lt;  0, from eq.subst Pp P,
(show  1  &lt;  0  → false, from dec_trivial) olt0
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661421):
<p>works for me</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661422):
<p>nevermind, that works.</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661436):
<p>I'm surprised this is not working</p>
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  &lt;  0, from eq.subst Pp P,
dec_trivial olt0
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661438):
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
begin
intro H,
rw H at P,
revert P,
exact dec_trivial
end
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661439):
<p>aah</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661441):
<p>tactic mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661481):
<p>makes it all look so easy</p>

#### [ Kenny Lau (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661486):
<blockquote>
<p>I'm surprised this is not working</p>
</blockquote>
<div class="codehilite"><pre><span></span>def  big_not_zero (a : nat) (P : 1  &lt; a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  &lt;  0, from eq.subst Pp P,
dec_trivial olt0
</pre></div>


<p><code>dec_trivial</code> takes no argument</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661492):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Where did you learn tactic mode from? last few chapters of lean tutorial?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661494):
<p>Tactic mode chapter</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661499):
<p>I have no idea why TPIL spends so long teaching people term mode</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661500):
<p>Fair enough, I didn't last that long :D</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661501):
<p>For a beginner tactic mode is the bomb</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661504):
<p>you can see what you're doing at all times</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661544):
<p>what the goal is, what the hypotheses are</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661547):
<p>and you can try simp on every line in case it does the job</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661550):
<p>I like term mode, at least I have an illusion I understand what's going on :)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661553):
<p>you have far more powerful tools available to you in tactic mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661555):
<p>and then later on you can start figuring out what the tools are doing</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661556):
<p>and how they're doing it</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661564):
<p>You say "I don't understand decidability or how to use it"</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661565):
<p>I say "dec_trivial invokes a great tactic"</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661605):
<p>so your problems are solved in the short term</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661612):
<p>and then in the longer term you can start wondering about what it's doing and how it's doing it</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661619):
<p>My method is more robust than Kenny's</p>

#### [ Kenny Lau (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661621):
<blockquote>
<p>My method is more robust than Kenny's</p>
</blockquote>
<p>yeah right</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661626):
<p>because his solution relies on you knowing that there's a theorem in the library</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661629):
<p>called <code> nat.not_lt_zero </code></p>

#### [ Kenny Lau (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661632):
<p>implying one shouldn't know about theorems in the library</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661634):
<p>whereas mine just relies on you being aware that stuff like this is decidable and there's a tactic which does it</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661636):
<p>I am saying mine is more robust.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661639):
<p>I am not saying anything about whether it's a good idea to know the library</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661680):
<p>What if tomorrow Adam wants to prove <code>2&lt;1-&gt;false</code>?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661689):
<p>We all know it's decidable</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661695):
<p>and you and I know we can use no_confusion or all sorts of other tricks</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661698):
<p>but <code>dec_trivial</code> just does the job</p>

#### [ Kenny Lau (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661700):
<div class="codehilite"><pre><span></span>def big_not_zero&#39; (a : nat) (P : 1 &lt; a) : a ≠ 0 :=
λ h, (show ¬1 &lt; 0, from dec_trivial) (h ▸ P)
</pre></div>

#### [ Kenny Lau (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661701):
<p>satisfied?</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661745):
<p>It's good advice Kevin, I'll learn the tactic mode.</p>

#### [ Kenny Lau (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661748):
<p>alright</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661753):
<p>I think you should start with tactic mode and move on to term mode later.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661754):
<p>It's what they do in Software Foundations</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661757):
<p>and it's what I'm doing in the book I'm writing on doing maths in Lean</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661765):
<p>but this is because my book is targetting mathematicians who have no idea what this lambda business is all about</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661766):
<p>because typically they will know no functional programming</p>

#### [ Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661767):
<p>let's replace matlab with haskell</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661768):
<p>They do that next door</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661770):
<p>in the computing department</p>

#### [ Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661771):
<p>great</p>

#### [ Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661772):
<p>see you</p>

#### [ Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661773):
<p>:P</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661812):
<p>in the computing department?</p>

#### [ Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661813):
<p>right</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661814):
<p>Remember I'm on the curriculum review committee!</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661815):
<p>But I don't think I can push for Haskell for mathematicians</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661819):
<p>I am currently pushing for Python</p>

#### [ Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661820):
<p>i'm just kidding</p>

#### [ Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661822):
<p>but python is already there</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661823):
<p>but not maths in python</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661825):
<p>just general python</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661828):
<p>i.e. teach them classes etc</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661833):
<p>OOP python is the worst lol</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661834):
<p>oh</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661835):
<p>use java for OOP</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661837):
<p>oh</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661840):
<p>oh</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661841):
<p>pee</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661843):
<p>Should I push for java?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661848):
<p>Why would a mathematician want to learn java?</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661849):
<p>heh</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661850):
<p>I think we should just teach them tactic mode ;-)</p>

#### [ Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661851):
<p>push for lean</p>

#### [ Kenny Lau (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661890):
<p>problem solved</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661891):
<p>I think that some of them might want to compute something at some point</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661892):
<p>maybe they do that in the applied maths parts or something</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661893):
<p>I have no idea what they do there</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661895):
<p>but I don't think it's theorems</p>

#### [ Johannes Hölzl (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661899):
<p>Of couse</p>

#### [ Johannes Hölzl (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661905):
<p>(deleted)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661906):
<p>I think they figure out what f(10) is if they know some differential equation satisfied by f, and also they know f(0)</p>

#### [ Kenny Lau (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661907):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> wrong chat</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662069):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'd say teaching OOP is a bad idea. OOP is kind of dying at the moment anyway -- very few new languages actually have rich OOP features (rust, golang), and even in python very little new stuff gets written using OOP.</p>
<p>We've got a great new guy at Glasgow, who's teaching first year programming in python. He uses jupyter notebooks and shows applications of computation to multiple different problems (simulating fireworks, solving Travelling Salesman, etc.). I've done a guest lecture on Nim this year (<a href="https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material" target="_blank" title="https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material">https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material</a>).</p>
<p>I think that's a more productive use of student's time than teaching them OOP.</p>

#### [ Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662070):
<p>I insisted to not use jupyter</p>

#### [ Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662074):
<p>even in the exam :P</p>

#### [ Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662077):
<p><code>python -m pip install numpy</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662120):
<p>So I am in the maths department at Imperial College London and we're having a top-to-bottom curriculum review, and amongst the things that can change is that we can completely rethink what we teach to the undergraduates in terms of programming.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662121):
<p>So I am definitely genuinely interested in hearing people's opinions.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662123):
<p>However we are definitely focussed on what mathematicians should need to know</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662131):
<p>in the sense of "what people who employ mathematicians want them to know"</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662133):
<p>You'd obviously want to modify the content a little bit to make it more mathsy,  but I think coding up an optimal algorithm to play Nim is definitely a worthy thing to teach first year mathematicians.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662136):
<p>Your link doesn't work btw</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662189):
<p>Ah, it's hidden from students cause it has solutions :D. one moment</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662191):
<p>don't worry</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662192):
<p>I don't want to disrupt</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662360):
<p>That's the task statement: <a href="/user_uploads/3121/US_PO9-qzNBOQE1P_W4cNQ1C/lab17-3.html" target="_blank" title="lab17-3.html">lab17-3.html</a> </p>
<p>There are ~7 specific python template files, which walk them through a solution, and they have to implement each one.</p>
<p>Each file gets automatically checked using something called "CMS", I believe stands  for "Contest Management System". Checking uses a regular test suite.</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662415):
<p>Happy to share everything if you'd like, but at the moment I'm tethering and the internet is a bit slow.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662419):
<p>honestly don't worry</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662424):
<p>I can imagine what is there</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662429):
<p>I always imagine stuff like nim as being in the <code>recreational mathematics</code> box</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662430):
<p>i.e. stuff they do outside of regular maths</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662469):
<p>but I am not 100% sure whether I have this in the right box</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662479):
<p>python has <code>^</code> -- do you let them use this or force them to code their own?</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662645):
<p>I let them use that after they've learned how it works.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662704):
<p>Just the opposite of what I did with my kids</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662708):
<p>I asked them how to compute powers in python and let them be completely confused for 15 minutes</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662709):
<p>it's generally a problem with teaching python, it has everything and students sometimes just solve things with one-liners, without ever understanding it.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662713):
<p>just like tactic mode ;-)</p>

#### [ Kenny Lau (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662721):
<p>I don't normally use <code>numpy</code> and <code>sympy</code> :P</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662725):
<p>Kenny, what do we teach the 1st years?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662726):
<p>Currently</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662729):
<p>Do they import a lot of libraries?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662731):
<p><code>scipy</code>?</p>

#### [ Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662770):
<p><code>numpy</code> and <code>sympy</code></p>

#### [ Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662771):
<p>I thought you're the head of curiculum reform</p>

#### [ Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662775):
<p>curriculum</p>

#### [ Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662776):
<p>words</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662841):
<p>I'm just on the committee</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662843):
<p>my job is to decide what to do in the future</p>

#### [ Kenny Lau (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662844):
<p>well you're the acting head of the department</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662846):
<p>I don't want to pollute my understanding by knowing what we currently do</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662857):
<p>Maybe I should go and fill in forms :-/</p>

#### [ Kenny Lau (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662900):
<p>how many goddam forms do you have</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662901):
<p>they come in at a rate faster than I can fill them in</p>

#### [ Kenny Lau (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662903):
<p>what are those forms</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662912):
<p>I had to do a risk assessment form for Ana because she's pregnant. 6 pages of questions such as how much radioactive material there was in the department etc. Life is great when you're a manager.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662949):
<p>OK I'm going to fill in more right now</p>

#### [ Kenny Lau (Apr 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662952):
<p>life is always great</p>

#### [ Andrew Ashworth (Apr 05 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124664028):
<p>I think between python, R, and Matlab, that's quite enough for a maths student... in a way I'm a little sad you can't get by without just pen, paper, and coffee pot</p>

#### [ Patrick Massot (Apr 05 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686378):
<blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'd say teaching OOP is a bad idea. OOP is kind of dying at the moment anyway -- very few new languages actually have rich OOP features (rust, golang), and even in python very little new stuff gets written using OOP.</p>
<p>We've got a great new guy at Glasgow, who's teaching first year programming in python. He uses jupyter notebooks and shows applications of computation to multiple different problems (simulating fireworks, solving Travelling Salesman, etc.). I've done a guest lecture on Nim this year (<a href="https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material" target="_blank" title="https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material">https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material</a>).</p>
<p>I think that's a more productive use of student's time than teaching them OOP.</p>
</blockquote>
<p>What is this crazyness? Where did you see OOP dying?</p>

#### [ Patrick Massot (Apr 05 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686392):
<p>I guess  this is what Haskell people say?</p>

#### [ Patrick Massot (Apr 05 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686402):
<p>But what about the real world?</p>

#### [ Moses Schönfinkel (Apr 05 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686651):
<p>OOP is definitely not dying in the industry.</p>

#### [ Patrick Massot (Apr 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686878):
<p>Yes, this very much sounds like functional programming academic fantasy</p>

#### [ Sebastian Ullrich (Apr 05 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686972):
<p>To say that OOP is dying is certainly hyperbole, but none of the languages mentioned are particularly functional...</p>

#### [ Moses Schönfinkel (Apr 05 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687127):
<p>Go doesn't even have generics, speaking of modern design...</p>

#### [ Patrick Massot (Apr 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687187):
<p>Go certainly looks awful</p>

#### [ Patrick Massot (Apr 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687309):
<p>I never saw Rust but the wikipedia page features quite a occurrences of Haskell and ML</p>

#### [ Patrick Massot (Apr 05 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687600):
<p>Let's discuss something more productive: <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> am I correct in thinking that the nightly download link on  <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a> is no longer relevant and should not be used anymore?</p>

#### [ Chris Hughes (Apr 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687691):
<blockquote>
<p>Let's discuss something more productive: <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> am I correct in thinking that the nightly download link on  <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a> is no longer relevant and should not be used anymore?</p>
</blockquote>
<p>Is there a new download link. It took me ages to update lean today, because MSYS didn't know where my c compiler was, and neither did I.</p>

#### [ Patrick Massot (Apr 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687706):
<p><a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a></p>

#### [ Patrick Massot (Apr 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687752):
<p>You need to compare with <a href="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4">https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4</a></p>

#### [ Patrick Massot (Apr 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687757):
<p>(my understanding is it's not yet more automatic, but this is already great progress)</p>

#### [ Sebastian Ullrich (Apr 05 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687777):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Correct. We're still waiting on AppVeyor enabling cron builds for us before we can make it official</p>

#### [ Patrick Massot (Apr 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687820):
<p>Thanks</p>


{% endraw %}

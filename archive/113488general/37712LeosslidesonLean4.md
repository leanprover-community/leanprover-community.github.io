---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37712LeosslidesonLean4.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Leo's slides on Lean 4](https://leanprover-community.github.io/archive/113488general/37712LeosslidesonLean4.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133248994):
<blockquote>
<p>Apropos Lean 4: Leo gave a new talk at Galois inc. You find the slides on <a href="http://leanprover.github.io" target="_blank" title="http://leanprover.github.io">leanprover.github.io</a>: <a href="http://leanprover.github.io/talks/LeanAtGalois.pdf" target="_blank" title="http://leanprover.github.io/talks/LeanAtGalois.pdf">http://leanprover.github.io/talks/LeanAtGalois.pdf</a> Some new information about Lean4!</p>
</blockquote>
<p>What do the colors mean on slide 29?</p>

#### [ Johannes Hölzl (Sep 03 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249362):
<p>I guess blue are things implemented in C++, green for Lean, and red is external</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249440):
<p>(deleted)</p>

#### [ Johannes Hölzl (Sep 03 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249459):
<p>On the second slide it says: "Lean is a platform for <strong>software verification</strong> and formalized mathematics"</p>

#### [ Johannes Hölzl (Sep 03 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249482):
<p>while software verification is highlighted mathematics is still mentioned...</p>

#### [ Patrick Massot (Sep 03 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249514):
<p>but he was talking in front of people doing software verification</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249518):
<p>He mentions Mario's ring tactic</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249521):
<p>he hardly ever talks about mathlib</p>

#### [ Johan Commelin (Sep 03 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249541):
<p>Kevin, he even mentions <em>you</em>!</p>

#### [ Johan Commelin (Sep 03 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249594):
<p>The future of Lean 4 depends on you (-;</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249598):
<p>He mentioned me in his Oxford talk. He believes in using Lean for education so it gets a mention. He is more skeptical about mathlib (he thinks it's too early) and in his Oxford talk he barely mentioned it at all.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249625):
<p>On the other hand, <code>ring</code> is a <em>really</em> nice tactic, and Mario's recent edits to the tactic show that it really is not a trivial matter at all to get it working in Lean.</p>

#### [ Johan Commelin (Sep 03 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249629):
<p>Well, I think that mentioning education is worth a lot more then pointing out: "Hey we've got our mathlib, which contains not even half of the stuff contained in other provers stdlibs"</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249698):
<p>If he were to mention mathlib I think he'd do better by talking about the derivative of the size rather than the size.</p>

#### [ Johan Commelin (Sep 03 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249700):
<p>The education thingy is pretty spectacular. And if it is a success, then a successful mathlib is a corollary.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249796):
<p>And in some sense I'd like to take issue with this "maths library too small" comment. So we don't have Godel's incompleteness theorem. But we do have schemes and hence we have stuff taught at MSc level in a normal mathematics department. And soon we'll have perfectoid spaces and hence we will have stuff taught at PhD level in a strong mathematics department. I would be interested to see a list of topics which are in other theorem provers and which are introduced only at beginning graduate student level in a strong mathematics department in a mainstream (i.e. geometry, number theory, topology, algebra, analysis) course.</p>

#### [ Mario Carneiro (Sep 03 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249850):
<blockquote>
<p>External contributors can prove the new compiler is correct</p>
</blockquote>
<p>See, he did mention me</p>

#### [ Kevin Buzzard (Sep 03 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249853):
<p>Leo told me I need to go into schools. He is really serious about the idea. I have one school talk in my calendar in October and I will almost certainly be doing another one before the end of the year.</p>

#### [ Mario Carneiro (Sep 03 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133249967):
<p>also, he's revealing quite a bit about lean 4 internals stuff, like the new lean IR. This is the first public appearance of it, so I guess he thinks it's pretty stable at this point</p>

#### [ Simon Hudon (Sep 03 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133267963):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think of the promise of better support for proofs by reflection?</p>

#### [ Mario Carneiro (Sep 03 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133278854):
<p>I think it's great. Jeremy and I have talked before about an analogue to Coq's <code>vm_compute</code>, i.e. using <code>#eval</code> to prove theorems. This is sorely needed in many places, i.e. you can easily prove primality of 10 digit numbers using <code>#eval</code> but it is nearly impossible to use the decidable instance in the kernel. Obviously using <code>#eval</code> to prove things means that your trusted code base must include the entire compiler and associated things, but lean 4 is opening up the possibility of proving that all correct anyway, plus even an unverified computation is far more trustworthy than a human calculation, so I'm not particularly worried about inconsistency.</p>

#### [ Mario Carneiro (Sep 03 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133279277):
<p>One thing you can do today to emulate <code>vm_compute</code> is to normalize a term in the VM, then assert the equality as an axiom or use sorry. This has some obvious downsides though, since you can exploit these axioms to prove false things if you circumvent the tactic, i.e. it's not really checked for correctness. Doing this inside Lean would prevent the possibility for exploitation outside bugs in lean itself.</p>

#### [ Simon Hudon (Sep 04 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Leo%27s%20slides%20on%20Lean%204/near/133290558):
<p>What worries me is that if we use this kind of feature, we may not have a choice to trust a lot of software. If one of our libraries use it, everything downstream won't be able to check using a small kernel</p>


{% endraw %}

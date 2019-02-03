---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/25068quadraticreciprocity.html
---

## Stream: [maths](index.html)
### Topic: [quadratic reciprocity](25068quadraticreciprocity.html)

---


{% raw %}
#### [ Kevin Buzzard (May 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919765):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Did you prove Fermat's Little Theorem <a href="https://en.wikipedia.org/wiki/Fermat%27s_little_theorem" target="_blank" title="https://en.wikipedia.org/wiki/Fermat%27s_little_theorem">https://en.wikipedia.org/wiki/Fermat%27s_little_theorem</a> in Lean? I am interested in proving Euler's Criterion <a href="https://en.wikipedia.org/wiki/Euler%27s_criterion" target="_blank" title="https://en.wikipedia.org/wiki/Euler%27s_criterion">https://en.wikipedia.org/wiki/Euler%27s_criterion</a> and Gauss' Lemma <a href="https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)" target="_blank" title="https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)">https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)</a> in Lean, with a view to proving when -1 and +-2 are squares mod p (this is related to quadratic reciprocity).</p>

#### [ Kevin Buzzard (May 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919774):
<p>Is anything like that there already? Do we know the integers mod p are a field?</p>

#### [ Kevin Buzzard (May 01 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919786):
<p>What are good mathlib files to look at?</p>

#### [ Kevin Buzzard (May 01 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125920424):
<p>Oh I have it in Xena in M1F ;-)</p>

#### [ Kevin Buzzard (May 01 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125920427):
<p>That's handy :-)</p>

#### [ Kevin Buzzard (May 01 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125924429):
<p>Are the finite rings Z/nZ in Lean? I thought a bit about how to define them and decided that constructing the quotient of Z by the equivalence relation of being congruent mod n would be a really painless way to do it because all the lemmas would probably already be there. I found many of them all for nat in <code>modeq</code> but to avoid kerfuffle with <code>neg</code> I thought that Z would be better. How much of this stuff is already done?</p>

#### [ Reid Barton (May 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125925147):
<p>There is <code>data.int.modeq</code> now, too</p>

#### [ Kevin Buzzard (May 01 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125926213):
<p>Oh perfect! Many thanks.</p>

#### [ Chris Hughes (May 01 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125932072):
<p>I did get started on defining integers mod n. My effort is here. Some of the proofs are unfinished <a href="https://github.com/dorhinj/lean/blob/master/Zmod.lean" target="_blank" title="https://github.com/dorhinj/lean/blob/master/Zmod.lean">https://github.com/dorhinj/lean/blob/master/Zmod.lean</a></p>

#### [ Chris Hughes (May 01 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125932130):
<p>I thought it would probably be better to define this stuff in a general ring / euclidean domain, not just integers, especially after I ran into a load of trouble converting xgcd from nats into ints.</p>

#### [ Johan Commelin (May 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933136):
<p>You mean that you want to define "ring mod ideal" in general? Or just "ring mod n"?</p>

#### [ Kenny Lau (May 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933272):
<blockquote>
<p>You mean that you want to define "ring mod ideal" in general? Or just "ring mod n"?</p>
</blockquote>
<p>ring mod n doesn't make much sense in general, I think</p>

#### [ Mario Carneiro (May 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933274):
<p>Sure it does, (n) is an ideal</p>

#### [ Kenny Lau (May 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933275):
<p>but not a special one</p>

#### [ Kenny Lau (May 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933281):
<p>n is as special as other elements in the ring</p>

#### [ Mario Carneiro (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933324):
<p>I've been thinking about how to unify this idea with my idea for Z/nZ as fin n with better operations. I think the best option is just to keep the developments separate (ish), with a provable isomorphism Z/nZ -&gt; Z mod (n) where (n) is the ideal generated by n</p>

#### [ Chris Hughes (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933327):
<p>Didn't you do it in a general ring Kenny?</p>

#### [ Kenny Lau (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933328):
<p>indeed</p>

#### [ Chris Hughes (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933333):
<p>Why not PR it?</p>

#### [ Kenny Lau (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933334):
<p>reasons</p>

#### [ Mario Carneiro (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933335):
<p>For similar reasons to <code>rat</code>, I would not want Z/nZ to be a quotient when doing computations. This would make stuff like <code>a^k : Z/nZ</code> far too expensive</p>

#### [ Kenny Lau (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933336):
<p>(it will just be an interface of <code>linear_algebra.quotient_module</code> and <code>ring_theory.ideal</code>)</p>

#### [ Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933375):
<p>It's not completely trivial, you have to take a ring as a module over itself and then quotient by the ideal construed as a submodule</p>

#### [ Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933380):
<p>and then convert back to a ring</p>

#### [ Kenny Lau (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933381):
<p>right</p>

#### [ Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933383):
<p>The theorems are probably easy specializations of existing theorems, but I think the specialization is worthwhile</p>

#### [ Kenny Lau (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933422):
<p>so are you saying I should build the interface?</p>

#### [ Mario Carneiro (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933423):
<p>right</p>

#### [ Mario Carneiro (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933424):
<p>make it so users don't have to think about modules for ring theory</p>

#### [ Kenny Lau (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933426):
<p>:)</p>

#### [ Kevin Buzzard (May 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125950166):
<blockquote>
<p>n is as special as other elements in the ring</p>
</blockquote>
<p>n is one of the elements you can guarantee is there in every ring, so it's special in some sense.</p>

#### [ Kenny Lau (May 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125950172):
<p>ah, you're on about the universal ring business again</p>


{% endraw %}

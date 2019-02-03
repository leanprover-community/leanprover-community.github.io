---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98536reducible.html
---

## Stream: [general](index.html)
### Topic: [@[reducible]](98536reducible.html)

---


{% raw %}
#### [ Kenny Lau (Apr 01 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124484786):
<p>When should I use <code>@[reducible] def</code> and when to just use <code>def</code>?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493291):
<p><code>ge</code> is tagged <code>reducible</code>, because I don't want to double the amount of theorems I have about inequalities</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493292):
<p>I just want <code>a ge b</code> to unfold to <code>b le a</code> as soon as possible</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493333):
<p>so whenever the elaborator or whatever runs into <code>ge</code> it should just think "that's notation for <code>le</code> and I will just unfold it right here and now"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493341):
<p>"because then stuff like <code>rw</code> will work better, I will be able to rw theorems about <code>le</code> in terms involving <code>ge</code>"</p>

#### [ Sebastian Ullrich (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493393):
<p>Which doesn't work because <code>rw</code> and <code>simp</code> match the term head literally</p>

#### [ Simon Hudon (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493485):
<p>What if you use <code>abbreviation</code> instead of <code>@[reducible]</code>?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493488):
<p>oh yes I remember this being a problem with rw!</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493494):
<p>There was maybe even some issue about this.</p>

#### [ Sebastian Ullrich (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493784):
<blockquote>
<p>What if you use <code>abbreviation</code> instead of <code>@[reducible]</code>?</p>
</blockquote>
<p><code>abbreviation</code> is <code>@[reducible]</code> + a kernel reducibility annotation, which you can most likely ignore. So use <code>abbreviation</code> if you like it more than <code>@[reducible] def</code>.</p>

#### [ Kenny Lau (Apr 01 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493830):
<p>what will happen if I just make everything reducible?</p>

#### [ Kenny Lau (Apr 01 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493831):
<p>when is <code>@[reducible]</code> not desired?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494193):
<p>I think you have problems with readability after a while</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494195):
<p>You define an exciting new thing and mark it reducible</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494196):
<p>and want to prove basic lemmas about it</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494199):
<p>but the moment Lean does anything with it, it unfolds the definition</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494205):
<p>and it's then harder to use because you have to keep folding it up again when you want to apply the previous lemma</p>

#### [ Kenny Lau (Apr 03 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558714):
<p>Should I make these reducible?</p>
<div class="codehilite"><pre><span></span>def orbit : set X :=
{ y | ∃ g : G, g • x = y }

def stab : set G :=
{ g | g • x = x }
</pre></div>

#### [ Mario Carneiro (Apr 03 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558770):
<p>the answer is almost always no</p>

#### [ Mario Carneiro (Apr 03 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558782):
<p>instead, you should have a simp lemma that says <code>g \in stab x &lt;-&gt; g \bu x = x</code></p>

#### [ Kenny Lau (Apr 03 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558783):
<p>aha</p>


{% endraw %}

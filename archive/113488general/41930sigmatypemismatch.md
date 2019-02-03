---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41930sigmatypemismatch.html
---

## Stream: [general](index.html)
### Topic: [sigma type mismatch](41930sigmatypemismatch.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 26 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220067):
<p><code>stalk2</code> below doesn't typecheck:</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220112):
<div class="codehilite"><pre><span></span>universe u
variables (X : Type u) (P : set (set X))

definition  stalk1 (x : X) :=
Σ U : {U : set X // x ∈ U ∧ P U}, ℕ

definition  stalk2 (x : X) :=
Σ (U : set X) (Hx : x ∈ U) (PU : P U), ℕ
</pre></div>

#### [ Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220122):
<p>red squiggle is on the sigma in stalk2</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220123):
<p>error is</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220124):
<div class="codehilite"><pre><span></span>type mismatch at application
  Σ (PU : P U), ℕ
term
  λ (PU : P U), ℕ
has type
  P U → Type : Type 1
but is expected to have type
  ?m_1 → Type : Type (max ? 1)
</pre></div>

#### [ Kevin Buzzard (Mar 26 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220146):
<p>I <em>think</em> that I would rather work with stalk2 rather than stalk1</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220163):
<p>because I tend to avoid subtypes if I can</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220167):
<p>I am still a bit scared of all the up-arrows</p>

#### [ Kevin Buzzard (Mar 26 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220282):
<p>[background : X is a topological space, P is a basis for the open sets, I'm defining the stalk of a presheaf <a href="https://stacks.math.columbia.edu/tag/009H" target="_blank" title="https://stacks.math.columbia.edu/tag/009H">https://stacks.math.columbia.edu/tag/009H</a> just after 6.30.1; here's a special case <a href="https://stacks.math.columbia.edu/tag/0078" target="_blank" title="https://stacks.math.columbia.edu/tag/0078">https://stacks.math.columbia.edu/tag/0078</a> which in Lean currently looks like <a href="https://github.com/kbuzzard/lean-stacks-project/blob/16a88206397eaa664dd00cf917c78359b7119cb3/src/tag0078.lean#L9" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/16a88206397eaa664dd00cf917c78359b7119cb3/src/tag0078.lean#L9">https://github.com/kbuzzard/lean-stacks-project/blob/16a88206397eaa664dd00cf917c78359b7119cb3/src/tag0078.lean#L9</a> ]</p>

#### [ Chris Hughes (Mar 26 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124221257):
<p>Sigma only takes two arguments. Also the type of nat doesn't depend on the set, so you may as well use prod.</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124221456):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> It's desugared to nested sigmas. But it still doesn't typecheck because <code>P U</code> does not live in <code>Type _</code>. I would suggest using structures in favor of nested anything.</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222122):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  -- the actual type I want to make is  more complex -- the nat was just a MWE of my problem. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I need to make a type because I am actually interested in a quotient of the type I'm trying to construct. Your observation is that this doesn't typecheck either:</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222127):
<p><code> definition  stalk2 (x : X) (U : set X) (Hx : x ∈ U) := Σ (PU : P U), ℕ</code></p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222139):
<p>and I don't really understand why.</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222146):
<p>But at the end of the day</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222187):
<p>I would like some sigma type so I can put an equivalence relation on it and form the quotient type.</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222207):
<p>Are you suggesting I stick with the <code>stalk1</code> approach?</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222271):
<p>Presumably you prefer <code>A -&gt; B -&gt; C</code> to <code>A and B -&gt; C</code>, i.e. here we avoid the structure [not subtype -- sorry] and prefer the "nested" approach?</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222300):
<p>No, I'm suggesting</p>
<div class="codehilite"><pre><span></span>structure stalk3 (x : X) :=
(U : set X) (Hx : x ∈ U) (PU : P U) (n : ℕ)
</pre></div>


<p>so that you don't have to worry about every component whether it should be a sigma or a prod or a pprod or ... and on top of that you get projections with meaningful names.</p>

#### [ Kevin Buzzard (Mar 26 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124223706):
<p>Oh, I see: and then this is still a type so I can still put an equivalence relation on it. I will try it this way! Thanks!</p>

#### [ Kenny Lau (Mar 26 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124230980):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> have you tried it? (if not, i’ll do it)</p>

#### [ Kevin Buzzard (Mar 26 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231051):
<p>No, I've been at meetings until recently and since then I've been talking to Chris about rings</p>

#### [ Kenny Lau (Mar 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231262):
<p>I’ll do it when i get back home then</p>

#### [ Kenny Lau (Mar 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231264):
<p>which will happen in 15 minutes</p>

#### [ Kevin Buzzard (Mar 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231348):
<p>I pushed as far as I got. Thanks.</p>


{% endraw %}

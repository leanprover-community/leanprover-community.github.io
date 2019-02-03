---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53623metauniverses.html
---

## Stream: [general](index.html)
### Topic: [meta + universes](53623metauniverses.html)

---


{% raw %}
#### [ Reid Barton (Sep 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133974969):
<p>Could/should <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> allow <code>meta</code> to break "universe safety", e.g., stick a field of type <code>Type</code> inside a structure declared to have type <code>Type</code>?</p>

#### [ Reid Barton (Sep 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133975221):
<p>To support things like existential types in Haskell</p>

#### [ Sebastian Ullrich (Sep 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133975646):
<p>It's not a bad idea. We have discussed it before, but there are some issues in the details. For example, we would still like to distinguish between values and proofs in the compiler. Anyway, you should be able to define existential types in meta Lean 3 using a generalized version of <code>unchecked_cast</code> that can cast between universes</p>

#### [ Mario Carneiro (Sep 14 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133980222):
<p>Ah, this is a nice idea, I hadn't thought about using <code>unchecked_cast</code> to enable universe casting. I'll add an interface for this in mathlib</p>

#### [ Mario Carneiro (Sep 14 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133980318):
<p>I think that the best way to enable this kind of thing in meta land without having a whole different language is to do all universe checks as normal, but drop the check on maximum universe levels for <code>meta inductive</code>s</p>

#### [ Mario Carneiro (Sep 14 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133980377):
<p>so it would still generate the same recursors as normal, but if the type is supposed to be <code>Type 3</code> and you say <code>Type 1</code> instead then that's okay</p>

#### [ Sebastian Ullrich (Sep 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/133980492):
<p>Right, we discussed that before but never followed up on it <a href="https://github.com/leanprover/lean/pull/1580#issuecomment-301203751" target="_blank" title="https://github.com/leanprover/lean/pull/1580#issuecomment-301203751">https://github.com/leanprover/lean/pull/1580#issuecomment-301203751</a></p>

#### [ Mario Carneiro (Sep 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003123):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Whoa, this was not expected. Not only does the advertised method not work, but I think I can prove there is no workaround, that is, VM evaluation respects universes! This means that something like universe inconsistent inductives may be the only way to make this work.</p>

#### [ Kenny Lau (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003181):
<p>can we define a function that sends <code>u : nat</code> to <code>Type u</code>?</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003182):
<p><code>u : nat</code> does not typecheck</p>

#### [ Kenny Lau (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003185):
<p>not even in the unsafe level?</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003190):
<p>they are not the same thing</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003192):
<p>levels and natural numbers are completely different, syntactically</p>

#### [ Kenny Lau (Sep 15 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003257):
<p>where is <code>max</code> defined?</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003296):
<p>nowhere, it's primitive</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20%2B%20universes/near/134003307):
<p>Basically, <code>unchecked_cast</code> works by casting across a sorried proof of type equality, which is erased by the VM so that the equality recursor just steps directly from one type to another, and hopefully the VM representations match up so this makes sense. But the equality can only go between two elements of the same universe, and similarly with heq. Indeed, if you look at the recursor of any inductive, it has a motive that lands in <code>Type l</code> for some fixed <code>l</code>, and you can only move from one place to another along this family, meaning you can never escape <code>Type l</code> by application of this recursor.</p>


{% endraw %}

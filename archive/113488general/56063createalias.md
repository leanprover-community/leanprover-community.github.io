---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56063createalias.html
---

## Stream: [general](index.html)
### Topic: [create alias](56063createalias.html)

---


{% raw %}
#### [ Zesen Qian (Aug 17 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309111):
<p>How can I create an alias to anther declaration? Say, in my namespace <code>foo</code> I want to create a <code>true</code> such that users can see <code>foo.true</code> and the prover treats it equally to <code>true</code> from core.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309539):
<p>equally is hard, but there are a few ways to get close</p>

#### [ Zesen Qian (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309551):
<p>right now I'm thinking about <code>def</code> with <code>attribute [reducible]</code></p>

#### [ Mario Carneiro (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309556):
<p><code>@[reducible] def</code> makes <code>rw</code> and <code>simp</code> see through the definition, as well as typeclass inference</p>

#### [ Zesen Qian (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309559):
<p>I guess that should work, but really I'm looking for shorter path.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309566):
<p><code>abbreviation</code> does something similar with kernel reduction, I'm not sure exactly</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309572):
<p>what do you mean "shorter path"?</p>

#### [ Zesen Qian (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309578):
<p>I mean, less characters to type.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309584):
<p>alias true = true would be the best.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309623):
<p>mathlib has an <code>alias</code> tactic, but it doesn't set <code>reducible</code></p>

#### [ Mario Carneiro (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309646):
<p>what's wrong with just <code>def true := true</code>?</p>

#### [ Chris Hughes (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309652):
<p><code>notation</code>?</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309684):
<p>also, what is your use case? I wrote <code>alias</code> to support alias constructions but it doesn't get much use since I specifically try to avoid aliases</p>

#### [ Zesen Qian (Aug 17 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309741):
<p>I need something in my namespace that's definitionally equal to <code>true</code></p>

#### [ Zesen Qian (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309775):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I haven't used notation before, can you give an example?</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309783):
<p><code>def true := true</code> is the easiest way to accomplish that</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309796):
<p><code>notation `true'` := true</code></p>

#### [ Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309850):
<p>but notation is not a def</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309857):
<p>so there will be no <code>foo.true'</code> that way</p>

#### [ Zesen Qian (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309863):
<p>yeah, I realize that.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309876):
<p>ok, so the best way is <code>reducible</code> <code>def</code>.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309877):
<p>but you still haven't said why you need this</p>

#### [ Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309894):
<p>I'm doing some metaprogramming. A proof given by SMT solvers is mapped to a proof in lean.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309899):
<p>so a <code>true</code> in source proof mapped to <code>true</code> in lean.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309904):
<p>then just map to the real <code>true</code></p>

#### [ Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309912):
<p>I have a file containing all stuff that source proofs will refer.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309960):
<p>so I don't need to write the mapping myself. The meta program will look it up itself.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309992):
<p>but then your output statements will just be needlessly encoded with reducible defs</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310001):
<p>you are writing the mapping just by giving these defs</p>

#### [ Zesen Qian (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310021):
<p>yeah, but that's not big problem, no one is gonna read the proof as long as it's correct.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310024):
<p>machine generated proofs are never intended for people.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310070):
<p>heh, you would be surprised</p>

#### [ Zesen Qian (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310081):
<p>I hope I will never be suprised.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310090):
<p>anyway, I'm going <code>reducible</code> <code>def</code>s.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310128):
<p>I don't think there is any point in using reducible here though. if it's in the proof term it's in the proof term</p>

#### [ Zesen Qian (Aug 17 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310183):
<p>I don't know what you meant.</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310184):
<p>you aren't using it with rw or anything so it won't be unfolded</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310330):
<p>if you put together a proof using these variant definitions, it will make no difference to the type-correctness as long as it's defeq, and a regular def accomplishes that</p>

#### [ Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310459):
<p>I think you are right.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310460):
<p>I can now get it work without reducible, but I will see it can keep working.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310466):
<p>yeah, but I'm thinking about if the user provides me with the "real" <code>true</code>.</p>

#### [ Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310486):
<p>and when a proof depends on the definitional equality between these two <code>true</code>, will that still work?</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310563):
<p>yes, that's what defeq does</p>

#### [ Zesen Qian (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310571):
<p>ok then!</p>

#### [ Mario Carneiro (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310576):
<p>you can replace <code>true</code> with <code>true'</code> anywhere in the proof with no changes</p>

#### [ Zesen Qian (Aug 17 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310605):
<p>ok. I guess I overlooked lean's ability of identifying equalities.</p>


{% endraw %}

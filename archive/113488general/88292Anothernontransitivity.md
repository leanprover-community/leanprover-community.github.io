---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88292Anothernontransitivity.html
---

## Stream: [general](index.html)
### Topic: [Another non-transitivity](88292Anothernontransitivity.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 02 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123163815):
<p>While trying to prove that lean doesn't have any other sources of definitional non-transitivity besides K-like eliminators, I discovered another one, quotients of propositions:</p>
<div class="codehilite"><pre><span></span>variables (α : Prop) (r : α → α → Prop) (β : Sort*)
  (f : α → β) (H : Π (a b : α), r a b → f a = f b) (a : α)
example : quot.lift f H (quot.mk r a) = f a := rfl
example (h : quot r) : quot.lift f H h = quot.lift f H (quot.mk r a) := congr rfl rfl
example (h : quot r) : quot.lift f H h = f a := sorry
</pre></div>

#### [ Mario Carneiro (Mar 02 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123163882):
<p>Note that a quotient of a proposition is always useless, because propositions are already subsingletons. Maybe we should just make <code>quot</code> always live in <code>Type</code>, even if the input is a <code>Prop</code>?</p>

#### [ Simon Hudon (Mar 02 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164192):
<p>What do we gain by doing that?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164194):
<p>doing what</p>

#### [ Simon Hudon (Mar 02 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164234):
<p>Putting <code>quot</code> in <code>Type</code> even when the input is a <code>Prop</code></p>

#### [ Mario Carneiro (Mar 02 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164242):
<p>The source of non-transitivity is when the major premise of an iota rule is a proof, while the resulting type is a <code>Type</code></p>

#### [ Mario Carneiro (Mar 02 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164248):
<p>This happens exactly when the inductive type is a <code>Prop</code> but it "large eliminates"</p>

#### [ Simon Hudon (Mar 02 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164293):
<p>Is the kind of price that you pay only when you're in that situation?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164295):
<p>And <code>quot p</code> acts like a large eliminator in this case because <code>lift</code> has target <code>Type</code></p>

#### [ Mario Carneiro (Mar 02 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164305):
<p>The issue is that you can arbitrarily muck with the major premise and extract data from it even though it's a prop</p>

#### [ Simon Hudon (Mar 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164351):
<p>A bit as if your the <code>quot</code> framework acted as an axiom of choice?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164355):
<p>Any other time it's not a problem - if the type itself is in <code>Type</code> then the major premise is not subject to proof irrelevance, and if it is a small eliminator then anything that results will also be subject to proof irrelevance</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164375):
<p>It's not quite axiom of choice level, because large elimination is only sound in the first place when there is exactly one thing that can be in the major premise... but that's only up to definitional equality and there are potentially many ways to write it</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164377):
<p>This is where undecidability of defeq arises</p>

#### [ Simon Hudon (Mar 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164426):
<p>The thing I'm worried about is if you build something on top of <code>quot</code> and you need functions of type <code>Sort u -&gt; Sort u</code>, putting <code>quot</code> in <code>Type</code> may require you to have complicated universe expressions and force you to deal with types that live in different universes.</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164432):
<p>For example, consider the definitional equality <code>quot.lift f H h = f a</code> in the example above. Where would it get <code>a</code> from to perform that reduction?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164436):
<p>It's a proof, so it is "unique"... but that doesn't make the problem easier</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164477):
<p>The other alternative, which was actually in use for a while, is to have <code>quot : Type u -&gt; Type u</code> like so many other things</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164479):
<p>I think it was generalized to Sort because no one saw any harm in it</p>

#### [ Simon Hudon (Mar 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164526):
<p>Yeah I see. I find myself siding with <code>Type u -&gt; Type u</code>. I wonder if that rules out anything useful</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164532):
<p>You can recover <code>quot</code> on <code>Sort</code>, without quite as many definitional rules, by simply using <code>quot (plift p)</code></p>

#### [ Simon Hudon (Mar 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164583):
<p>Oh nice! I like that. In the general case, <code>quot</code> is cheap (from a design perspective) and you only pay a price for exotic uses</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164591):
<p>I think I would prefer <code>quot : Sort u -&gt; Sort (max 1 u)</code> since it is the axiomatic one, and <code>quotient : Type u -&gt; Type u</code>. This should avoid most universe unification problems</p>

#### [ Simon Hudon (Mar 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164594):
<p>Yeah, you're right</p>

#### [ Simon Hudon (Mar 02 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164633):
<p>Just to be sure. You're saying that this example demonstrate undecidability of defeq. Does that mean that the current type checker does not terminate on this example?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164639):
<p>No, the current typechecker does not accept those definitional equalities</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164640):
<p>even though they are composed from acceptable definitional equalities</p>

#### [ Simon Hudon (Mar 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164684):
<p>Right but it is a known state of affair that definitional equalities are not transitive, no?</p>

#### [ Mario Carneiro (Mar 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164690):
<p>Right, hence "another non-transitivity"</p>

#### [ Simon Hudon (Mar 02 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164732):
<p>What I'm asking is why do we need to avoid this one?</p>

#### [ Mario Carneiro (Mar 02 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164854):
<p>Because it is preferable to have a reasonable story for how defeq works and to only break it with good reason. (Full disclosure: this is also going to add another page to my paper, for a dumb edge case that I am positive is currently completely unused)</p>

#### [ Mario Carneiro (Mar 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164894):
<p>In fact, I've even had conversations discussing putting <code>acc</code> in Type to avoid exactly this problem, and that's a much bigger deal</p>

#### [ Simon Hudon (Mar 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164895):
<p>(About the disclosure: are you telling me that you're being paid by the big definitional equality industry?)</p>

#### [ Mario Carneiro (Mar 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164902):
<p>I guess I am, in a way...</p>

#### [ Simon Hudon (Mar 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164904):
<p>What's the consequence of putting <code>acc</code> in Type?</p>

#### [ Mario Carneiro (Mar 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123169571):
<p>Again, it eliminates issues caused by large elimination. If <code>acc</code> was in Type and <code>quot</code> was in type, then definitional equality would be decidable, transitive, all that good stuff</p>

#### [ Gabriel Ebner (Mar 02 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123174245):
<p>I had already submitted a PR to move <code>acc</code> into <code>Type</code> once: <a href="https://github.com/leanprover/lean/pull/1803" target="_blank" title="https://github.com/leanprover/lean/pull/1803">https://github.com/leanprover/lean/pull/1803</a>  But of course it got rejected.  The comments on the PR are an interesting read, though.</p>

#### [ Gabriel Ebner (Mar 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123174616):
<p>Just if anybody else wondered, <code>congr rfl rfl</code> in the original post is definitionally equal to <code>rfl</code>.  And if I see this correctly, my PR would not fix this issue.</p>

#### [ Sean Leather (Mar 02 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175304):
<p><a href="https://github.com/leanprover/lean/pull/1803#issuecomment-325014390" target="_blank" title="https://github.com/leanprover/lean/pull/1803#issuecomment-325014390">https://github.com/leanprover/lean/pull/1803#issuecomment-325014390</a> :</p>
<blockquote>
<p>If "several people" == @digama0, then it doesn't count :)</p>
</blockquote>
<p>Ouch! <span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Patrick Massot (Mar 02 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175720):
<p>Yes, I'm very worried by that paper <span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> is writing. I don't  understand anything about type theory but, to me, it sounds like Mario is scientifically documenting some weakness of Lean (which is irrelevant to end users and doesn't allow to prove false). In principle this is fair. But is it a smart diplomatic move? How could that improve the little "communication issue"?</p>

#### [ Patrick Massot (Mar 02 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175872):
<p>I have a recurrent question: should I learn what "subsingleton" means? If yes, where?</p>

#### [ Chris Hughes (Mar 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175881):
<p>Subsingleton just means a type with 0 or 1 elements</p>

#### [ Patrick Massot (Mar 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175888):
<p>I understand that bit. It doesn't explain why it comes up all the time, always with "elimination" in the same neighborhood</p>

#### [ Simon Hudon (Mar 02 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175932):
<p>In the context of Lean, that includes any <code>Prop</code>. I believe it's a generalization of proof irrelevance.</p>

#### [ Simon Hudon (Mar 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175944):
<p>When checking if two terms are the same, you ignore proof terms and you can ignore subsingleton types.</p>

#### [ Patrick Massot (Mar 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175985):
<p>I see</p>

#### [ Patrick Massot (Mar 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175987):
<p>Thanks</p>

#### [ Gabriel Ebner (Mar 02 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178245):
<p><span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span> That's just proof irrelevance.  <span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> Subsingleton is a type with at most one element (we have the subsingleton type class for that).  Subsingleton elimination is something slightly different: usually, inductive data types in Prop only allow you to eliminate into Prop.  For example, the recursor for ∃ only allows you to obtain propositions, if you could eliminate into Type, then you could extract the witness and thereby prove choice.  Subsingleton elimination is now a relaxation of this restriction: in some cases it is perfectly sound for the recursor of an inductive proposition to eliminate into Type: intuitively, if you don't get any additional "data" when eliminating (such as constructor arguments that are in Type, or which constructor of the inductive proposition is used).  For example, ∧, false, true, all eliminate into Type.</p>

#### [ Patrick Massot (Mar 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178735):
<p>Thanks for your explanation but I'm afraid I'm missing too much background. Can you explain what "∧  eliminate into Type" means? Maybe with an example? I know about <code>and.elim</code> but I don't see any Type here, only Prop.</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178810):
<blockquote>
<p>Thanks for your explanation but I'm afraid I'm missing too much background. Can you explain what "∧  eliminate into Type" means? Maybe with an example? I know about <code>and.elim</code> but I don't see any Type here, only Prop.</p>
</blockquote>
<p>look at <code>and.rec</code></p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178860):
<p>Compare with <code>Exists.rec</code> [sorry, typo fixed]</p>

#### [ Gabriel Ebner (Mar 02 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123179178):
<p>Example:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- and eliminates into Type, this means that in the</span>
<span class="c1">-- recursor we can return values e.g. of type nat : Type</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">and</span><span class="bp">.</span><span class="n">rec</span> <span class="n">true</span> <span class="n">true</span> <span class="bp">ℕ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="mi">5</span><span class="o">)</span> <span class="bp">⟨⟨⟩</span><span class="o">,</span><span class="bp">⟨⟩⟩</span>

<span class="c1">-- however Exists does not eliminate into Type (just</span>
<span class="c1">-- into Prop), we cannot return values of type nat : Type,</span>
<span class="c1">-- just propositions</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">Exists</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">true</span><span class="o">)</span> <span class="bp">ℕ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">witness</span> <span class="n">h</span><span class="o">,</span> <span class="mi">5</span><span class="o">)</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">trivial</span><span class="bp">⟩</span>
             <span class="c1">-- could use witness here, so forbidden ^</span>
</pre></div>


<p>The second example fails, since nat is not in Prop.</p>

#### [ Patrick Massot (Mar 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123180791):
<p>Thank you very much. I was confused by the type of <code>and.elim</code>. Since it only wraps <code>and.rec</code>, why do we have a different type here?</p>

#### [ Gabriel Ebner (Mar 02 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123182111):
<p>The <code>.rec</code> one is the one generated by the kernel, and is the only one that matters (for foundational purposes).  I don't know the reason behind the <code>.elim</code> redefinitions, my best guess is that they correspond to the inference rules in natural deduction (which obviously only talk about Prop).</p>

#### [ Simon Hudon (Mar 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123194465):
<p>Thanks for correcting my mistake</p>


{% endraw %}

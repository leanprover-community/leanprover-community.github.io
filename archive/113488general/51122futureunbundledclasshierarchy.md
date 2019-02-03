---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51122futureunbundledclasshierarchy.html
---

## Stream: [general](index.html)
### Topic: [future unbundled class hierarchy](51122futureunbundledclasshierarchy.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 15 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698387):
<p>Sebastian Ullrich said (in the multiset thread)</p>
<blockquote>
<p>Just idle speculation, I suppose in a future unbundled class hierarchy we would rather have an instance <code>is_zero ∅ (multiset a)</code> instead of <code>has_zero (multiset a)</code>?</p>
</blockquote>
<p>Does this say "in Lean 4, the whole type class system is going to change a lot"? </p>
<p>I realised over the last two weeks that mathematicians think "G is a group" is a proposition, but that <code>Hyp : group G</code> is not. Maybe if a mathematician is pushed they might concede that actually it's "the pair <code>(G,*)</code> is a group" which is the proposition, but Lean still wants more (identity and inverse). I guess what I'm saying is that questions from students have made me myself question why things are set up this way.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698439):
<p>The last bit has to do with constructivity in type theory</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698457):
<p>Even if a function is uniquely defined in the relational sense, it's not quite the same as a function in type theory</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698464):
<p>I thought it might do. So if someone decided to make the fundamental typeclass <code>is_group</code> we'd end up carrying around all three things (mul, inv, identity)</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698510):
<p>So while in ZFC it suffices to have (G,*) since 1 is unique, in lean you really want a concrete witness to this</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698514):
<p>What about making <code>G</code> plus <code>mul</code> + <code>inv</code> + <code>1</code> into a structure, and making <code>is_group</code> a propositional typeclass?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698516):
<p>In classical lean, you can nevertheless define 1 from * if you wanted, but its definitional reductions won't be great</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698524):
<p>I'm just trying to question the way we do it, not because of groups, but because of diamonds in general. Presumably if every typeclass was a Prop the diamond problems would go away</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698526):
<p>That option has been discussed (<code>group_struct</code> plus <code>is_group</code>)</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698572):
<p>My response is, if <code>group_struct</code> isn't useful on its own it's not worth the definition</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698575):
<p>I was wondering whether Sebastian's comments meant that some changes would be implemented</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698582):
<p>if every interesting <code>group_struct</code> is also a group then it may as well be bundled in the definition</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698584):
<p>Remember there were problems with product of metric / top spaces (which I think were solved) and problems with modules over rings (which I think were not)</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698590):
<p>Can this sort of approach be used to solve them?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698596):
<p>Sebastian's comments relate to Leo's plans with the new algebraic hierarchy</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698597):
<p>If every interesting <code>group_struct</code> were a group, but this caused problems later down the line, then this would be an argument for not bundling.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698598):
<p>i.e. the <code>@[algebra]</code> classes</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698601):
<p>that's a rather vague worry</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698602):
<p>Where do I read about Leo's plans and the <code>@[algebra]</code> classes?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698641):
<p>there's a wiki page for it</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698644):
<p><a href="https://github.com/leanprover/lean/wiki/Refactoring-structures" target="_blank" title="https://github.com/leanprover/lean/wiki/Refactoring-structures">https://github.com/leanprover/lean/wiki/Refactoring-structures</a></p>

#### [ Mario Carneiro (Jul 15 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698654):
<p>I remain skeptical. I will wait for Leo's implementation before considering anything along these lines</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698667):
<p>So here we are just waiting to see what happens in Lean 4 and then we go with whatever changes get made?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698695):
<p>pretty much</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698698):
<p>it's not like there is any other option</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698699):
<p>I thought that another vague plan was to get a whole bunch of maths out of core Lean</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698703):
<p>I believe that will happen as well</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698706):
<p>and then it's up to mathlib to decide whether it's <code>group</code> or <code>is_group</code></p>

#### [ Mario Carneiro (Jul 15 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698713):
<p>It's possible that changes to <code>simp</code> will necessitate a certain design</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698767):
<p>And it's not just "leo broke today's system", it could just as easily be "Leo's new system is way better and we would be stupid not to use it"</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698819):
<p>I predict that most of the large scale structural changes in mathlib after lean 4 will be done because we want to take advantage of some new feature, not to fix a breaking change</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698841):
<p>I'd seen that wiki page several times before, and my interpretation of it was "it's mostly CS stuff that I don't understand, but it documents an old change to the structure command which was already made"</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698852):
<p>I now think this interpretation might be incorrect -- it might say "even though there is <code>use_old_structure_command</code> or whatever it's called, there are still some things here which are not in Lean and might in the future be in Lean"</p>


{% endraw %}

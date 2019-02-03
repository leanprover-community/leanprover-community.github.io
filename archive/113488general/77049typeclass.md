---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77049typeclass.html
---

## Stream: [general](index.html)
### Topic: [typeclass](77049typeclass.html)

---


{% raw %}
#### [ Kenny Lau (Mar 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761005):
<p>why does this have no problem:</p>
<div class="codehilite"><pre><span></span>class add_comm_monoid (α : Type u) extends add_monoid α, add_comm_semigroup α

class add_group (α : Type u) extends add_monoid α, has_neg α :=
(add_left_neg : ∀ a : α, -a + a = 0)

class add_comm_group (α : Type u) extends add_group α, add_comm_monoid α
</pre></div>


<p>but this gives me an error?</p>
<div class="codehilite"><pre><span></span>class has_upair extends has_zmem α :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)

class has_sUnion extends has_zmem α :=
(sUnion : α → α)
(zmem_sUnion_iff_zmem_zmem : ∀ x z, z ∈ sUnion x ↔ ∃ t, z ∈ t ∧ t ∈ x)

class has_sUnion_upair extends has_sUnion α, has_upair α
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761012):
<p>error:</p>
<div class="codehilite"><pre><span></span>invalid &#39;structure&#39; header, field &#39;to_has_zmem&#39; from &#39;zfc.has_upair&#39; has already been declared
</pre></div>

#### [ Simon Hudon (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761063):
<p>Why isn't <code>α</code> a parameter of <code>has_upair</code> and <code>has_sUnion</code>?</p>

#### [ Kenny Lau (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761069):
<p>oh it's a variable I declared before</p>

#### [ Kenny Lau (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761073):
<p>(sorry for not providing MWE)</p>

#### [ Simon Hudon (Mar 15 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761280):
<p>Ah! I see! This is what is called diamond-shaped inheritance scheme. It causes you to inherit <code>to_has_zmem</code> multiple times which causes it to clash with itself.</p>

#### [ Simon Hudon (Mar 15 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761299):
<p>(C++ programmers also know that as "diamond of death")</p>

#### [ Simon Hudon (Mar 15 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761350):
<p>They have been carefully exorcised from the basic libraries</p>

#### [ Simon Hudon (Mar 15 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761435):
<p>Is there a way to not make <code>has_upair</code> inherit <code>has_zmem</code>?</p>

#### [ Simon Hudon (Mar 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761461):
<p>You could change:</p>
<div class="codehilite"><pre><span></span>class has_upair extends has_zmem α :=
</pre></div>


<p>into</p>
<div class="codehilite"><pre><span></span>class has_upair [has_zmem α] :=
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761472):
<p>then why does the first one work?</p>

#### [ Simon Hudon (Mar 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761601):
<p>Good question. I wonder if that's because <code>add_comm_monoid</code> doesn't have fields. You can basically inline it in the <code>extends</code> clause of <code>add_comm_group</code></p>

#### [ Simon Hudon (Mar 15 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761784):
<p>If that's the case, you maybe could take advantage of it by splitting <code>has_upair</code> in two:</p>
<div class="codehilite"><pre><span></span>class has_upair_1 [has_zmem α] :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)

class has_upair_2 extends has_zmem α,  has_upair  α
</pre></div>


<p>I'm not sure if that would work but it might be worth a try</p>

#### [ Kenny Lau (Mar 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761803):
<div class="codehilite"><pre><span></span>class has_sUnion_upair extends has_zmem α :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)
(sUnion : α → α)
(zmem_sUnion_iff_zmem_zmem : ∀ x z, z ∈ sUnion x ↔ ∃ t, z ∈ t ∧ t ∈ x)

instance has_sUnion_upair.to_has_sUnion [s : has_sUnion_upair α] : has_sUnion α :=
{ ..s }

instance has_sUnion_upair.to_has_upair [s : has_sUnion_upair α] : has_upair α :=
{ ..s }
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761807):
<p>this is what i did</p>

#### [ Simon Hudon (Mar 15 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761870):
<p>The part I don't like about your solution is that I believe it forces you to duplicate the statement of your laws.</p>

#### [ Kenny Lau (Mar 15 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761979):
<p>the part I don't like about your solution is that I would have to have <code>has_zmem</code> as my hypothesis each time</p>

#### [ Simon Hudon (Mar 15 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762005):
<p>No. If you use <code>has_upair_2</code>, it comes with <code>has_zmem</code></p>

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762095):
<p>oh...</p>

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762102):
<p>so your solution is basically like "distrib"</p>

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762106):
<p>create a useless class that only has distributivity</p>

#### [ Simon Hudon (Mar 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762194):
<p>You could say that</p>

#### [ Simon Hudon (Mar 15 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762295):
<p>Actually, useless is not accurate: try commenting it out to see if it's useful</p>

#### [ Kenny Lau (Mar 15 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762354):
<p>I mean <code>distrib</code> is useless in the sense that no mathematician cares about it</p>

#### [ Simon Hudon (Mar 15 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762436):
<p>I think it's still useful. It might not be an interesting structure but for some theorems, you may only care about distributivity without a whole semiring</p>

#### [ Simon Hudon (Mar 15 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762495):
<p>The same theorem or tactics could then be applicable whether you have a semiring or a distributive lattice</p>

#### [ Simon Hudon (Mar 15 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762702):
<p>In the case of my solution, the <code>has_upair_1</code> is more of a coding trick, you're right. I think it happens rarely enough that it's an ugliness we can live with. I would prefer if diamond shaped inheritance was supported properly but it has been ruled out for performance reason</p>

#### [ Mario Carneiro (Mar 15 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123768060):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> The original code works because it is using the old structure command to merge the fields together. People seem to be scared of anything marked "old" though, so if you want to recover this behavior with the new structure command, rather than creating a useless typeclass, you should extend <code>has_upair</code> and restate the axioms of <code>has_sUnion</code>, then construct a parent instance for <code>has_sUnion</code> (or vice versa).</p>

#### [ Kenny Lau (Mar 15 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123769395):
<p>so if I use old structure, everything will work?</p>

#### [ Mario Carneiro (Mar 15 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123769435):
<p>for some value of "everything"</p>

#### [ Kevin Buzzard (Mar 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123770735):
<p>I guess whether or not it will work in Lean 4 is another matter...</p>

#### [ Kevin Buzzard (Mar 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123770925):
<p>I guess the other thing is that presumably there was a reason the structure command was changed. Hmm, they might only be performance-related though.</p>

#### [ Simon Hudon (Mar 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771129):
<p>I think they are. Leo considered the price to be too high despite C++ and Eiffel offering the feature with reasonable performances</p>

#### [ Andrew Ashworth (Mar 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771153):
<p>eh, most large software projects have moved away from large inheritance trees</p>

#### [ Simon Hudon (Mar 15 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771236):
<p>Have they? For performance reasons? I seem to remember it being a bottomless well of bugs in C++ because the design is kind of dumb. As far as I know, the feature is still in use in Eiffel code bases</p>

#### [ Andrew Ashworth (Mar 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771293):
<p>not for performance, but because most people do inheritance wrong. this is the feeling i get from the places i've worked at with large code-bases</p>

#### [ Andrew Ashworth (Mar 15 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771351):
<p>if you asked most people what the liskov substitution principle was they'd cross their eyes and wonder what you'd had for breakfast</p>

#### [ Andrew Ashworth (Mar 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771426):
<p>well, that's a bit unfair, LSP is a bit jargon-ny, but the point is, it's easy to shoot yourself in the foot with misuse of inheritance</p>

#### [ Simon Hudon (Mar 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123772124):
<p>I think that's one reason Eiffel got inheritance right. Have you ever used it?</p>


{% endraw %}

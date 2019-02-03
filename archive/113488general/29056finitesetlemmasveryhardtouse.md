---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29056finitesetlemmasveryhardtouse.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [finite set lemmas very hard to use](https://leanprover-community.github.io/archive/113488general/29056finitesetlemmasveryhardtouse.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127169799):
<p>A lot of the finite set lemmas are extremely difficult to use. For example <code>set.empty_card</code> can only be used in a rewrite, if I've used <code>fintype_empty</code> as my <code>fintype</code> instance in my goal. Would it be a good idea to make fintype instances an argument to the lemma whenever they're used in the statement of a theorem?</p>

#### [ Kevin Buzzard (May 27 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170886):
<p>You mean instead of using the type class resolution system?</p>

#### [ Kevin Buzzard (May 27 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170892):
<p>Let me just comment that if I've understood your question correctly then I had the same problems using the <code>is_ring_hom</code> typeclass and it seemed to me initially that by far the easiest fix was just to make it not a typeclass</p>

#### [ Kevin Buzzard (May 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170897):
<p>but instead I started that typeclass woes thread, and every time I got stuck or frustrated, Mario explained how to do it</p>

#### [ Kevin Buzzard (May 27 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170904):
<p>Actually on re-reading -- are you asking something else?</p>

#### [ Mario Carneiro (May 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127171166):
<p>The solution is to use that <code>fintype</code> is a subsingleton to fix your argument</p>


{% endraw %}

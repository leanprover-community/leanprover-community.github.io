---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29056finitesetlemmasveryhardtouse.html
---

## Stream: [general](index.html)
### Topic: [finite set lemmas very hard to use](29056finitesetlemmasveryhardtouse.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127169799):
A lot of the finite set lemmas are extremely difficult to use. For example `set.empty_card` can only be used in a rewrite, if I've used `fintype_empty` as my `fintype` instance in my goal. Would it be a good idea to make fintype instances an argument to the lemma whenever they're used in the statement of a theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170886):
You mean instead of using the type class resolution system?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170892):
Let me just comment that if I've understood your question correctly then I had the same problems using the `is_ring_hom` typeclass and it seemed to me initially that by far the easiest fix was just to make it not a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170897):
but instead I started that typeclass woes thread, and every time I got stuck or frustrated, Mario explained how to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127170904):
Actually on re-reading -- are you asking something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20set%20lemmas%20very%20hard%20to%20use/near/127171166):
The solution is to use that `fintype` is a subsingleton to fix your argument


{% endraw %}

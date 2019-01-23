---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/32800Whatswiththeinzero.html
---

## Stream: [maths](index.html)
### Topic: [What's with the `_` in `zero_`?](32800Whatswiththeinzero.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 07 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135330352):
I've seen this in a few places now:

```lean
class is_submodule {α : Type u} {β : Type v} [ring α] [module α β] (p : set β) : Prop :=
(zero_ : (0:β) ∈ p)
(add_  : ∀ {x y}, x ∈ p → y ∈ p → x + y ∈ p)
(smul : ∀ c {x}, x ∈ p → c • x ∈ p)
```
Why `zero_` and `add_` but not `smul_`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135331864):
I think we are using `'` for this now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135331865):
it's avoiding a name clash with a restated axiom just below it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 07 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135342852):
Once we decide on a convention will it mean that a lot of code needs to be rewritten? The idea is that we are separating off the actual constructor (which is supposed to be thought of as hidden?) from the user interface? Of course `'` is used in other situations in mathlib to mean something else -- like "oh if you don't want that `add_sub_cancel` you might instead find `add_sub_cancel'` useful", right?


{% endraw %}

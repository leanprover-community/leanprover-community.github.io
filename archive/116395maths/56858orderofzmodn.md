---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56858orderofzmodn.html
---

## Stream: [maths](index.html)
### Topic: [order of zmod n](56858orderofzmodn.html)

---


{% raw %}
#### [ Guy Leroy (Aug 02 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130770849):
Hi, I'm trying to find the order of zmod n.
Chris helped me and wrote this code:

instance (n : nat) : pos_nat (nat.succ n) := ⟨nat.succ_pos _⟩ 
instance : fintype  (units (zmod 5)) := sorry
instance : decidable_eq (units (zmod 5)) := 
λ x y, decidable_of_iff _ ⟨ units.ext, λ _,by simp *⟩
#eval @order_of (units (zmod 5)) _ _ _ ⟨(2 : zmod 5), 2⁻¹, rfl, rfl⟩ 

However the eval command sends the error "units.fintype: trying to evaluate sorry" presumably because we didn't prove instance : fintype  (units (zmod 5)). So I guess my question is how can I prove the latter?

#### [ Kenny Lau (Aug 02 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771157):
MWE please

#### [ Kevin Buzzard (Aug 02 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771164):
I think Chris said that `units R` is not just the subtype of R -- to construct a term of type `units R` you actually need to give both `u` and its inverse `v`. So you will need to prove some lemma (which might be already there) saying that there's an injection from `units R` to `R`, and then convince lean that a subtype of a fintype is a fintype.

To look for the injection from `units R` into `R` I would find where `units` are defined and then look at the code written shortly afterwards to see if there's anything useful. Then one might hope that all the rest is there already.

#### [ Kenny Lau (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771214):
no, the subtype of a fintype is not a fintype. that's why you can create a fintype by a surjection but not by an injection

#### [ Kenny Lau (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771219):
(but you can do various things if you have a finset of R that contains all the units, such as `finset.attach`)

#### [ Kenny Lau (Aug 02 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771228):
and the injection is just `units.val`

#### [ Kevin Buzzard (Aug 02 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771277):
```quote
no, the subtype of a fintype is not a fintype.
```
Wait what? Even when everything is decidable?

#### [ Kenny Lau (Aug 02 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771279):
if it's decidable then it's ok

#### [ Kevin Buzzard (Aug 02 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771291):
I don't know if decidability is proved, but for a in Zmod n I can decide if it's a unit or not. @**Chris Hughes** do you know if this needs doing, or is it already done?

#### [ Kevin Buzzard (Aug 02 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771406):
@**Guy Leroy** Chris suggests you prove an equiv between `units (zmod n)` and the nats between 0 and n-1 which are coprime to n. That would do it.

#### [ Kevin Buzzard (Aug 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771415):
Oh Ellen just messaged me, she's sitting next to me. I can't believe I'm in a room full of people all talking to each other online. Guy is about 4 metres from me. Is this how kids work nowadays?

#### [ Guy Leroy (Aug 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771464):
Thanks for the answers!

#### [ Scott Morrison (Aug 02 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771479):
@**Kevin Buzzard** just wait until they get the neural implants...

#### [ Kenny Lau (Aug 02 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771543):
kids these days, only focussing on their laptops instead of on their newspapers

#### [ Patrick Massot (Aug 02 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772043):
I'm pretty surprised they gathered in the same room. Where I studied, all freely accessible computer rooms disappeared because students stopped using them when internet reached the student housing 15 years ago.

#### [ Kenny Lau (Aug 02 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772049):
they're doing UROP

#### [ Kevin Buzzard (Aug 02 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772978):
I force them to come in :-) In fact I don't even know why we're meeting in the computer room -- everyone brings their own computers.


{% endraw %}

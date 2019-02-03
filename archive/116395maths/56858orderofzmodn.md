---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56858orderofzmodn.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [order of zmod n](https://leanprover-community.github.io/archive/116395maths/56858orderofzmodn.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Guy Leroy (Aug 02 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130770849):
<p>Hi, I'm trying to find the order of zmod n.<br>
Chris helped me and wrote this code:</p>
<p>instance (n : nat) : pos_nat (nat.succ n) := ⟨nat.succ_pos _⟩ <br>
instance : fintype  (units (zmod 5)) := sorry<br>
instance : decidable_eq (units (zmod 5)) := <br>
λ x y, decidable_of_iff _ ⟨ units.ext, λ _,by simp *⟩<br>
#eval @order_of (units (zmod 5)) _ _ _ ⟨(2 : zmod 5), 2⁻¹, rfl, rfl⟩ </p>
<p>However the eval command sends the error "units.fintype: trying to evaluate sorry" presumably because we didn't prove instance : fintype  (units (zmod 5)). So I guess my question is how can I prove the latter?</p>

#### [ Kenny Lau (Aug 02 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771157):
<p>MWE please</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771164):
<p>I think Chris said that <code>units R</code> is not just the subtype of R -- to construct a term of type <code>units R</code> you actually need to give both <code>u</code> and its inverse <code>v</code>. So you will need to prove some lemma (which might be already there) saying that there's an injection from <code>units R</code> to <code>R</code>, and then convince lean that a subtype of a fintype is a fintype.</p>
<p>To look for the injection from <code>units R</code> into <code>R</code> I would find where <code>units</code> are defined and then look at the code written shortly afterwards to see if there's anything useful. Then one might hope that all the rest is there already.</p>

#### [ Kenny Lau (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771214):
<p>no, the subtype of a fintype is not a fintype. that's why you can create a fintype by a surjection but not by an injection</p>

#### [ Kenny Lau (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771219):
<p>(but you can do various things if you have a finset of R that contains all the units, such as <code>finset.attach</code>)</p>

#### [ Kenny Lau (Aug 02 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771228):
<p>and the injection is just <code>units.val</code></p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771277):
<blockquote>
<p>no, the subtype of a fintype is not a fintype.</p>
</blockquote>
<p>Wait what? Even when everything is decidable?</p>

#### [ Kenny Lau (Aug 02 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771279):
<p>if it's decidable then it's ok</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771291):
<p>I don't know if decidability is proved, but for a in Zmod n I can decide if it's a unit or not. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> do you know if this needs doing, or is it already done?</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771406):
<p><span class="user-mention" data-user-id="111947">@Guy Leroy</span> Chris suggests you prove an equiv between <code>units (zmod n)</code> and the nats between 0 and n-1 which are coprime to n. That would do it.</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771415):
<p>Oh Ellen just messaged me, she's sitting next to me. I can't believe I'm in a room full of people all talking to each other online. Guy is about 4 metres from me. Is this how kids work nowadays?</p>

#### [ Guy Leroy (Aug 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771464):
<p>Thanks for the answers!</p>

#### [ Scott Morrison (Aug 02 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771479):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> just wait until they get the neural implants...</p>

#### [ Kenny Lau (Aug 02 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130771543):
<p>kids these days, only focussing on their laptops instead of on their newspapers</p>

#### [ Patrick Massot (Aug 02 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772043):
<p>I'm pretty surprised they gathered in the same room. Where I studied, all freely accessible computer rooms disappeared because students stopped using them when internet reached the student housing 15 years ago.</p>

#### [ Kenny Lau (Aug 02 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772049):
<p>they're doing UROP</p>

#### [ Kevin Buzzard (Aug 02 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/order%20of%20zmod%20n/near/130772978):
<p>I force them to come in :-) In fact I don't even know why we're meeting in the computer room -- everyone brings their own computers.</p>


{% endraw %}

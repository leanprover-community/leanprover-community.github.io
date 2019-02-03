---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09115lefordiv.html
---

## Stream: [general](index.html)
### Topic: [le for div?](09115lefordiv.html)

---


{% raw %}
#### [ Nicholas Scheel (Apr 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124631308):
<p>This seems like a silly question but I've scoured mathlib and init for this lemma and I can't find it: <code>∀ {n m : ℕ} (h : n ≤ m) {k}, n/k ≤ m/k</code><br>
I don't think it can be derived from <code>div_le_of_le_mul</code> since <code>k*(n/k) = n</code> does not necessarily hold (only if <code>k | n</code>)<br>
a version for multiplication would be nice too<br>
does this exist? is there a nice way to prove it?</p>

#### [ Simon Hudon (Apr 04 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124631526):
<p>I think <code>le_div_iff_mul_le</code>with <code>div_mul_le_self</code> should allow you to prove that</p>

#### [ Chris Hughes (Apr 04 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632258):
<p>It doesn't. Applying <code>le_div_of_mul_le</code> gives you something false to prove, if say <code>n=4</code>, <code>m=5</code>, <code>k=3</code></p>

#### [ Simon Hudon (Apr 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632310):
<p>Don't use <code>le_div_of_mul_le</code>; use <code>le_div_iff_mul_le</code> instead</p>

#### [ Chris Hughes (Apr 04 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632336):
<p>Sorry, I was talking about a  <code>div_le</code> not <code>le_div</code></p>

#### [ Nicholas Scheel (Apr 04 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632408):
<p>Thanks for the tip! <span class="emoji emoji-1f647" title="bow">:bow:</span> I think I got it working now:</p>
<div class="codehilite"><pre><span></span>lemma nat.le_mul {n m : ℕ} (h : n ≤ m) {k} : n*k ≤ m*k
:= begin
  cases k with k, rw [nat.mul_zero, nat.mul_zero],
  apply (nat.le_div_iff_mul_le n (m*nat.succ k) (nat.zero_lt_succ k)).1,
  rw [nat.mul_div_left],
  exact h,
  apply nat.zero_lt_succ,
end

lemma nat.le_div {n m : ℕ} (h : n ≤ m) {k} : n/k ≤ m/k
:= begin
  cases k with k, rw [nat.div_zero, nat.div_zero],
  apply (nat.le_div_iff_mul_le (n/nat.succ k) (m) (nat.zero_lt_succ k)).2,
  transitivity,
  apply nat.div_mul_le_self,
  exact h,
end
</pre></div>

#### [ Simon Hudon (Apr 04 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632672):
<p>A a matter of style, you may prefer <code>cases lt_or_eq_of_le (zero_le k) with hk hk</code> instead of <code>cases k with k</code></p>

#### [ Matt Wilson (Apr 04 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632693):
<p>peanut gallery question, but how long does that take to run</p>

#### [ Simon Hudon (Apr 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632760):
<p>About 51ms on my system</p>

#### [ Simon Hudon (Apr 04 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124632821):
<p>Sorry, wrong proof. <span class="user-mention" data-user-id="111651">@Nicholas Scheel</span> 's proof takes 6ms</p>

#### [ Simon Hudon (Apr 04 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124637611):
<p><span class="user-mention" data-user-id="111651">@Nicholas Scheel</span> Feel free to send a pull request of that theorem to mathlib. You should call it <code>nat.div_le_div</code>.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124645163):
<p><code> nat.mul_le_mul_right : ∀ {n m : ℕ} (k : ℕ), n ≤ m → n * k ≤ m * k </code> is already there</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124645166):
<p>but I haven't seen the div version before</p>

#### [ Mario Carneiro (Apr 05 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650222):
<p>I'm also surprised to find this is missing. I will add it to mathlib, by the name <code>nat.div_le_div_right</code></p>

#### [ Nicholas Scheel (Apr 05 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650281):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110026">@Simon Hudon</span>  How about this? <a href="https://github.com/MonoidMusician/mathlib/pull/1" target="_blank" title="https://github.com/MonoidMusician/mathlib/pull/1">https://github.com/MonoidMusician/mathlib/pull/1</a> ;)</p>

#### [ Mario Carneiro (Apr 05 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650329):
<p>I'm also going to rewrite the proof, since it's a one-liner. I think Simon gave a hint earlier about this, see if you can shorten your proof</p>

#### [ Nicholas Scheel (Apr 05 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650541):
<p>hmm okay, I don’t know enough to see how to shorten it like that and I’ve run out of time tonight, feel free to pick it up if you want <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (Apr 05 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650589):
<p>oh, actually I forgot about the zero case. Anyway here's my attempt at shortening it:</p>
<div class="codehilite"><pre><span></span>protected theorem div_le_div {n m : ℕ} (h : n ≤ m) {k : ℕ} : n / k ≤ m / k :=
(nat.eq_zero_or_pos k).elim (λ k0, by simp [k0]) $ λ hk,
(nat.le_div_iff_mul_le _ _ hk).2 $ le_trans (nat.div_mul_le_self _ _) h
</pre></div>

#### [ Nicholas Scheel (Apr 05 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650592):
<p>(whoops didn’t realize that I PRed my own repo)</p>

#### [ Mario Carneiro (Apr 05 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le%20for%20div%3F/near/124650653):
<p>looking at the differences, I guess I didn't do much besides compactify the same steps, more or less</p>


{% endraw %}

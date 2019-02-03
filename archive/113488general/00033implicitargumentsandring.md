---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00033implicitargumentsandring.html
---

## Stream: [general](index.html)
### Topic: [implicit arguments, and `ring`](00033implicitargumentsandring.html)

---


{% raw %}
#### [ Scott Morrison (Sep 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878744):
<p>Hi <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, I noticed an unfortunate feature of <code>ring</code>.</p>

#### [ Scott Morrison (Sep 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878745):
<p>I'd got stuck doing this:</p>
<div class="codehilite"><pre><span></span>example (x y : ℕ) (h : x ^ 2 + 3 * y ^ 2 = 4) : false :=
begin
ring at h,
simp at h,
ring at h,
simp at h,
-- ...
end
</pre></div>

#### [ Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878784):
<p>where it looks like the goal isn't changing.</p>

#### [ Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878788):
<p>It just says </p>
<div class="codehilite"><pre><span></span>x y : ℕ,
h : x ^ 2 + 3 * y ^ 2 = 4
⊢ false
</pre></div>

#### [ Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878791):
<p>but with pp.all true, you can see if flipping back and forth:</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878803):
<p>You shouldn't use <code>ring</code> nonterminally</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878808):
<p>at least not automatically (i.e. in <code>tidy</code>)</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878815):
<p>if it doesn't close the goal, assume it failed</p>

#### [ Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878817):
<p>Yes, I know, but I want to for a moment anyway. :-)</p>

#### [ Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878818):
<p>Ah, okay. :-)</p>

#### [ Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878821):
<p>But that takes all the fun out of it.</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878823):
<p><code>ring</code> rewrites the goal into sum-of-products form for ease of reading when it fails</p>

#### [ Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878827):
<p>Because sometimes <code>ring at *, exfalso, linarith</code> can get stuff done.</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878829):
<p>this form disagrees with simp normal form in some places</p>

#### [ Scott Morrison (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878870):
<p>The problem I was having here is actually just in the implicit arguments flipping back and forth.</p>

#### [ Scott Morrison (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878874):
<p>The expression "itself" is not being changed by either <code>simp</code> or <code>ring</code>.</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878881):
<p>wait, maybe I don't understand then</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878882):
<p>what is changing?</p>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878894):
<p>With usual pretty printing, neither <code>simp</code> nor <code>ring</code> do anything, and the goal just looks like</p>
<div class="codehilite"><pre><span></span>x y : ℕ,
h : x ^ 2 + 3 * y ^ 2 = 4
⊢ false
</pre></div>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878896):
<p>but with pp.all we get:</p>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878898):
<div class="codehilite"><pre><span></span>x y : nat,
h :
  @eq.{1} nat
    (@has_add.add.{0} nat nat.has_add
       (@has_pow.pow.{0 0} nat nat nat.has_pow x (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
       (@has_mul.mul.{0} nat
          (@mul_zero_class.to_has_mul.{0} nat
             (@semiring.to_mul_zero_class.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one))
          (@has_pow.pow.{0 0} nat nat nat.has_pow y (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))
    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
⊢ false
</pre></div>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878899):
<p>after the <code>simp</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878900):
<p>oh, it's nat.pow isn't it</p>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878901):
<p>and then</p>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878905):
<div class="codehilite"><pre><span></span>x y : nat,
h :
  @eq.{1} nat
    (@has_add.add.{0} nat nat.has_add
       (@has_pow.pow.{0 0} nat nat
          (@monoid.has_pow.{0} nat
             (@semiring.to_monoid.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          x
          (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
       (@has_mul.mul.{0} nat
          (@mul_zero_class.to_has_mul.{0} nat
             (@semiring.to_mul_zero_class.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one))
          (@has_pow.pow.{0 0} nat nat
             (@monoid.has_pow.{0} nat
                (@semiring.to_monoid.{0} nat
                   (@comm_semiring.to_semiring.{0} nat
                      (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                         nat.canonically_ordered_comm_semiring))))
             y
             (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))
    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
⊢ false
</pre></div>

#### [ Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878906):
<p>after the <code>ring</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878947):
<p>right, <code>ring</code> prefers monoid powers but that's not simp normal form</p>

#### [ Scott Morrison (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878950):
<p>Okay, I see.</p>

#### [ Scott Morrison (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878951):
<p>Nothing to be done, then!</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878962):
<p><code>ring </code> doesn't make any attempt to be in simp normal form; if you need that you should just call <code>ring, simp</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878965):
<p>but even better is to just ignore the pretty failure mode</p>

#### [ Kenny Lau (Sep 29 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134879165):
<p>it's a feature!</p>


{% endraw %}

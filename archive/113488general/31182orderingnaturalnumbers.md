---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31182orderingnaturalnumbers.html
---

## Stream: [general](index.html)
### Topic: [ordering natural numbers](31182orderingnaturalnumbers.html)

---


{% raw %}
#### [ Adam Kurkiewicz (Apr 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667719):
It appears that lean can't synthesize what appears to be a natural order on natural numbers, and neither can I.

I'm a bit lost on what to do. I think I need `something: linear_ordered_field nat` but not sure how to get that `something`. Any help would be greatly appreciated. The terms I'm trying to produce are called `DOESNTWORK` and `DOESNTWORKEITHER` and are at the bottom of the second lemma.

```
def  gt1or0 (a : nat) : a =  0  ∨ a >  0  :=
sorry

def  multiply_is_no_less (a b : nat) (P : b ≠  0) : a <= a * b :=
or.elim (gt1or0 a)
(λ (H : a =  0),
have A : 0  <=  0, from dec_trivial,
have B : 0  =  0  * b, from eq.symm (zero_mul b),
have C : 0  <=  0  * b, from eq.subst B A,
have D : 0  = a, from eq.symm H,
show a <= a * b, from eq.subst D C
)
(λ (H : a >  0),
have A : b >  1, from  sorry,
-- this won't be automatically true, but we can get it from appropriate or.elim or similarly.
have DOESNTWORK : a < a * b, from lt_mul_of_gt_one_right H A,
have DOESNTWORKEITHER : a < a * b, from  @lt_mul_of_gt_one_right nat _ b a H A, sorry
 )
```

#### [ Kevin Buzzard (Apr 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667890):
In maths, a field is something with `+ - * /` like the rationals or reals.

#### [ Kevin Buzzard (Apr 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667891):
nat is no good because no `-` and no `/`

#### [ Kevin Buzzard (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667906):
In particular you can't use the general result ` lt_mul_of_gt_one_right ` on `nat`

#### [ Adam Kurkiewicz (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667907):
Ah of course. It's a bad lemma then.

#### [ Kevin Buzzard (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667909):
You might well find though, that the lemma you want is there anyway

#### [ Kevin Buzzard (Apr 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667965):
because when it comes to nat, the library seems to me to be fairly robust and complete

#### [ Kevin Buzzard (Apr 05 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667983):
In fact it would not surprise me if pretty much anything like this that you wanted to prove was either there (although you already found a counterexample to that with the div thing) or was easily provable from what is there.

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668038):
I know what each of the words `linear`, `field` and `ordered` mean, but of course typing was faster than thinking this time :D. I'll have a look, thanks!

#### [ Kevin Buzzard (Apr 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668056):
For `gt1or0` (which maybe should be called `gt0or0`) my instinct (in VS Code) is to type `#check nat.pos_of` and then hit esc, ctrl-space, esc,ctrl-space (the lean plugin is a bit buggy in this regard)

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668099):
and to see what comes up.

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668105):
`nat.pos_of...` means "proof, specific to nat, that something is positive if..."

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668111):
and then we find `nat.pos_of_ne_zero`

#### [ Kevin Buzzard (Apr 05 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668183):
Similarly, `#check nat.le_mul` (ctrl-space dance) leads you to `nat.mul_le_mul_right`

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668242):
Yup, looks like `nat.pos_of_ne_zero` will work (I can't reproduce your problems with the plugin, it works for me no problem, which is strange, since we're both using ubuntu 16.04 if I recall correctly).

#### [ Kevin Buzzard (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668244):
To prove `a = a * 1` (I am suggesting proving `a <= a * b` by proving `b >= 1` and `a = a * 1` and the lemma) that's just `mul_one`

#### [ Kevin Buzzard (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668250):
The issue with the plugin, which you might run into at some point, is that sometimes ctrl-space gives you a list of possibilities, and then esc and ctrl-space again gives you a bigger list!

#### [ Kevin Buzzard (Apr 05 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668256):
It's difficult to reproduce reliably

#### [ Kevin Buzzard (Apr 05 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668312):
`nat.succ_le_of_lt` will get you from `b > 0` to `b >= 1`, and you can guess how I found this

#### [ Kevin Buzzard (Apr 05 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668318):
In fact I could have guessed the name of that lemma without even searching.

#### [ Kevin Buzzard (Apr 05 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668320):
(note that le and lt are preferred to ge and gt in the naming convention)

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668365):
One naming convention gotcha -- `div` is `/` and and `dvd` is `|` (or more precisely `\|`)

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668370):
and `sub` and `neg` are different -- one is binary, one unary

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668374):
but the rigorous naming conventions make looking through the library much easier and if you're proving stuff about nat then it should be really helpful for you.

#### [ Kevin Buzzard (Apr 05 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668428):
Last thing: `example : decidable_linear_order ℕ :=  by apply_instance` would have been the answer if the instance had been there. But stuff like `decidable_linear_order` is part of the type class system, so should all happen magically (indeed `apply_instance` is a tactic which invokes the magic).

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668574):
 great, I think things will be much easier from now on. Thank you! I'm trying to show there are infinitely many primes, which I think is a good exercise, although it's already in mathlib:
https://github.com/leanprover/mathlib/blob/08f19fde695d20cf1bd899969a1c59b350dd9e43/data/nat/prime.lean#L201


{% endraw %}

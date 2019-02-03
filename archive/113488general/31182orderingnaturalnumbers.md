---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31182orderingnaturalnumbers.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [ordering natural numbers](https://leanprover-community.github.io/archive/113488general/31182orderingnaturalnumbers.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Adam Kurkiewicz (Apr 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667719):
<p>It appears that lean can't synthesize what appears to be a natural order on natural numbers, and neither can I.</p>
<p>I'm a bit lost on what to do. I think I need <code>something: linear_ordered_field nat</code> but not sure how to get that <code>something</code>. Any help would be greatly appreciated. The terms I'm trying to produce are called <code>DOESNTWORK</code> and <code>DOESNTWORKEITHER</code> and are at the bottom of the second lemma.</p>
<div class="codehilite"><pre><span></span>def  gt1or0 (a : nat) : a =  0  ∨ a &gt;  0  :=
sorry

def  multiply_is_no_less (a b : nat) (P : b ≠  0) : a &lt;= a * b :=
or.elim (gt1or0 a)
(λ (H : a =  0),
have A : 0  &lt;=  0, from dec_trivial,
have B : 0  =  0  * b, from eq.symm (zero_mul b),
have C : 0  &lt;=  0  * b, from eq.subst B A,
have D : 0  = a, from eq.symm H,
show a &lt;= a * b, from eq.subst D C
)
(λ (H : a &gt;  0),
have A : b &gt;  1, from  sorry,
-- this won&#39;t be automatically true, but we can get it from appropriate or.elim or similarly.
have DOESNTWORK : a &lt; a * b, from lt_mul_of_gt_one_right H A,
have DOESNTWORKEITHER : a &lt; a * b, from  @lt_mul_of_gt_one_right nat _ b a H A, sorry
 )
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667890):
<p>In maths, a field is something with <code>+ - * /</code> like the rationals or reals.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667891):
<p>nat is no good because no <code>-</code> and no <code>/</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667906):
<p>In particular you can't use the general result <code> lt_mul_of_gt_one_right </code> on <code>nat</code></p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667907):
<p>Ah of course. It's a bad lemma then.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667909):
<p>You might well find though, that the lemma you want is there anyway</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667965):
<p>because when it comes to nat, the library seems to me to be fairly robust and complete</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124667983):
<p>In fact it would not surprise me if pretty much anything like this that you wanted to prove was either there (although you already found a counterexample to that with the div thing) or was easily provable from what is there.</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668038):
<p>I know what each of the words <code>linear</code>, <code>field</code> and <code>ordered</code> mean, but of course typing was faster than thinking this time :D. I'll have a look, thanks!</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668056):
<p>For <code>gt1or0</code> (which maybe should be called <code>gt0or0</code>) my instinct (in VS Code) is to type <code>#check nat.pos_of</code> and then hit esc, ctrl-space, esc,ctrl-space (the lean plugin is a bit buggy in this regard)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668099):
<p>and to see what comes up.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668105):
<p><code>nat.pos_of...</code> means "proof, specific to nat, that something is positive if..."</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668111):
<p>and then we find <code>nat.pos_of_ne_zero</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668183):
<p>Similarly, <code>#check nat.le_mul</code> (ctrl-space dance) leads you to <code>nat.mul_le_mul_right</code></p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668242):
<p>Yup, looks like <code>nat.pos_of_ne_zero</code> will work (I can't reproduce your problems with the plugin, it works for me no problem, which is strange, since we're both using ubuntu 16.04 if I recall correctly).</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668244):
<p>To prove <code>a = a * 1</code> (I am suggesting proving <code>a &lt;= a * b</code> by proving <code>b &gt;= 1</code> and <code>a = a * 1</code> and the lemma) that's just <code>mul_one</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668250):
<p>The issue with the plugin, which you might run into at some point, is that sometimes ctrl-space gives you a list of possibilities, and then esc and ctrl-space again gives you a bigger list!</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668256):
<p>It's difficult to reproduce reliably</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668312):
<p><code>nat.succ_le_of_lt</code> will get you from <code>b &gt; 0</code> to <code>b &gt;= 1</code>, and you can guess how I found this</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668318):
<p>In fact I could have guessed the name of that lemma without even searching.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668320):
<p>(note that le and lt are preferred to ge and gt in the naming convention)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668365):
<p>One naming convention gotcha -- <code>div</code> is <code>/</code> and and <code>dvd</code> is <code>|</code> (or more precisely <code>\|</code>)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668370):
<p>and <code>sub</code> and <code>neg</code> are different -- one is binary, one unary</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668374):
<p>but the rigorous naming conventions make looking through the library much easier and if you're proving stuff about nat then it should be really helpful for you.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668428):
<p>Last thing: <code>example : decidable_linear_order ℕ :=  by apply_instance</code> would have been the answer if the instance had been there. But stuff like <code>decidable_linear_order</code> is part of the type class system, so should all happen magically (indeed <code>apply_instance</code> is a tactic which invokes the magic).</p>

#### [ Adam Kurkiewicz (Apr 05 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordering%20natural%20numbers/near/124668574):
<p>great, I think things will be much easier from now on. Thank you! I'm trying to show there are infinitely many primes, which I think is a good exercise, although it's already in mathlib:<br>
<a href="https://github.com/leanprover/mathlib/blob/08f19fde695d20cf1bd899969a1c59b350dd9e43/data/nat/prime.lean#L201" target="_blank" title="https://github.com/leanprover/mathlib/blob/08f19fde695d20cf1bd899969a1c59b350dd9e43/data/nat/prime.lean#L201">https://github.com/leanprover/mathlib/blob/08f19fde695d20cf1bd899969a1c59b350dd9e43/data/nat/prime.lean#L201</a></p>


{% endraw %}

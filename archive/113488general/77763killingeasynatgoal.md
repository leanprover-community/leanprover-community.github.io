---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77763killingeasynatgoal.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [killing easy nat goal](https://leanprover-community.github.io/archive/113488general/77763killingeasynatgoal.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 20 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969731):
<p>Faced with <code>∀ n, 2 * nat.succ (n) = nat.succ (2 * n + 1)</code> I find that simp or ring don't seem to be able to do it. Even <code>intro n, simp [nat.succ_eq_add_one,mul_add,one_add_one_eq_two]</code> doesn't work. I can use simp and then ring!</p>

#### [ Kevin Buzzard (Mar 20 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969887):
<div class="codehilite"><pre><span></span>  intro n,
  suffices : 2 + 2 * n = 1 + (1 + 2 * n),
    simp [nat.succ_eq_add_one,mul_add,this],
  ring
</pre></div>

#### [ Kevin Buzzard (Mar 20 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969888):
<p>meh</p>

#### [ Patrick Massot (Mar 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971217):
<p>Isn't there a lemma saying it suffices to prove this in Z, and then ring does it?</p>

#### [ Simon Hudon (Mar 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971737):
<p>Interesting! What would that lemma look like?</p>

#### [ Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971848):
<p>From a mathematician perspective, the lemma says the inclusion of N into Z is injective</p>

#### [ Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971851):
<p>Insert words like coercion or cast</p>

#### [ Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971854):
<p>and get the CS version</p>

#### [ Patrick Massot (Mar 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971878):
<p>I don't have a computer with Lean where I am right now</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971881):
<p>Fortunately I think ring seems to work on nat, faced with ring operations like + or *</p>

#### [ Simon Hudon (Mar 20 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971936):
<p>ah! So the injectivity of <code>coe</code> plus the distributivity over +, * and succ would do it. That is really nice</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971953):
<p>One issue is that ring would rather see <code>n + 1</code> than <code>nat.succ n</code></p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971978):
<p>to coerce into Z you'll need <code>nat.cast_add</code>, <code>nat.cast_mul</code>, <code>nat.cast_one</code></p>

#### [ Simon Hudon (Mar 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971979):
<p>I would assume that <code>↑(succ n) = ↑n + 1</code> would be a simp rule so <code>succ</code> would disappear</p>

#### [ Chris Hughes (Mar 20 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972132):
<p>Have you tried rfl? 2<em>succ n := 2</em>n + 2 := succ(2*n+1), maybe rw add_comm or mul_comm first?</p>

#### [ Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972404):
<p>There should be a tactic doing that for any equality in nat which would immediately follow from ring in int</p>

#### [ Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972415):
<p>without any preliminary rw</p>

#### [ Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972422):
<p>I'm sure Simon is already writing it</p>

#### [ Simon Hudon (Mar 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972435):
<p>I sneezed so you wrote the above before I could get started</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972553):
<blockquote>
<p>Have you tried rfl? 2<em>succ n := 2</em>n + 2 := succ(2*n+1), maybe rw add_comm or mul_comm first?</p>
</blockquote>
<p>Aah! I tried refl before intro n and it failed, but after intro n it succeeds.</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972554):
<p>Thanks.</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972561):
<p>Chris, I'm doing the exercises here:</p>

#### [ Kevin Buzzard (Mar 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972570):
<p><a href="https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html" target="_blank" title="https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html">https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html</a></p>

#### [ Simon Hudon (Mar 20 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123973436):
<p>I did a bit of scripting and then tried to find what fails and I found that this works: </p>
<div class="codehilite"><pre><span></span>example (n : ℕ) : 2 * nat.succ (n) = nat.succ (2 * n + 1) :=
begin
  ring,
end
</pre></div>


<p>Why doesn't it work for you?</p>

#### [ Kevin Buzzard (Mar 20 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123976260):
<p>because I had "forall n" in front of it :-/</p>

#### [ Simon Hudon (Mar 20 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123976344):
<p>Maybe <code>ring</code> should start with <code>intros</code></p>


{% endraw %}

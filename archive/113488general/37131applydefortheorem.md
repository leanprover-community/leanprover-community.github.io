---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37131applydefortheorem.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [apply def or theorem](https://leanprover-community.github.io/archive/113488general/37131applydefortheorem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Hoang Le Truong (Aug 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131070910):
<p>I have the following definitions </p>
<div class="codehilite"><pre><span></span> def index  {s : set( set α)} (n:ℕ)  [fintype s] (H:∀i∈ s, finite i)
    : set(set(set α )) :=  { t| t ⊆ s ∧   fintype.card t=n}
</pre></div>


<p>I get a following error</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type,
s : set (set α),
n : ℕ,
_inst_1 : fintype ↥s,
H : ∀ (i : set α), i ∈ s → finite i,
t : set (set α)
⊢ fintype ↥t
</pre></div>


<p>I see that the following definition in <code>data.set.finite</code></p>
<div class="codehilite"><pre><span></span>def fintype_subset (s : set α) {t : set α} [fintype s] [decidable_pred t] (h : t ⊆ s) : fintype t :=
by rw ← inter_eq_self_of_subset_right h; apply_instance
</pre></div>


<p>How can I apply it to my definition?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071337):
<p>So alpha is a random type, s is a set of subsets of alpha (so s could be empty), _inst_1 is a proof that s is finite (so s could still be empty), H says something about all elements of s (so if s is empty then H is true), but alpha could still be a random type, and now t is some set of subsets of alpha so there's no reason to expect that t is finite, unless I made a slip.</p>

#### [ Chris Hughes (Aug 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071399):
<p><code>{ t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}</code></p>

#### [ Kevin Buzzard (Aug 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071404):
<p>Oh, so that type class instance can't be synthesized because Lean hasn't got to the point where t is a subset of s yet.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071421):
<p>So Chris' clever trick is to give a name to the fact that t is a subset of s, and then we can use it later.</p>

#### [ Chris Hughes (Aug 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071427):
<p>The other set is finite too, since it's a subset of the powerset of s, which is finite.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071519):
<p>Right -- I was just looking at the error, where there were no assumptions on t at all. You managed to insert the subset assumption into the system so Lean could see it.</p>

#### [ Chris Hughes (Aug 07 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071726):
<p>There is a case for a dependent and. The trouble with the exists trick is there's no <code>exists.left</code> and <code>exists</code> doesn't eliminate into data, but dependent and could.</p>

#### [ Chris Hughes (Aug 08 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071738):
<p>But I don't think it comes up that often.</p>

#### [ Hoang Le Truong (Aug 08 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131071810):
<p>I try  <code>{ t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}</code> but I get </p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type,
s : set (set α),
n : ℕ,
_inst_1 : fintype ↥s,
H : ∀ (i : set α), i ∈ s → finite i,
t : set (set α),
h : t ⊆ s
⊢ decidable_pred t
</pre></div>

#### [ Chris Hughes (Aug 08 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072001):
<p>You can use <code>local attribute [instance] classical.prop_decidable</code> before the statement of the theorem.</p>

#### [ Hoang Le Truong (Aug 08 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072181):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  Since <code>s</code> is finite and <code>t ⊆ s</code> then <code>t </code> is finite by def <code> fintype_subset</code></p>
<div class="codehilite"><pre><span></span>def index   {s : set( set α)} (n:ℕ)  [fintype s] (H:∀i∈ s, finite i)
    : set(set(set α )) :=  { t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}
</pre></div>


<p>where am I use <code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Chris Hughes (Aug 08 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072280):
<p>On its own line before the definition.</p>

#### [ Chris Hughes (Aug 08 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072342):
<p>You might be better off using <code>finsets</code> for this actually.</p>

#### [ Chris Hughes (Aug 08 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072354):
<p>Then you don't have to worry about proving things are finite.</p>

#### [ Hoang Le Truong (Aug 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20def%20or%20theorem/near/131072422):
<p>Ok I will try it</p>


{% endraw %}

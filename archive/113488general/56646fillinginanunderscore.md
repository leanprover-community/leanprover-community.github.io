---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56646fillinginanunderscore.html
---

## Stream: [general](index.html)
### Topic: [filling in an underscore](56646fillinginanunderscore.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 29 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374909):
<div class="codehilite"><pre><span></span>import data.fintype
import algebra

universes u v
-- Chris multiset example

theorem meh {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n := λ H, lt.trans H $ nat.lt_succ_self _

theorem miracle (f : ℕ → ℕ)
(d : ℕ)
(Hd :
  ∀ (g : fin d → ℕ),
    (∀ (i : fin d), f (i.val) = g i) →
      finset.sum (finset.range d) f = finset.sum finset.univ g)
(g : fin (nat.succ d) → ℕ)
(h : ∀ (i : fin (nat.succ d)), f (i.val) = g i)
: finset.sum (finset.range d) f = finset.sum finset.univ (λ (i : fin d), g ⟨i.val, meh i.is_lt⟩)
:=
let gres : fin d → ℕ := λ (i : fin d), g ⟨i.val, meh i.is_lt⟩ in
begin
rw Hd gres (λ i, h ⟨i.val,_⟩)
end
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374951):
<p>Lean magically filled in the underscore in the last but one line</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374971):
<p>It either guessed that <code>i&lt;n -&gt; i&lt;succ n</code></p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374972):
<p>or proved it</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374973):
<p>or decided it didn't care if it was true</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374979):
<p>Note that the result is proved in the definition of gres</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124375018):
<p>(gres is the restriction of <code>g : fin (d+1) -&gt; nat</code>, to fin d)</p>

#### [ Chris Hughes (Mar 29 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124375687):
<p>I think it proved it. Looking at the proof term, it used <code>lt_succ_of_lt</code>. I didn't know lean could do that.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124376073):
<p>What triggered that? Is it the <code>rw</code> ? I tried to minimise this but didn't get far.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124418473):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> can you clarify what is going on here?</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124423248):
<p>The <code>rw</code> is a confounder here. You could equally well use <code>exact Hd gres (λ i, h ⟨i.val, _⟩)</code> to close the goal. Here are some intermediate data points:</p>
<div class="codehilite"><pre><span></span>Hd gres (λ i, _) -- -&gt; looking for proof of ⊢ f (i.val) = gres i
</pre></div>


<div class="codehilite"><pre><span></span>Hd gres (λ i, h _)
type mismatch at application
  Hd gres (λ (i : fin d), h ?m_1[i])
term
  λ (i : fin d), h ?m_1[i]
has type
  ∀ (i : fin d), f (?m_1[i].val) = g ?m_1[i]
but is expected to have type
  ∀ (i : fin d), f (i.val) = gres i
</pre></div>


<div class="codehilite"><pre><span></span>Hd gres (λ i, h ⟨_, _⟩) -- works
</pre></div>


<p>Lean isn't magically guessing the proof, it's unfolding <code>gres</code> and unifying with the enclosed proof</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433011):
<p>Oh I see. The moment I saw rw I thought "I don't understand that tactic properly, maybe it's doing something under the hood,  so I give in"</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433012):
<p>But now you tell me exact works I can just debug it myself with <code>pp.proofs true</code>.</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433025):
<p>I used to think of stuff like type class inference and proofs being magicked around was just all part of some magic, it's only now I begin to realise that everything that happens, happens for a really precise reason.</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433076):
<p>In some sense I still draw the line at reading <code>tactic.interactive</code> (partly because I know it will be incomprehensible).</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433093):
<p>but really it's because I feel like "end users" shouldn't have to know anything about a tactic other than what is documented.</p>

#### [ Kenny Lau (Mar 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433142):
<blockquote>
<p>I used to think of stuff like type class inference and proofs being magicked around was just all part of some magic, it's only now I begin to realise that everything that happens, happens for a really precise reason.</p>
</blockquote>
<p>there is no magic in lean</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433202):
<p>No, just sufficiently advanced technology.</p>

#### [ Kenny Lau (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433205):
<p>which is canonically isomorphic though</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433208):
<p>so I heard</p>


{% endraw %}

---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79327finitesumpuzzle.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [finite sum puzzle](https://leanprover-community.github.io/archive/113488general/79327finitesumpuzzle.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 30 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390119):
<div class="codehilite"><pre><span></span>import tactic.ring

theorem  finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
(finset.range n).sum f = ((list.range n).map f).sum :=  sorry
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390133):
<p>I've been thinking a lot about induction today.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390183):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there some super-cute way of doing this already?</p>

#### [ Kevin Buzzard (Mar 30 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390201):
<p>I have been trying to formalise quite an abstract approach to questions like these but for all I know this sort of thing is completely well-known. Note that a mathematician would say this proof was trivial and indeed it would be hard to explain to a mathematician why this needed a proof.</p>

#### [ Mario Carneiro (Mar 30 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390250):
<p>It should be by definition, more or less</p>

#### [ Mario Carneiro (Mar 30 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390252):
<p>does <code>rfl</code> work?</p>

#### [ Mario Carneiro (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390310):
<p>Also, of course that needs a proof, stop thinking that proofs that are simple by induction are trivial enough to not need a proof</p>

#### [ Ching-Tsun Chou (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390311):
<p>Don't you need the commutativity of "+" on natural numbers?</p>

#### [ Mario Carneiro (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390315):
<p>that's on the same lines as saying commutativity of natural numbers is trivial</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390473):
<p>Ah, it's not quite by definition, because multiset prod is not defined in terms of list prod but instead is defined using foldl. This works:</p>
<div class="codehilite"><pre><span></span>theorem finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
  (finset.range n).sum f = ((list.range n).map f).sum :=
multiset.coe_sum _
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390533):
<p>Here's a slightly less magical way to write it:</p>
<div class="codehilite"><pre><span></span>theorem finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
  (finset.range n).sum f = ((list.range n).map f).sum :=
show ((list.range n).map f : multiset ℕ).sum = ((list.range n).map f).sum, from
multiset.coe_sum _
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390583):
<p><code>f</code> can map to an <code>add_comm_monoid</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390587):
<p>sure</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390588):
<p>that's what you need, I believe.</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390594):
<p>the theorem you stated is not maximally general</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390597):
<p>So this one seems genuinely easier than Chris' problem?</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390600):
<p>yes, because finset sum is defined as a multiset sum over the map</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390837):
<p>Here's three more trivial statements:</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390842):
<div class="codehilite"><pre><span></span>import tactic.ring
universe u
open nat

theorem list_range_map_sum_induction {X : Type u} [has_add X] [has_zero X] {n : ℕ} (f : ℕ → X) :
  ((list.range (succ n)).map f).sum = ((list.range n).map f).sum + f n := sorry

theorem finset_range_sum_induction {R : Type u} [add_comm_monoid R] {f : ℕ → R} {d : ℕ} :
  (finset.range (succ d)).sum f = (finset.range d).sum f + f d := sorry

theorem finset_univ_sum_fin_induction {R : Type u} [add_comm_monoid R] {d : ℕ}
  {f : fin (nat.succ d) → R} :
  finset.univ.sum f =
    finset.univ.sum (λ i : fin d, f ⟨i.val,lt_trans i.is_lt $ nat.lt_succ_self d⟩) -- d or _?
    + f ⟨d,nat.lt_succ_self _⟩ -- is _ or d better style at the end?
  := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390886):
<p>They all say the same trivial thing in maths</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390888):
<p>so I am really interested in the slickest possible proofs in Lean</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390892):
<p>because I suspect that occasionally my students will want statements like this to just go away</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390947):
<p>If these get unsorried then we get the following proof of Chris' problem from yesterday:</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390956):
<div class="codehilite"><pre><span></span>theorem chris_example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) :
(finset.range n).sum f = finset.univ.sum g := begin
induction n with d Hd, refl, -- base case trivial
-- for the inductive step it&#39;s handy to have notation for the restriction of g,
let gres : fin d → ℕ := λ i,g ⟨i.val,lt_trans i.is_lt $ nat.lt_succ_self d⟩,
-- goal now of form &quot;first kind of sum to succ d equals second kind&quot;
rw finset_range_sum_induction,
rw finset_univ_sum_fin_induction,
-- goal now &quot;first sum to d + f d = second sum to d + g d&quot;
rw [(Hd gres (λ i, h ⟨i.val,_⟩))], -- first sum equals second sum
rw h ⟨d,_⟩, -- f d = g d -- so done
end
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390957):
<p>with not a <code>pmap</code> in sight</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391040):
<p>I would argue that this was a "natural" proof which hides away the abstraction.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391103):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Here's what another proof of your fin n question might look like.</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391106):
<p>By the way, here's a(nother) proof of chris's theorem:</p>
<div class="codehilite"><pre><span></span>example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1 = g i) :
  (finset.range n).sum f = finset.univ.sum g :=
show ((list.range n).map f : multiset ℕ).sum =
   (((list.range n).pmap fin.mk _).map g : multiset ℕ).sum,
by rw [multiset.coe_sum, multiset.coe_sum, ← (funext h : _ = g),
       list.map_pmap, ← list.pmap_eq_map]
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391190):
<p>What I don't like about your proofs is that they seem (to me) to involve knowing about some internal implementation of things. My proof is implementation-free. The library maintainer just creates those <code>blah_sum_induction</code> proofs (the three things sorried above) , and then the end user can construct proofs of Chris' theorem without having to worry about any other implementation.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391225):
<p>Each of the induction laws gives rise to an abstraction which looks like this:</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391233):
<p>I agree, chris has found a hole in the mathlib coverage here</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391244):
<p>Your second theorem is provable by <code>simp</code>, but <code>list.range</code> doesn't break up nicely because the numbers are listed in increasing order</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391303):
<p>I'm not a big fan of your statement of <code>finset_univ_sum_fin_induction</code>, it's all too complicated in the theorem statement</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391308):
<div class="codehilite"><pre><span></span>@[reducible] definition sum_map_range {R : Type u} [add_comm_monoid R] (addend : ℕ → R) : ℕ → R
| zero := (0 : R)
| (succ n) := sum_map_range n + addend n

theorem list_range_map_sum_abstraction {R : Type} [add_comm_monoid R]
  (f : ℕ → R) (n : ℕ) : ((list.range n).map f).sum = sum_map_range f n := sorry

theorem finset_range_sum_abstraction {R : Type u} [add_comm_monoid R] (f : ℕ → R) (n : ℕ) :
  (finset.range n).sum f = sum_map_range f n := sorry

theorem finset_univ_sum_fin_abstraction {R : Type u} [add_comm_monoid R] (f : ℕ → R) (n : ℕ) :
  finset.univ.sum (λ i : fin n, f(i.val)) = sum_map_range f n := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391312):
<p>yes, the fin one stinks.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391365):
<p>If you use lists or finsets then f is a function on N, but to do Chris' problem you had to use a function on fin n</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391367):
<p>I think there are functions for raising <code>fin n</code> to <code>fin (n+1)</code>. Alternatively, you could use <code>fin2</code>, which has a natural inductive construction instead of being a subtype of nat</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391379):
<p><code>fin2</code> is not really developed much, but it is defined in <code>dioph.lean</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391432):
<p>I specifically wanted to design functions which gave me the biggest chance of being covered for all variants of the following question:"this Lean statement is trivially true in maths because it says <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>⋯</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>⋯</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">f(0)+f(1)+\cdots+f(n-1)=f(0)+f(1)+\cdots+f(n-1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathrm">0</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="minner">⋯</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathrm">0</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="minner">⋯</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span>, so how do you prove it in Lean?"</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391442):
<p>I feel like I have convinced myself that for any way of representing the set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo separator="true">,</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo separator="true">,</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>}</mo></mrow><annotation encoding="application/x-tex">\{0,1,...,n-1\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">1</span><span class="mpunct">,</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mpunct">,</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">}</span></span></span></span> in Lean</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391447):
<p>there is an induction principle and an abstraction principle.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391448):
<p>Do I have the right names for these things?</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391500):
<p>As you can see, the examples I have attempted to work out are <code>list.range n</code>, <code>fin n</code> and <code>finset.range n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391502):
<p>Sounds like I need to do <code>fin2 n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391541):
<p>I should say that I have not proved the induction hypotheses in all cases yet.</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391544):
<p>It's mostly used for technical reasons; you can also define recursion principles on <code>fin n</code> with the same structure as <code>fin2</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391552):
<p>but I think that <code>fz</code> and <code>fs</code> are the right way to think about induction on <code>fin n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391555):
<p>But as a mathematician I would find a proof of these sorts of thing rather distasteful (they're all "obvious by induction")</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391597):
<p>so I feel like they should be hidden from view.</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391601):
<p>It's always messy when the function is only partially defined, so that you can't even talk about it out of domain</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391603):
<p>that's what makes <code>list.pmap</code> necessary, and also what makes it a pain to work with</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391610):
<p>What makes Chris's problem hard is the usage of <code>g : fin n -&gt; N</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391614):
<p>same for your induction principle, <code>fin (succ n) -&gt; N</code> is even worse</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391671):
<p>I get the sense that you want to put everything in the form <code>map_sum_range</code> of something, but that doesn't work for partial functions</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391812):
<p>Here's a 4th one</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391815):
<div class="codehilite"><pre><span></span>theorem multiset_sum_map_range_induction {X : Type u} [add_comm_monoid X] {n : ℕ} (f : ℕ → X) :
  ((multiset.range (succ n)).map f).sum =
   ((multiset.range n).map f).sum + f n := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391855):
<p>Corresponding to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>}</mo></mrow><annotation encoding="application/x-tex">\{0,1,\ldots,n-1\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">1</span><span class="mpunct">,</span><span class="minner">…</span><span class="mpunct">,</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">}</span></span></span></span> = <code>multiset.range n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391859):
<p>Each model gives you a new induction principle</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391867):
<p>which I think mathlib could offer with a standard name</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391914):
<p>There are only a finite number of ways that a mathematician can say this trivial thing, and it would be nice if we could just pull a proof out of a hat for each one.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391923):
<p>Could I even write a tactic which proves all these things? Just in some stupid way -- it just tries all the proofs and chooses the one that works.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391932):
<p>aah, <code>simp</code> works on that one.</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391981):
<p>I support the definition of your <code>map_sum_range</code>, which I and I think chris called <code>series</code>; it's on my to do list</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391984):
<p>That would make your <code>multiset_sum_map_range_induction</code> theorem, which I might otherwise call <code>multiset.range_succ_map_sum</code>, just <code>series_succ</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391992):
<p>It's not called <code>induction</code> because it's not an induction principle</p>

#### [ Mario Carneiro (Mar 30 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392042):
<p>As I've said, I think it will alleviate many of the issues you are having with these sums. If you urgently need it, why not try writing it yourself? Don't worry about connecting it to <code>finset.range</code>, just prove everything directly by induction. Then we can relate it to the other ways to talk about finite sums</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392084):
<p><code>simp</code> does the multiset and finset variants, but not the list variant.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392096):
<p>Can you tell me exactly what you are suggesting I prove? I am interested in getting this done ASAP and I have some time now, term finished.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392135):
<p>I think your sketches above should enable me to prove everything</p>

#### [ Kevin Buzzard (Mar 30 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392154):
<p>Sorry about the induction name. I thought carefully about the abstract syntax of the names but I seem to have used the wrong term.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392315):
<p>I love <code>dioph.lean</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392316):
<div class="codehilite"><pre><span></span>(D∃4 $ D∃5 $ D∃6 $ D∃7 $ D∃8 $
D&amp;7 D* D&amp;7 D- (D&amp;5 D* D&amp;5 D- D.1) D* D&amp;8 D* D&amp;8 D= D.1 D∧
D&amp;4 D* D&amp;4 D- (D&amp;5 D* D&amp;5 D- D.1) D* D&amp;3 D* D&amp;3 D= D.1 D∧
D&amp;2 D* D&amp;2 D- (D&amp;0 D* D&amp;0 D- D.1) D* D&amp;1 D* D&amp;1 D= D.1 D∧
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392318):
<p>who could fail to love that bit</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392359):
<p>whatever is going on in that file</p>

#### [ Mario Carneiro (Mar 30 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392429):
<p>That's the closest lean comes to a domain specific language right now</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392482):
<p>So there is <code>vector</code> and <code>vector3</code>. Is there a <code>vector2</code>? I can't find it. (<code>fin2</code> is used to build <code>vector3</code>)</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392530):
<p>I have a Masters student working on Matiesevich's theorem for their project, so I showed them <code>dioph.lean</code>. They know no Lean. I'm not sure they found it very helpful.</p>

#### [ Mario Carneiro (Mar 30 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392536):
<p>There was once a vector2, but I deleted it because it wasn't needed. <code>vector2</code> was inductively defined by</p>
<div class="codehilite"><pre><span></span>inductive vector2 (A : Type u) : nat -&gt; Type u
| nil : vector2 0
| cons (n) : A -&gt; vector2 n -&gt; vector2 (succ n)
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392542):
<p>From the names, you can guess that <code>vector</code>, <code>vector2</code> and <code>vector3</code> are all isomorphic</p>

#### [ Mario Carneiro (Mar 30 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392596):
<p>I think you can find it in the file history of <code>dioph.lean</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393725):
<p>I can't believe it. I feel like I have learnt something new about induction today, and I have been teaching it for 20 years.</p>

#### [ Kenny Lau (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393765):
<p>what is it?</p>

#### [ Kenny Lau (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393769):
<p>well there's always more to learn :P</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393775):
<p>yes but I'm usually trying to look nearer the top</p>

#### [ Kevin Buzzard (Mar 30 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393844):
<p>There is one abstract principle of induction <code>g := lam n, sum_to_n f</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393898):
<p>which you can prove assuming a hypothesis of the form <code>\forall n, g (succ n) = g n + f n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393911):
<p>but the problem is that there are several ways to encode <code>sum_to_n</code>in Lean</p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393915):
<p>e.g. the "pure" way via an inductive type</p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393963):
<p>or ways which create an auxiliary type along the way, like <code>sum_to_n f = ((list.range n).map f).sum</code> which at some point builds a list and then sums over it</p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394065):
<p>and for each of these design decisions about how you're going to sum this series (e.g. a design decision that some other program has forced upon you) you are given a definition of <code>sum_to_n : (ℕ → R) → (ℕ → R)</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394071):
<p>(e.g. <code>λ f, λ n ((list.range n).map f).sum</code> )</p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394119):
<p>it's now your job to prove <code>∀ n, sum_to_n (succ n) = sum_to_n n + f n</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394220):
<p>And that's quite annoying because list doesn't deconstruct like that.</p>

#### [ Kenny Lau (Mar 30 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394520):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> do you have a list of goals?</p>

#### [ Kevin Buzzard (Mar 30 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394527):
<p>I'm writing a blog post about it. This has been a most enjoyable day.</p>

#### [ Kenny Lau (Mar 30 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394727):
<blockquote>
<p>it's now your job to prove <code>∀ n, sum_to_n (succ n) = sum_to_n n + f n</code></p>
</blockquote>
<p>done</p>

#### [ Kenny Lau (Mar 30 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394764):
<div class="codehilite"><pre><span></span>theorem sum_to_n.succ : sum_to_n (n+1) = sum_to_n n + f n :=
begin
  dsimp [sum_to_n],
  rw [list.range_concat],
  rw [list.map_append],
  rw [list.sum_append],
  rw [list.map_singleton],
  rw [list.sum_cons],
  rw [list.sum_nil],
  rw [add_zero]
end
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394965):
<p>version 2</p>

#### [ Kenny Lau (Mar 30 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394966):
<div class="codehilite"><pre><span></span>theorem sum_to_n.succ : sum_to_n (n+1) = sum_to_n n + f n :=
by simp [sum_to_n, list.range_concat]
</pre></div>

#### [ Kevin Buzzard (Mar 30 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399570):
<p><a href="https://wordpress.com/post/xenaproject.wordpress.com/1344" target="_blank" title="https://wordpress.com/post/xenaproject.wordpress.com/1344">https://wordpress.com/post/xenaproject.wordpress.com/1344</a></p>

#### [ Kenny Lau (Mar 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399701):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> did you sleep?</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399746):
<p>Meh <a href="https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/" target="_blank" title="https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/">https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/</a> is better</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399747):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> or <span class="user-mention" data-user-id="110064">@Kenny Lau</span> Feel free to leave comments if you have definitions for <code>sum_to_n</code></p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399750):
<blockquote>
<p>but, unfortunately, because I fear that in practice people really might occasionally find themselves in a situation where they need a new kind of proof by induction </p>
</blockquote>
<p>writing new recursion principles is common and expected, from what i've seen out there</p>

#### [ Kenny Lau (Mar 30 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399807):
<p>“using the fucking ring tactic”</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399819):
<p>you can see some of this in mathlib, where new elimination lemmas are defined fairly frequently</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399859):
<p>if we go back to the nats, strong induction is commonplace yet requires a proof</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399920):
<p>In lean web editor link, <code>tactic.ring</code> is not available so I had to prove it the old skool way! Thank you <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> for <code>tactic.ring</code>. No, it appears I didn't go to sleep and now the sun is up. Crap. I'm behaving like a kid.</p>

#### [ Kenny Lau (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399923):
<p>lol</p>

#### [ Kenny Lau (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399972):
<p>i am shocked</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399975):
<blockquote>
<p>writing new recursion principles is common and expected, from what i've seen out there</p>
</blockquote>
<p>I realised that Chris could solve his problem with good recursion principles.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399979):
<p>I don't have to be up at 7am though, because the kids have finished school now.</p>

#### [ Kenny Lau (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399987):
<p>so the philosophy is to always write eliminators for the things you create?</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399988):
<p>If I don't get my act together I'll be up at 7am anyway.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399992):
<p>I guess that might be what I am saying.</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399993):
<p>also as a matter of style, you could give names to your function variables as opposed to always lambda-ing them</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399994):
<p>Or some version of this.</p>

#### [ Kenny Lau (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399995):
<p>i am still shocked <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400038):
<p>for example <code>def square : ℕ → ℕ := λ i, i ^ 2 </code> could be <code>def square n : nat := n ^ 2</code></p>

#### [ Kenny Lau (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400039):
<p>fin has no eliminator though</p>

#### [ Kenny Lau (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400040):
<p>hence the problem</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400041):
<p>yes, my approach with fin was not much fun.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400042):
<p>But I need to sleep.</p>

#### [ Kenny Lau (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400045):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> I think he decided he does not care about styles</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400048):
<p>I just wrote it in the way that appealed to me most.</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400052):
<p>I have also written three solutions to the problems.</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400053):
<p>when you're a professor, you can write your homework exercises however you like, haha</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400093):
<p>One of them is just "axiom axiom constant" etc etc, and it's very cool, you can still do the last part :-)</p>

#### [ Kenny Lau (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400096):
<p>constant name : false</p>

#### [ Kenny Lau (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400097):
<p>theorem RH : sorry := false.elim name</p>

#### [ Kevin Buzzard (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400099):
<p>I might be a professor but I am still very much a learner at this game. I'd be happy for any more stylistic comments.</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400142):
<p>it's only really meaningful in large, complicated definitions</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400143):
<p>of which square does not count</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400146):
<p>i will continue to file nitpicking issues if i see them, though</p>

#### [ Andrew Ashworth (Mar 30 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400603):
<p>actually later on you give summand a nice name so i take back everything i wrote, haha</p>

#### [ Kevin Buzzard (Mar 30 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400647):
<p>In fact my initial draft had an error in which I only spotted when I tried to prove that my genuine summing function was equal the one I defined with constants and axioms</p>

#### [ Chris Hughes (Mar 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124407580):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I did define sums and sums between nats here. <a href="https://github.com/dorhinj/lean/blob/master/sum_between_nats.lean" target="_blank" title="https://github.com/dorhinj/lean/blob/master/sum_between_nats.lean">https://github.com/dorhinj/lean/blob/master/sum_between_nats.lean</a> The proofs aren't mathlib ready and I don't think series is a particularly good name. I proved various basic properties as well.</p>


{% endraw %}

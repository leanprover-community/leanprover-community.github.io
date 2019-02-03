---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87044linarithfailure.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [linarith failure](https://leanprover-community.github.io/archive/116395maths/87044linarithfailure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jan 17 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363230):
<p>I've started doing basic analysis in Lean with the undergraduates and I'm really using <code>linarith</code> a lot, it's really handy for this sort of thing. I was trying to prove that 1/n tended to zero using it, and I ran into this: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">c</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span> <span class="c1">-- fails</span>
</pre></div>


<p>Is that a bug, or am I asking too much?</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363405):
<p>that looks like a bug</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363437):
<p>does <code>generalize : 1/a = x; linarith</code> work?</p>

#### [ Rob Lewis (Jan 17 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363577):
<p>Yeah, that should be within scope. I'm guessing it's still too aggressive about ignoring nonlinear things, instead of trying to work with the linear parts. I fixed something related a while back iirc, but maybe not enough.</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363825):
<p><code>linarith h1 h2</code> should work if it's a filtering problem</p>

#### [ Kevin Buzzard (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363832):
<p>Yes, generalizing works.</p>

#### [ Kevin Buzzard (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363853):
<p><code>linarith</code> takes arguments??</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363871):
<p>apparently (reading the src now)</p>

#### [ Rob Lewis (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363877):
<p>It might reject it at the parsing step though.</p>

#### [ Rob Lewis (Jan 17 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363904):
<p>I'll look into it soon.</p>

#### [ Rob Lewis (Jan 17 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363935):
<p>linarith takes arguments, in case you have lots of hypotheses and know which ones are contradictory.</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365130):
<p>PS this was great:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">abs</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">abs</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">max</span><span class="o">,</span>
  <span class="c1">-- goal with three ite&#39;s in</span>
  <span class="n">split_ifs</span><span class="o">,</span>
  <span class="c1">-- 8 goals</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">linarith</span><span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365202):
<p>You can replace that <code>, repeat</code> with a <code>;</code></p>

#### [ Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365214):
<p>But that's less readable</p>

#### [ Patrick Massot (Jan 17 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365246):
<p>It requires knowing what <code>;</code> does, but then it's readable</p>

#### [ Rob Lewis (Jan 17 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366709):
<p>This is buried a little deeper than I expected. It's a mistake in the part of <code>linarith</code> that normalizes non-integer coefficients (in <code>norm_hyp_aux</code> I think). I'll fix it, but not tonight.</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366787):
<p>Thanks for chasing this up! I really want to let undergraduates see that doing basic analysis in Lean is really easy, the triangle inequality proof went down really well!</p>

#### [ Patrick Massot (Jan 17 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366901):
<p>I'm also very interested in this. Do you have files to share?</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366917):
<p>I've only given one lecture so far and I've done barely anything.</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367083):
<p><a href="https://github.com/ImperialCollegeLondon/M1P1-lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean">https://github.com/ImperialCollegeLondon/M1P1-lean</a></p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367161):
<p>I proved a sequence has at most one limit; I used ring to prove things like e + e = 2 * e and Kenny was in the front row exploding.</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367175):
<p>But I can't teach all the students the 100 lemmas each of which can be proved by ring</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367186):
<p>I want to just teach them ring instead</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367420):
<p>My plan is to track their lectures and prove the interesting theorems as they're proved in class.</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367472):
<p>wow, you really jumped right in</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367509):
<p>in the ITP class Jeremy and I are teaching we've barely got to what a <code>def</code> is, how <code>variable</code> and <code>section</code> work and so on</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367534):
<p>I asked the lecturer. He said that he was going to assume that the reals were a complete archimedean field and develop everything from that.</p>

#### [ Patrick Massot (Jan 17 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367547):
<p>This is why we need mathematicians to teach proof assistants</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367632):
<p>so my plan was to spend the term trying to prove the things he proved, but in Lean. I would imagine that many of them are in mathlib already, but I didn't even look at the definition of a sequence tending to a limit in case it used cofinite filters. Of course I used the epsilon / N definition, because that's what they're told.</p>

#### [ Rob Lewis (Jan 17 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/156324714):
<p>Never mind, I fixed it tonight. There could be some similar cases that this fix misses though.</p>

#### [ Kevin Buzzard (Jan 24 2019 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/156771005):
<p>I have another linarith failure. The hypotheses involving <code>N</code> and <code>n</code> are irrelevant to the goal, and if you comment out the line with them in then linarith succeeds, but if you leave them in then it fails.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span>
<span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hirrelevant</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="n">N</span><span class="o">)</span> <span class="c1">-- comment out this line to fix</span>
<span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">-</span> <span class="n">l</span> <span class="bp">≤</span> <span class="bp">-</span><span class="o">(</span><span class="n">A</span> <span class="bp">-</span> <span class="n">l</span><span class="o">))</span> <span class="o">(</span><span class="n">h_1</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">≤</span> <span class="bp">-</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">h_2</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">l</span> <span class="bp">≤</span> <span class="bp">-</span><span class="n">l</span><span class="o">)</span>
<span class="o">(</span><span class="n">h_3</span> <span class="o">:</span> <span class="bp">-</span><span class="o">(</span><span class="n">A</span> <span class="bp">-</span> <span class="n">l</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>  <span class="n">A</span> <span class="bp">&lt;</span> <span class="n">l</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">done tactic failed, there are unsolved goals</span>
<span class="cm">...</span>
<span class="cm">⊢ ↑(2 * -1) + 2 = 0</span>
<span class="cm">-/</span>
</pre></div>

#### [ Rob Lewis (Jan 24 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/156777566):
<p>Yeah, I know what's going on here. <code>linarith</code> is actually "succeeding," but <code>Hirrelevant</code> convinced it it was working over <code>int</code> instead of <code>real</code>, so it builds the wrong proof of contradiction. I'm on it.</p>

#### [ Rob Lewis (Jan 24 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/156777590):
<p>In the meantime, you can help it out by calling <code>linarith {restrict_type := ℝ}</code> instead.</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157057941):
<p>Is this expected behaviour? </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">b</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">linarith</span><span class="o">,</span> <span class="c1">-- fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">linarith failed to find a contradiction</span>
<span class="cm">state:</span>
<span class="cm">a b : ℤ,</span>
<span class="cm">h : a &lt; b,</span>
<span class="cm">c : ℤ := b,</span>
<span class="cm">a_1 : a ≥ c</span>
<span class="cm">⊢ false</span>
<span class="cm">-/</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>In practice I have some positive real <code>eps := (b - a) / 2</code> which is mentioned in several hypotheses  and the conclusion. I can close my goal with lots of <code>change</code> or <code>show</code> commands removing all the <code>eps</code>'s and then running <code>linarith</code> after, but my understanding of the internals of <code>linarith</code> is sufficiently poor that I don't know whether I should expect the tactic to handle these variables defined in terms of other variables or whether they're my problem.</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157058260):
<p>Aah, I can do <code>have Heps : eps = (b - a) / 2 := rfl, rw Heps at *</code> as a workaround :-) I don't know any other way of doing multiple substitutions at once.</p>

#### [ Reid Barton (Jan 28 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157058397):
<p>Do you need the <code>rw</code>? After all <code>eps = (b - a) / 2</code> is also a linear constraint</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157058484):
<p>Well spotted :-) Yes, it works fine in my (quite complicated) use case. Excellent trick!</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157058742):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">b</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">c</span><span class="o">,</span>
  <span class="c1">-- linarith, -- fails</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">linarith</span><span class="o">,</span> <span class="c1">-- works</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jan 28 2019 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157058940):
<p>It's funny that <code>c := b</code> shows up in my local context, but the hypothesis that c = b is apparently not in it. If the let were syntactic sugar, I wouldn't need the have, right? I'm not entirely sure what's going on here. Hmm, oh OK, maybe c is defined to be b, and Lean knows this but the fact isn't in the local context. I guess I'm showing my ignorance of how things really work here. I was hoping <code>unfold eps</code> would work in my case but it didn't.</p>

#### [ Reid Barton (Jan 28 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157060217):
<p>It seems like tactics like <code>rw</code> and <code>simp</code> sometimes "see through" let-bound variables, and I never understood exactly when or why</p>

#### [ Rob Lewis (Jan 28 2019 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157060491):
<blockquote>
<p>maybe c is defined to be b</p>
</blockquote>
<p>This is roughly right, a <code>let</code> is like a local <code>def</code>. It's not syntactic sugar.</p>
<blockquote>
<p>but the fact isn't in the local context</p>
</blockquote>
<p>The information is in the type context, which is why you see <code>c : Z := b</code>. There's no term of type <code>c = b</code> until you add it manually. I don't think <code>linarith</code> should unfold <code>let</code> bindings, since they can be used to hide arbitrarily large terms. It's analogous to unfolding definitions (which <code>linarith</code> doesn't do and shouldn't do).</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061190):
<p>Thanks for the clarification Rob. I didn't like my original solution (lots of 'change') but I'm happy to add the hypothesis that <code>c</code> equals its definition to the context and then let <code>linarith</code> take over. I have over 20 occurrences of <code>linarith</code> in <a href="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean">https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean</a> so far; it's an essential tactic for this sort of thing.</p>

#### [ Patrick Massot (Jan 28 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061326):
<p>Did you tried also using <code>mono</code>?</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061337):
<p>I don't know what that does.</p>

#### [ Kevin Buzzard (Jan 28 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061346):
<p>Isn't it some disease in the US?</p>

#### [ Patrick Massot (Jan 28 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061489):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#mono" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#mono">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#mono</a></p>

#### [ Patrick Massot (Jan 28 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061576):
<p>There is also <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#apply_rules" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#apply_rules">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#apply_rules</a></p>

#### [ Patrick Massot (Jan 28 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061835):
<p>but apply_rules seems very slow</p>

#### [ Patrick Massot (Jan 28 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157061960):
<p>You can try to stick the following into  your limits file:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- Next lemma could be either hidden of given a user-friendly proof</span>
<span class="kn">lemma</span> <span class="n">zero_of_abs_lt_all</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">eq_zero_of_abs_eq_zero</span> <span class="err">$</span> <span class="n">eq_of_le_of_forall_le_of_dense</span> <span class="o">(</span><span class="n">abs_nonneg</span> <span class="n">x</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span> <span class="n">le_of_lt</span> <span class="o">(</span><span class="n">h</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">)</span>

<span class="c1">-- The next few things should be hidden</span>
<span class="bp">@</span><span class="o">[</span><span class="n">user_attribute</span><span class="o">]</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">ineq_rules</span> <span class="o">:</span> <span class="n">user_attribute</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">name</span> <span class="o">:=</span> <span class="bp">`</span><span class="n">ineq_rules</span><span class="o">,</span>
  <span class="n">descr</span> <span class="o">:=</span> <span class="s2">&quot;lemmas usable to prove inequalities&quot;</span> <span class="o">}</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">ineq_rules</span><span class="o">]</span> <span class="n">add_lt_add</span> <span class="n">le_max_left</span> <span class="n">le_max_right</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">obvious_ineq</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">linarith</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply_rules</span> <span class="n">ineq_rules</span><span class="o">]</span>
<span class="n">run_cmd</span> <span class="n">add_interactive</span> <span class="o">[</span><span class="bp">`</span><span class="n">obvious_ineq</span><span class="o">]</span>
<span class="c1">-- end of scary things</span>

<span class="c1">-- We&#39;re ready to prove the theorem.</span>
<span class="kn">theorem</span> <span class="n">limits_are_unique</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">m</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">hl</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">l</span><span class="o">)</span>
<span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- Let prove |l - m| is smaller than any positive number, since that will easily imply l = m</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">,</span>
    <span class="k">from</span> <span class="n">eq_of_sub_eq_zero</span> <span class="o">(</span><span class="n">zero_of_abs_lt_all</span> <span class="bp">_</span> <span class="n">this</span><span class="o">),</span>
  <span class="c1">-- Let ε be any positive number, and let&#39;s prove |l - m| &lt; ε</span>
  <span class="n">intros</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span>
  <span class="c1">-- Because aₙ → l, there exists Nₗ such that n ≥ Nₗ → |aₙ - l| &lt; ε/2</span>
  <span class="n">cases</span> <span class="n">hl</span> <span class="o">(</span><span class="n">ε</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">obvious_ineq</span><span class="o">)</span> <span class="k">with</span> <span class="n">Nₗ</span> <span class="n">Hₗ</span><span class="o">,</span>
  <span class="c1">-- Because aₙ → m, there exists Nₘ such that n ≥ Nₘ → |aₙ - m| &lt; ε/2</span>
  <span class="n">cases</span> <span class="n">hm</span> <span class="o">(</span><span class="n">ε</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">obvious_ineq</span><span class="o">)</span> <span class="k">with</span> <span class="n">Nₘ</span> <span class="n">Hₘ</span><span class="o">,</span>
  <span class="c1">-- The trick is to let N be the max of Nₗ and Nₘ</span>
  <span class="k">let</span> <span class="n">N</span> <span class="o">:=</span> <span class="n">max</span> <span class="n">Nₗ</span> <span class="n">Nₘ</span><span class="o">,</span>
  <span class="c1">-- Now clearly N ≥ Nₗ...</span>
  <span class="k">have</span> <span class="n">H₁</span> <span class="o">:</span> <span class="n">Nₗ</span> <span class="bp">≤</span> <span class="n">N</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">obvious_ineq</span><span class="o">,</span>
  <span class="c1">-- ... so |a_N - l| &lt; ε/2</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">|</span> <span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">l</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:=</span> <span class="n">Hₗ</span> <span class="n">N</span> <span class="n">H₁</span><span class="o">,</span>
  <span class="c1">-- similarly N ≥ Nₘ...</span>
  <span class="k">have</span> <span class="n">H₂</span> <span class="o">:</span> <span class="n">Nₘ</span> <span class="bp">≤</span> <span class="n">N</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">obvious_ineq</span><span class="o">,</span>
  <span class="c1">-- ... so |a_N - m| &lt; ε/2 too</span>
  <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:</span> <span class="bp">|</span> <span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:=</span> <span class="n">Hₘ</span> <span class="n">N</span> <span class="n">H₂</span><span class="o">,</span>
  <span class="c1">-- We now combine</span>
  <span class="n">exact</span> <span class="k">calc</span> <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">≤</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">+</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">l</span><span class="bp">|</span> <span class="o">:</span> <span class="n">triangle&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
   <span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="bp">+</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">obvious_ineq</span>
   <span class="bp">...</span> <span class="bp">=</span> <span class="n">ε</span> <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Jan 28 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157062049):
<p>Note that you can put <code>triangle'</code> into the list of obvious inequalities and get all inequalities proved for free, but this would probably be cheating</p>

#### [ Kevin Buzzard (Jan 28 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157063086):
<p>Can this do the product of limits is limit of product?</p>

#### [ Kevin Buzzard (Jan 28 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157063094):
<p>That was horrible</p>

#### [ Kevin Buzzard (Jan 28 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157063115):
<p><a href="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/87f2b5b4dc741c5d44751678e37229c1964799e3/src/limits.lean#L299" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/87f2b5b4dc741c5d44751678e37229c1964799e3/src/limits.lean#L299">https://github.com/ImperialCollegeLondon/M1P1-lean/blob/87f2b5b4dc741c5d44751678e37229c1964799e3/src/limits.lean#L299</a> That was where it started going wrong</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157065227):
<p><code>linarith</code> seems to know <code>add_lt_add</code> for the reals.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157067936):
<p><a href="#narrow/stream/116395-maths/topic/nonlinarith/near/157067630" title="#narrow/stream/116395-maths/topic/nonlinarith/near/157067630">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067630</a> Got it, thanks to you and Reid.</p>

#### [ Patrick Massot (Jan 29 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157088858):
<p>Actually I also don't like your <code>triangle'</code>. Remembering 10 versions of the triangle inequality is not how we teach this. You can do:</p>
<div class="codehilite"><pre><span></span>  <span class="k">calc</span>
    <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">=</span> <span class="bp">|</span><span class="o">(</span><span class="n">l</span> <span class="bp">-</span> <span class="n">a</span> <span class="n">N</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="o">)</span><span class="bp">|</span> <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span>
        <span class="bp">...</span> <span class="bp">≤</span> <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">a</span> <span class="n">N</span><span class="bp">|</span> <span class="bp">+</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">obvious_ineq</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">l</span> <span class="bp">|</span> <span class="bp">+</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">abs_sub</span>
        <span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="bp">+</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span>               <span class="o">:</span> <span class="k">by</span> <span class="n">obvious_ineq</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">ε</span>                       <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span><span class="o">,</span>
</pre></div>


<p>where the only painful part is this <code>rw abs_sub</code>. I added <code>abs_add</code>, which is the regular triangle inequality for abs, to the <code>obvious_ineq</code> rules, but it's probably better to explicitly use it since it's a key part of the argument</p>

#### [ Patrick Massot (Jan 29 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157088863):
<p>simply replace that <code>by obvious_ineq</code> with <code>abs_add _ _</code></p>

#### [ Patrick Massot (Jan 29 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157088922):
<p>I'll do limits of products tonight if I have time, and if I'm not too depressed about trying to use Lean for teaching (my first lecture using Lean will be at the end of this afternoon)</p>

#### [ Johan Commelin (Jan 29 2019 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157090831):
<p>Good luck Patrick!</p>

#### [ Johan Commelin (Jan 29 2019 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157090851):
<p>And I really like your little tactics!</p>

#### [ Jeremy Avigad (Jan 29 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157104340):
<p>A thought: it might be useful to have a tactic <code>set</code> that does what Kevin wants, i.e. a version of <code>let</code> that puts an equality in the context. For example, <code>set h : a = t</code> would create a new variable <code>a</code>, and put <code>h : a = t</code> into the context. Under the hood, <code>set</code> changes the goal <code>G</code> to <code>forall a, a = t -&gt; G</code>, and then introduces the hypotheses. It's a combination of noting <code>t = t</code>, reverting, generalizing, and introducing. (But maybe there is already a nice way to do this?)</p>

#### [ Rob Lewis (Jan 29 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157106342):
<p>It seems more natural to use a <code>let</code> to do that. Why not preserve the definitional equality?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">set</span> <span class="o">(</span><span class="n">a</span> <span class="n">h</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">tp</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">v</span><span class="o">,</span>
   <span class="n">nv</span> <span class="err">←</span> <span class="n">definev</span> <span class="n">a</span> <span class="n">tp</span> <span class="n">v</span><span class="o">,</span>
   <span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="err">%%</span><span class="n">nv</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">v</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">assert</span> <span class="n">h</span><span class="o">,</span>
   <span class="n">reflexivity</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">set</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;:&quot;</span><span class="o">))</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;:=&quot;</span><span class="o">))</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">i_to_expr</span> <span class="n">v</span> <span class="bp">&gt;&gt;=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">set</span> <span class="n">a</span> <span class="n">h</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">set</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Jeremy Avigad (Jan 29 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157108335):
<p>Looks good to me!</p>

#### [ Kevin Buzzard (Jan 29 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109507):
<p>The syntax looks a bit funny, it looks like h has type n :-/</p>

#### [ Rob Lewis (Jan 29 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109611):
<p>It is unfortunately not analogous to <code>let h : n := x + y</code>. Better suggestion?</p>

#### [ Kevin Buzzard (Jan 29 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109680):
<p>I remember always being muddled by <code>generalize</code>...</p>

#### [ Rob Lewis (Jan 29 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109722):
<p><code>set n := x + y using h</code>?</p>

#### [ Kevin Buzzard (Jan 29 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109742):
<p>maybe that's better!</p>

#### [ Kevin Buzzard (Jan 29 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157109750):
<p>cool little parser exercise to do now :-)</p>

#### [ Johan Commelin (Jan 29 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157110988):
<p><code>set n := x + y with h</code> in analogy with <code>cases ... with</code> etc.<br>
I think <code>using</code> will "use" one of your current hypotheses, or some expression (like in <code>simpa</code>),<br>
whereas <code>with</code> gives names for new hypotheses.</p>

#### [ Sebastien Gouezel (Jan 29 2019 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157120730):
<p>Is it possible to even get <code>let n := x + y with h</code>?</p>

#### [ Patrick Massot (Jan 29 2019 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157131673):
<p>In addition to syntax discussions, the question is whether this tactic should replace <code>x+y</code> by <code>n</code> everywhere, or only in the goal, or nowhere.</p>

#### [ Johan Commelin (Jan 29 2019 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157131920):
<p>In the example that Rob posted, associativity would prevent a naive replacement to yield <code>n+n+n = 5</code>, right? So then the replacement algorithm needs to know about associativity, and it becomes complicated.</p>

#### [ Rob Lewis (Jan 29 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157134524):
<p>Yeah, the example doesn't illustrate this very well. Maybe a variant <code>set! n := x + y with h</code> could try <code>simp only [h.symm] at *</code> at the end. But I think it's better not to do this by default, to match the behavior of <code>let</code>.</p>

#### [ Rob Lewis (Jan 29 2019 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157134602):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> <code>tactic.interactive.let</code> is defined in core, so I'm afraid not.</p>

#### [ Rob Lewis (Feb 01 2019 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346025):
<p>I've added this. The basic syntax is <code>set n := x + y with h</code>. Alternatives: <code>set! n := x + y with h</code> will rewrite <code>x + y</code> to <code>n</code> everywhere it can. <code>set n := x + y with h⁻¹</code> will make the equality proof face the other direction.</p>

#### [ Rob Lewis (Feb 01 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346068):
<p>I ended up needing this tactic for something I was doing yesterday, heh. It also led me to another bug in <code>linarith</code>.</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346771):
<p>how is this different from <code>let</code>?</p>

#### [ Rob Lewis (Feb 01 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346836):
<p>It adds a hypothesis that states the new definition propositionally.</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346840):
<p>is it also a let?</p>

#### [ Rob Lewis (Feb 01 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346844):
<p>Yes.</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346868):
<p>I think the <code>set n := x + y</code> variant may also be useful - no equality assumption, but <code>x + y</code> gets replaced by <code>n</code></p>

#### [ Mario Carneiro (Feb 01 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346928):
<p>I think that <code>set!</code> should be the default behavior, I'm not sure where the <code>set</code> behavior is better</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157346961):
<p>also I suggest <code>&lt;- h</code> instead of <code>h⁻¹</code> for the reversed proof - we haven't used the inverse symbol for symmetry since lean 2</p>

#### [ Kenny Lau (Feb 01 2019 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347045):
<p>Next time could we discuss the details before making changes to the mathlib in order to minimize changes to <code>tactic/interactive.lean</code>?</p>

#### [ Rob Lewis (Feb 01 2019 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347099):
<p>I chose this as the default because <code>set!</code> sometimes reorders hypotheses, which is a little annoying if you don't care. It's not a big deal though, I can change it. Sure, the behavior without an equality hypothesis sounds good, as well as the notation.</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347114):
<p>I hope that the changes can be obtained by <code>change</code> rather than <code>rw</code></p>

#### [ Rob Lewis (Feb 01 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347134):
<p><code>change at *</code> seems to have a bug, it fails completely.</p>

#### [ Rob Lewis (Feb 01 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347140):
<p>Or rather, it succeeds without doing anything.</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347202):
<p>you have to do it somewhat manually with the noninteractive change</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347215):
<p>you revert the relevant hypotheses then use <code>tactic.change</code></p>

#### [ Rob Lewis (Feb 01 2019 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347314):
<p>I'll give it another shot. I tried this first, but it was behaving strangely.</p>

#### [ Rob Lewis (Feb 01 2019 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157347319):
<p>Gotta run, lunchtime.</p>

#### [ Sebastien Gouezel (Feb 01 2019 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/157363142):
<p><code>set</code>-related question, although indirectly. I have an element of <code>fin n</code> given by a complicated formula, to which I would like to give a name for clarity. <code>let x := complicated_expression</code> works fine, but it would even be more useful for me to give a name to the fields of <code>x</code> directly, i.e., to write <code>let ⟨i, hi⟩ := complicated_expression</code>. This does not work. I can define <code>x</code>, and then <code>let i := x.1, let hi := x.2</code>, but then the fact that <code>⟨i, hi⟩ = complicated_expression</code> is not refl, it requires a proof based for instance on <code>fin.ext_iff</code>. All this looks like useless plumbing to me. Is there a nice syntax to do this that I am unaware of?</p>


{% endraw %}

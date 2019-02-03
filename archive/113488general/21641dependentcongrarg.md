---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21641dependentcongrarg.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [dependent congr_arg?](https://leanprover-community.github.io/archive/113488general/21641dependentcongrarg.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 23 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575693):
<p>I am assuming this is provable: <code>example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := sorry</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575733):
<p>The goal is <code>P f H2 = P g _</code>, and we have <code>H1 : f = g</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575737):
<p>but I can't rewrite</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575741):
<p>because <code>H2</code> is a proof of something involving f</p>

#### [ Simon Hudon (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575781):
<p>Have you tried <code>congr</code>?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575786):
<p>I would have to rewrite <code>f</code> and <code>H2</code> simultaneously.</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575789):
<p>use congr</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575795):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575798):
<p>Thanks!</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575806):
<p>So what does congr do?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575814):
<p>By which I mean</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575818):
<p>how would I do this in term mode</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575829):
<p>simp should also work here</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575836):
<p>I thought I tried it and it failed</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575846):
<p>simp doesn't work</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575849):
<p>that was what made me ask</p>

#### [ Patrick Massot (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575853):
<p>Kevin, you should spend more time reading documentation</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575856):
<p>?</p>

#### [ Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575895):
<p><code>example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := by cc</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575903):
<p>you win</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575907):
<p>:-)</p>

#### [ Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575908):
<p><a href="https://github.com/leanprover/mathlib/pull/114" target="_blank" title="https://github.com/leanprover/mathlib/pull/114">https://github.com/leanprover/mathlib/pull/114</a></p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575911):
<p>Yes, I saw it, and I even read Gabriel's explanation of what cc did</p>

#### [ Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575913):
<p>Oh, Gabriel wrote some comment</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575916):
<p>But the bottom line is that I still don't know what's going on</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575926):
<p>all I know is that I'm relieved to find that I'm trying to prove something which is true</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575941):
<p>Some months ago I would just have been happy to accept the magic</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575945):
<p>but now I am more interested in knowing how the magic works</p>

#### [ Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575981):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">h</span><span class="o">,</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="n">h</span><span class="o">)</span> <span class="bp">_</span>
</pre></div>

#### [ Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575987):
<p>For example I don't see how to use <code>congr_arg</code> or <code>congr_fun</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575994):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">drec_on</span> <span class="n">H1</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576000):
<p>Thanks Kenny</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576007):
<p>I was about to say "how do you prove this from <code>eq.rec</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576008):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">subst</span> <span class="n">H1</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576011):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H1</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576012):
<p>what is this <code>subst</code>?</p>

#### [ Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576016):
<p>tactic</p>

#### [ Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576026):
<p>takes hypothesis of the form <code>[expr] = h</code> or <code>h = [expr]</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576029):
<p>where <code>h</code> is any variable</p>

#### [ Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576035):
<p>and discharge the hypothesis while substituting everything</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576037):
<p>I like the subst proof best, in some sense, because it is closest to how I am thinking about what needs to be done</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576052):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I now realise that <code>simp</code> by itself had no chance of working :-)</p>

#### [ Kenny Lau (Apr 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576134):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">subst</span> <span class="n">H1</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=</span>
<span class="cm">λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),</span>
<span class="cm">  eq.drec (eq.refl (P f H2)) H1</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576217):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">drec</span> <span class="n">rfl</span> <span class="n">H1</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576221):
<p>should be the shortest term mode solution</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576226):
<p>The subst proof only works because one side is a variable here, but it is able to avoid the DTT problems that many other tactics have to face in this situation</p>

#### [ Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576287):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">),</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">rfl</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576298):
<p>what is so funny about that</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576299):
<p><code>simp</code> and <code>congr</code> both work by using congruence lemmas. These are generated on the fly and the term for them is a bit complicated but the structure is similar: from <code>a = b</code> and <code>c = d</code> derive <code>f a c = f a b</code>.</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576321):
<p>The real power is that the generated congruence lemma automatically makes use of subsingletons to avoid hypotheses, meaning that if <code>c</code> and <code>d</code> are proofs then you only have one hypothesis there</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576372):
<p>the <code>rfl</code> proof there is the term mode equivalent of <code>by subst</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576377):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">H1</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576409):
<blockquote>
<p>the <code>rfl</code> proof there is the term mode equivalent of <code>by subst</code></p>
</blockquote>
<p>depends on what you mean by equivalent</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576448):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">h</span><span class="o">,</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="n">h</span><span class="o">)</span> <span class="bp">_</span>
</pre></div>


</blockquote>
<p>This one is my favourite :-)</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576451):
<p>and <code>subst</code> is basically the same as <code>cases</code> or <code>induction</code> on an equality (although it does additional equality specific stuff like symmetry)</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576459):
<p>Oh I just saw the <code>|</code> one :-)</p>

#### [ Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576460):
<p>I think the <code>rfl</code> proof is equivalent to <code>by cases</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576472):
<p>and the <code>by subst</code> one is equivalent to <code>eq.drec</code></p>

#### [ Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576475):
<p>(because <code>eq.drec</code> is the proof generated by <code>by subst</code>)</p>

#### [ Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576482):
<p>(and the <code>| rfl</code> one is really invoking the inductive type and equality between constructors</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576487):
<p>like I said, they are all the same</p>

#### [ Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576501):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">H1</span><span class="bp">;</span> <span class="n">refl</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=</span>
<span class="cm">λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),</span>
<span class="cm">  eq.dcases_on H1</span>
<span class="cm">    (λ (H_1 : g = f), eq.rec (λ (H1 : f = f) (H_2 : H1 == eq.refl f), eq.refl (P f H2)) (eq.symm H_1) H1)</span>
<span class="cm">    (eq.refl g)</span>
<span class="cm">    (heq.refl H1)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576512):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">),</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">rfl</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=</span>
<span class="cm">λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),</span>
<span class="cm">  eq.dcases_on H1</span>
<span class="cm">    (λ (H_1 : g = f), eq.rec (λ (H1 : f = f) (H_2 : H1 == eq.refl f), id_rhs (P f H2 = P f H2) rfl) (eq.symm H_1) H1)</span>
<span class="cm">    (eq.refl g)</span>
<span class="cm">    (heq.refl H1)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576514):
<p>they're exactly the same</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576562):
<p><code>eq.dcases_on</code> is the same as <code>eq.drec</code> I believe</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576565):
<p>no there's an id_rhs` in one but not the other</p>

#### [ Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576583):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">dcases_on</span> <span class="n">H1</span> <span class="n">rfl</span>
</pre></div>

#### [ Mario Carneiro (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576588):
<p>I think you would get the exact same term if you use <code>by refl</code> instead of <code>rfl</code> in the term proof</p>

#### [ Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576593):
<blockquote>
<p>no there's an id_rhs` in one but not the other</p>
</blockquote>
<p>aha</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576615):
<p>I like the <code>|</code> proof because it is a really powerful way of doing the substitution.</p>

#### [ Kenny Lau (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576657):
<p>the term mode equivalent is <code>cases</code></p>

#### [ Mario Carneiro (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576680):
<p>If you replace <code>f</code> and <code>g</code> by constants this proof won't work</p>

#### [ Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576691):
<p>right</p>

#### [ Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576696):
<p>you'd need to generalize</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576705):
<p>or simp</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576716):
<p>simp uses congr, so it can do dependent rewrite</p>

#### [ Kenny Lau (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576757):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">h</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">f</span> <span class="n">H2</span> <span class="bp">=</span> <span class="n">P</span> <span class="n">g</span> <span class="o">(</span><span class="n">H1</span> <span class="bp">▸</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">congr</span><span class="bp">;</span> <span class="k">from</span> <span class="n">H1</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=</span>
<span class="cm">λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),</span>
<span class="cm">  (λ (h h_1 : ℕ → ℕ) (e_1 : h = h_1) (a : h 0 = 0) (a_1 : h_1 0 = 0),</span>
<span class="cm">     (λ (h h_1 : ℕ → ℕ) (e_1 : h = h_1) (a : h 0 = 0), eq.drec (eq.refl (P h (eq.rec a (eq.refl h)))) e_1) h h_1</span>
<span class="cm">       e_1</span>
<span class="cm">       a)</span>
<span class="cm">    f</span>
<span class="cm">    g</span>
<span class="cm">    H1</span>
<span class="cm">    H2</span>
<span class="cm">    (H1 ▸ H2)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576787):
<p>I think that's the same proof term after some beta reduction</p>

#### [ Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576799):
<p>as what?</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576806):
<p>the last few</p>

#### [ Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576812):
<p>every proof is equal because of proof irrelevance</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576822):
<p>Well, modulo <code>#reduce</code> reduction I think all proofs so far are the same</p>

#### [ Kenny Lau (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576901):
<p>church rosser much</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576913):
<p>did you check out my paper? C-R is false in lean</p>

#### [ Kenny Lau (Apr 23 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576916):
<p>I couldn't find your paper</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587726):
<p>Kenny: <a href="https://github.com/digama0/lean-type-theory/releases/" target="_blank" title="https://github.com/digama0/lean-type-theory/releases/">https://github.com/digama0/lean-type-theory/releases/</a></p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587729):
<p>and the reason I'm reviving this thread is that I discovered that in my use case, not all of the solutions worked.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587794):
<p>my actual goal is <code>extend_map_of_im_unit (g ∘ of_comm_ring R S) _ = extend_map_of_im_unit (of_comm_ring R S) H</code> where <code>of_comm_ring R S</code> is a ring homomorphism, so quite a bit more structurally complicated than my toy MWE</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587818):
<p>and <code>congr</code> gave me three random goals, one of which was <code>loc R S = (R × ↥S)</code> and that might not even be true.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587820):
<p><code>cc</code> also didn't work</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587878):
<p>but Kenny's <code>eq.drec_on H1 rfl</code> worked.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587883):
<p>simp didn't work</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587896):
<p>both subst and simp complained that H1 wasn't an appropriate lemma</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587898):
<p>even though it was of the form X = Y</p>

#### [ Kevin Buzzard (Apr 23 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587957):
<p>I realise now that I am using tactics less and less, I am on the whole doing quite abstract maths and the arguments are in some sense straightforward to show from first principles, so I don't really need any tactics beyond <code>rw</code>.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588601):
<p>aargh actually none of them worked :-/ the <code>eq.drec</code> approach looks like it works, but an error appears elsewhere. <code>cases H1</code> gave me an error I'd never seen before :-)</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588610):
<div class="codehilite"><pre><span></span>cases tactic failed, unsupported equality between type and constructor indices
(only equalities between constructors and/or variables are supported, try cases on the indices):
(λ (x : R), g (of_comm_ring R S x)) = λ (r : R), ⟦(r, ⟨1, _⟩)⟧
</pre></div>

#### [ Kevin Buzzard (Apr 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588683):
<p>that's surprising because H1 is <code>of_comm_ring R S = g ∘ of_comm_ring R S</code>.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588685):
<p>I don't need this lemma, I might give up on it.</p>


{% endraw %}

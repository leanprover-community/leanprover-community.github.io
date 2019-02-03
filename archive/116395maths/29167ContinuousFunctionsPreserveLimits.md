---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29167ContinuousFunctionsPreserveLimits.html
---

## Stream: [maths](index.html)
### Topic: [Continuous Functions Preserve Limits](29167ContinuousFunctionsPreserveLimits.html)

---


{% raw %}
#### [ Rohan Mitta (Sep 26 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671259):
<p>Is this in mathlib (or anything like this)? </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">Y</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">seq</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span>
  <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">seq</span> <span class="n">filter</span><span class="bp">.</span><span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">))</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">seq</span><span class="o">)</span> <span class="n">filter</span><span class="bp">.</span><span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">))</span>
  <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johannes Hölzl (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671293):
<p>this doesn't hold. <code>f</code> needs to be continuous at <code>a</code></p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671306):
<p>he's just editing :-)</p>

#### [ Rohan Mitta (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671321):
<p>Sorry I've just updated it with continuous f</p>

#### [ Johannes Hölzl (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671367):
<p>otherwise it is composition of <code>continuous.tendsto</code>, <code>tendsto.comp</code> and <code>H</code></p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671383):
<p>Thanks again Johannes. I've never used this stuff before.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671392):
<p>so all I do is offer encouragement and tell Rohan to ask his questions here :-) [he's sitting next to me]</p>

#### [ Johannes Hölzl (Sep 26 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671475):
<p>hehe, peer proving</p>

#### [ Johannes Hölzl (Sep 26 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671498):
<p>But this lemma is the reason why we use filters. We can express a lot of things as filters, and then just compose them</p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671516):
<p>I encourage Rohan to formalise precisely the statement he needs and ask it here. I think that's a good way of learning how to think about Lean.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671528):
<p>He's almost proved the contraction mapping theorem, this is just the last bit.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671615):
<p>I could see it was going to follow from standard filter stuff, I just don't yet know how to drive filters. I am all over the road.</p>

#### [ Rohan Mitta (Sep 26 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671746):
<p>Brilliant, that worked!</p>

#### [ Patrick Massot (Sep 26 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672107):
<p>For those reading without typing: the proof that Rohan wanted is <code>tendsto.comp H (H1.tendsto a)</code> This is the point of filters: the limit lemmas don't care whether you take the limit of a sequence at infinity, the limit of a function at a point or whatever</p>

#### [ Patrick Massot (Sep 26 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672226):
<p>Extra tip for Rohan: <code>f</code>, <code>seq</code> and <code>a</code> can be implicit arguments, they can be inferred from <code>H</code> and <code>H1</code> by unification</p>

#### [ Patrick Massot (Sep 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672326):
<p>a last one: your assumptions that <code>X</code> and <code>Y</code> are metric spaces are useless. You can replace them by <code>topological_space</code> without changing anything else</p>

#### [ Patrick Massot (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672489):
<p>Note also that the proof is much shorter than the statement, and very easy to remember, so the final tip may be to erase the lemma...</p>

#### [ Kevin Buzzard (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672534):
<p><code>tendsto (λ (n : ℕ), n + 1) at_top at_top</code></p>

#### [ Kevin Buzzard (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672542):
<p>We're so close :-)</p>

#### [ Kevin Buzzard (Sep 26 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672559):
<p>Do I have to actually unravel things here?</p>

#### [ Patrick Massot (Sep 26 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673138):
<p>I did the beginning up to the point where I hate those things:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">at_top</span> <span class="n">at_top</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">s</span> <span class="n">s_in</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mem_at_top_sets</span> <span class="n">at</span> <span class="n">s_in</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">s_in</span> <span class="k">with</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mem_map</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="o">],</span>
  <span class="n">existsi</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">b</span><span class="bp">+</span><span class="mi">1</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 26 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673171):
<p>State is now <code> b ≥ a ⊢ b + 1 ≥ a</code></p>

#### [ Patrick Massot (Sep 26 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673260):
<p>Of course the <code>change</code> in the middle is purely psychological, you can remove it</p>

#### [ Patrick Massot (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673463):
<p>Full proof is</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">at_top</span> <span class="n">at_top</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">s</span> <span class="n">s_in</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mem_at_top_sets</span> <span class="n">at</span> <span class="n">s_in</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">s_in</span> <span class="k">with</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mem_map</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="o">],</span>
  <span class="n">existsi</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span> <span class="bp">_</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">H</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_succ</span> <span class="n">b</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673487):
<p>try <code>constructor</code></p>

#### [ Patrick Massot (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673511):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I guess this is yet another test for mono</p>

#### [ Patrick Massot (Sep 26 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673602):
<p>Kenny, this works but it's even more ridiculous</p>

#### [ Patrick Massot (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673625):
<p>The only acceptable answer here is a finishing tactic (mono should do the trick)</p>

#### [ Rob Lewis (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673662):
<p><code>linarith</code> should work too.</p>

#### [ Patrick Massot (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673672):
<p>true</p>

#### [ Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673741):
<p>It does!</p>

#### [ Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673758):
<p>And it's already in mathlib</p>

#### [ Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673780):
<p>Do we have the contraction mapping theorem then?</p>

#### [ Patrick Massot (Sep 26 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673899):
<p>That being said, this proof is still too handcrafted. We should prove a lemma saying that the identity of a linearly_ordered type goes to top at top, and then use a version of squeeze</p>

#### [ Rohan Mitta (Sep 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674225):
<p>I've just finished a very long proof of </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">Banach_fixed_point</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span><span class="o">)</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">is_contraction</span> <span class="n">f</span><span class="o">)</span>
<span class="o">:</span> <span class="bp">∃!</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Sep 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674398):
<p>Now you can try to break it into ten lemmas</p>

#### [ Patrick Massot (Sep 26 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674664):
<p>I need to go and do real work, but I'll be happy to read your proof once it's available</p>

#### [ Kenny Lau (Sep 26 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134675116):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>

<span class="kn">open</span> <span class="n">filter</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">at_top</span> <span class="n">at_top</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mem_at_top_sets</span><span class="o">,</span> <span class="n">mem_map_sets_iff</span><span class="o">],</span>
  <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨</span><span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="n">b</span> <span class="bp">≥</span> <span class="n">N</span><span class="o">},</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">id</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">rintro</span> <span class="n">n</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">h2</span><span class="o">,</span> <span class="n">h3</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subst</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h2</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134675982):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">f</span> <span class="n">at_top</span> <span class="n">F</span><span class="o">)</span> <span class="o">:</span>
<span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="n">at_top</span> <span class="n">F</span> <span class="o">:=</span>
<span class="n">tendsto</span><span class="bp">.</span><span class="n">comp</span> <span class="o">(</span><span class="n">tendsto_def</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">HU</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">Ha</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">1</span> <span class="n">HU</span> <span class="k">in</span>
  <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span><span class="n">Ha</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">le_trans</span> <span class="n">Hx</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">H</span>
</pre></div>

#### [ Kevin Buzzard (Sep 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134676038):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">at_top</span> <span class="n">at_top</span> <span class="o">:=</span>
<span class="n">tendsto_def</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">HU</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">Ha</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">1</span> <span class="n">HU</span> <span class="k">in</span>
  <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span><span class="n">Ha</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">le_trans</span> <span class="n">Hx</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Sep 26 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677014):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean</a></p>

#### [ Kevin Buzzard (Sep 26 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677027):
<p>He's pushed!</p>

#### [ Kevin Buzzard (Sep 26 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677164):
<p>rofl he has the vmap version of filter so it doesn't compile for me :-) I'll fix it. <span class="user-mention" data-user-id="120559">@Rohan Mitta</span> I'm editing your file so that it compiles with the most recent mathlib</p>

#### [ Kevin Buzzard (Sep 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677333):
<p><em>rofl</em> there's still a sorry! Rohan I think you hadn't saved before you pushed :-) OK so the current state of the contraction mapping theorem is that the only finished version is on a laptop owned by an undergraduate who has just gone off to prepare a treasure hunt for Fresher's week.</p>

#### [ Rohan Mitta (Sep 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134683456):
<p>Okay whoops, I've saved and pushed again. Hopefully its all there now?</p>

#### [ Patrick Massot (Sep 26 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134684774):
<p>Congratulations Rohan!</p>


{% endraw %}

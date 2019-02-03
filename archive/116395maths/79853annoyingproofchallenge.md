---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/79853annoyingproofchallenge.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [annoying proof challenge](https://leanprover-community.github.io/archive/116395maths/79853annoyingproofchallenge.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Dec 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698181):
<p>Is there a nice way to prove this?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span>
</pre></div>

#### [ Kenny Lau (Dec 01 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698441):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ordered_group</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="mi">0</span><span class="o">)</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="err">$</span> <span class="o">(</span><span class="n">add_eq_zero_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="err">$</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj</span> <span class="n">H</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span>
</pre></div>

#### [ Kenny Lau (Dec 01 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698444):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Kevin Buzzard (Dec 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698524):
<p>Didn't your mother tell you never to end a sentence with a <code>▸</code>?</p>

#### [ Chris Hughes (Dec 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698586):
<p>Maybe it's some super duper eta reduction.</p>

#### [ Kenny Lau (Dec 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698638):
<p>oops it's supposed to end in <code>rfl</code></p>

#### [ Kenny Lau (Dec 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698639):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ordered_group</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="mi">0</span><span class="o">)</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="err">$</span> <span class="o">(</span><span class="n">add_eq_zero_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="err">$</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj</span> <span class="n">H</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Dec 01 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698647):
<p>oh that works better :-)</p>

#### [ Kevin Buzzard (Dec 01 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698701):
<p>What does the equation compiler actually <em>do</em> to decide that it can ignore the <code>none</code> cases? I mean, what does it try?</p>

#### [ Kenny Lau (Dec 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698712):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ordered_group</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="mi">0</span><span class="o">)</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="err">$</span> <span class="o">(</span><span class="n">add_eq_zero_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="err">$</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj</span> <span class="n">H</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">rfl</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ {a b : with_bot ℕ}, a + b = 1 → a = 0 ∨ b = 0 :=</span>
<span class="cm">λ {a b : with_bot ℕ} (a_1 : a + b = 1),</span>
<span class="cm">  option.cases_on a</span>
<span class="cm">    (λ (a : none + b = 1),</span>
<span class="cm">       option.cases_on b</span>
<span class="cm">         (λ (a : none + none = 1),</span>
<span class="cm">            eq.dcases_on a (λ (a_1 : some 1 = none), option.no_confusion a_1) (eq.refl 1) (heq.refl a))</span>
<span class="cm">         (λ (b : ℕ) (a : none + some b = 1),</span>
<span class="cm">            eq.dcases_on a (λ (a_1 : some 1 = none), option.no_confusion a_1) (eq.refl 1) (heq.refl a))</span>
<span class="cm">         a)</span>
<span class="cm">    (λ (a : ℕ) (a_1 : some a + b = 1),</span>
<span class="cm">       option.cases_on b</span>
<span class="cm">         (λ (a_1 : some a + none = 1),</span>
<span class="cm">            eq.dcases_on a_1 (λ (a_2 : some 1 = none), option.no_confusion a_2) (eq.refl 1) (heq.refl a_1))</span>
<span class="cm">         (λ (b : ℕ) (a_1 : some a + some b = 1),</span>
<span class="cm">            nat.cases_on b (λ (a_1 : some a + some 0 = 1), id_rhs (some a = 0 ∨ some 0 = 0) (or.inr rfl))</span>
<span class="cm">              (λ (b : ℕ) (a_1 : some a + some (nat.succ b) = 1),</span>
<span class="cm">                 id_rhs (some a = 0 ∨ some (b + 1) = 0)</span>
<span class="cm">                   (or.inl (eq.symm ((add_eq_zero_iff.mp (nat.succ_inj (option.some.inj a_1))).left) ▸ rfl)))</span>
<span class="cm">              a_1)</span>
<span class="cm">         a_1)</span>
<span class="cm">    a_1</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Dec 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698713):
<p>it does <code>option.no_confusion</code></p>

#### [ Kevin Buzzard (Dec 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698763):
<p><code>option.no_confusion</code> is such a great name for a function. I might get it on a t-shirt.</p>


{% endraw %}

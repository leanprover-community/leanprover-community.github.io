---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61444Compactopentopology.html
---

## Stream: [maths](index.html)
### Topic: [Compact-open topology](61444Compactopentopology.html)

---


{% raw %}
#### [ Patrick Massot (Sep 24 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554654):
<p>I see <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  merged <a href="https://github.com/leanprover/mathlib/pull/368" target="_blank" title="https://github.com/leanprover/mathlib/pull/368">https://github.com/leanprover/mathlib/pull/368</a> before Reid answered my comments. Was this done on purpose?</p>

#### [ Johannes Hölzl (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554751):
<p>ah, no. I was focusing on the first comment and forgot the other ones...</p>

#### [ Patrick Massot (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554770):
<p>I'm not saying they are crucial comments, but I was still suprised</p>

#### [ Johannes Hölzl (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554771):
<p>but I think also that <code>ev</code> could be changed to a <code>coe</code>.</p>

#### [ Patrick Massot (Sep 24 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134555078):
<p>I rather meant that <code>C(α, β)</code> could have a coe to fun, so that the definition of <code>ev</code> becomes <code>def ev : C(α, β) × α → β := λ p, p.1 p.2</code>, or the maybe more readable <code>def ev : C(α, β) × α → β | (f, x) := f x</code></p>

#### [ Reid Barton (Sep 24 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134557901):
<p>Patrick, regarding your very last comment, I've had too many bad experiences writing proofs about things defined by matching, and so I never use pattern matching in definitions in simple cases now. I do regret the loss of readability though. That's why I suggested <a href="#narrow/stream/113488-general/subject/eta.20for.20structures/near/130734254" title="#narrow/stream/113488-general/subject/eta.20for.20structures/near/130734254">lazy matching</a> (terminology borrowed from Haskell), so you could write <code>| ~(f, x) := f x</code> for <code>:= λ p, p.1 p.2</code>.</p>

#### [ Reid Barton (Sep 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134558026):
<p>As for the PR, I'm happy to either pretend it is still open and reply to comments by making a new PR, or just leave it as-is for now, until someone gets annoyed at the name <code>ev</code></p>

#### [ Patrick Massot (Sep 25 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589366):
<p>I don't understand the lazy matching discussion. Both the following definition work:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">x</span><span class="bp">+</span><span class="n">y</span>

<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span><span class="bp">+</span><span class="n">y</span>
</pre></div>


<p>What would you like that doesn't work?</p>

#### [ Chris Hughes (Sep 25 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589548):
<p>I think he wants to use notation similar to that to define <code>f</code> to be <code>λ x, x.1 + x.2</code></p>

#### [ Patrick Massot (Sep 25 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589734):
<p>But this is already this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span>  <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span>
<span class="n">def</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>  <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Sep 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589904):
<p>He wants to use nice notation for it, the <code>.1</code> stuff is better for definitional reduction, but <code>λ ⟨x, y⟩, x + y</code> looks nicer.</p>

#### [ Johannes Hölzl (Sep 25 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589937):
<p>The problem happens when you use coercion, e.g. from a subtype. When you use matching:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f</span> <span class="o">:</span> <span class="n">subtype</span> <span class="n">p</span> <span class="bp">-&gt;</span> <span class="n">A</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">ha</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">op</span> <span class="n">a</span><span class="o">,</span> <span class="n">ha</span><span class="bp">...⟩</span>
<span class="kn">lemma</span> <span class="n">coe_f</span> <span class="o">:</span> <span class="n">coe</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">op</span> <span class="o">(</span><span class="n">coe</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">a</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>


<p>while using projection gives us a <code>rfl</code> proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">subtype</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">op</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">...⟩</span>
<span class="kn">lemma</span> <span class="n">coe_f</span> <span class="o">:</span> <span class="n">coe</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">op</span> <span class="o">(</span><span class="n">coe</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Patrick Massot (Sep 25 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134590507):
<p>Indeed I was suprised that my <code>f = f'</code> is not rfl</p>

#### [ Reid Barton (Sep 25 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592411):
<p>More generally, when you have a function <code>f : S -&gt; T</code> and both <code>S</code> and <code>T</code> are structures, it's better (when possible) to have <code>T.mk ...</code> as the outer structure of <code>f</code>, and do the pattern matching on <code>S</code> inside, rather than having <code>S.rec_on</code> as the outer structure and constructing <code>T</code> inside.</p>

#### [ Reid Barton (Sep 25 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592472):
<p>Then if you compose with another such function <code>g : T -&gt; U</code>, and you form <code>g (f s)</code>, the places where <code>g</code> pattern matches on its argument will reduce with the <code>T.mk</code> which is the outer structure of <code>f s</code>.</p>

#### [ Reid Barton (Sep 25 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592488):
<p>If you do it the other way then <code>g (f s)</code> will look like <code>T.rec_on (S.rec_on s ...) ...</code>, and you won't be able to make any progress unless <code>s</code> is already a constructor.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134968087):
<p>FYI: I added a proper constant for the type of continuous maps and renamed the theory to <code>continuous_map</code>.</p>


{% endraw %}

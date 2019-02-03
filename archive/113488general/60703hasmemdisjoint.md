---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60703hasmemdisjoint.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [has_mem disjoint](https://leanprover-community.github.io/archive/113488general/60703hasmemdisjoint.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Oct 02 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017185):
<p>Currently, there is this definition in <code>data/list/basic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">disjoint</span> <span class="o">(</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">⦃</span><span class="n">a</span><span class="o">⦄,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l₁</span> <span class="bp">→</span> <span class="n">a</span> <span class="err">∉</span> <span class="n">l₂</span>
</pre></div>


<p>Would there be any interest in replacing it with the following more general version?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">disjoint</span> <span class="o">{</span><span class="n">α</span> <span class="n">β₁</span> <span class="n">β₂</span><span class="o">}</span> <span class="o">[</span><span class="n">has_mem</span> <span class="n">α</span> <span class="n">β₁</span><span class="o">]</span> <span class="o">[</span><span class="n">has_mem</span> <span class="n">α</span> <span class="n">β₂</span><span class="o">]</span> <span class="o">(</span><span class="n">b₁</span> <span class="o">:</span> <span class="n">β₁</span><span class="o">)</span> <span class="o">(</span><span class="n">b₂</span> <span class="o">:</span> <span class="n">β₂</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">⦃</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">⦄,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">b₁</span> <span class="bp">→</span> <span class="n">a</span> <span class="err">∉</span> <span class="n">b₂</span>
</pre></div>


<p>I'm using the latter quite a lot, and a number of the <code>list</code> theorems can be stated about it instead.</p>

#### [ Simon Hudon (Oct 02 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017241):
<p>Can those list theorems be generalized too?</p>

#### [ Sean Leather (Oct 02 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017249):
<p>A number of them could.</p>

#### [ Simon Hudon (Oct 02 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017259):
<p>What assumptions do they need on top of <code>has_mem</code>?</p>

#### [ Sean Leather (Oct 02 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017312):
<p>I haven't looked into it, but theorems like this obviously need <code>list</code>s:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">disjoint_of_disjoint_cons_left</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">:</span> <span class="n">disjoint</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l₁</span><span class="o">)</span> <span class="n">l₂</span> <span class="bp">→</span> <span class="n">disjoint</span> <span class="n">l₁</span> <span class="n">l₂</span>
</pre></div>

#### [ Sean Leather (Oct 02 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017321):
<p>But this...</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">disjoint</span><span class="bp">.</span><span class="n">symm</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">disjoint</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">disjoint</span> <span class="n">l₂</span> <span class="n">l₁</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">i₂</span> <span class="n">i₁</span> <span class="o">:=</span> <span class="n">d</span> <span class="n">i₁</span> <span class="n">i₂</span>
</pre></div>

#### [ Kenny Lau (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017383):
<p>you mean <code>lattice.disjoint</code></p>

#### [ Simon Hudon (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017384):
<p>I guess you could also reformulate the first one to use <code>insert</code></p>

#### [ Sean Leather (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017386):
<p>For me, the latter <code>disjoint</code> is useful when mixing <code>list</code> and <code>finset</code>.</p>

#### [ Sean Leather (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017398):
<blockquote>
<p>you mean <code>lattice.disjoint</code></p>
</blockquote>
<p>I don't think I do. I specifically want <code>has_mem</code>.</p>

#### [ Kenny Lau (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017401):
<p>but what structure has mem?</p>

#### [ Sean Leather (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017403):
<p>Also, <code>β₁</code> and <code>β₂</code> are different.</p>

#### [ Kenny Lau (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017404):
<p>does this make much sense for <code>option.has_mem</code>?</p>

#### [ Sean Leather (Oct 02 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017452):
<blockquote>
<p>I guess you could also reformulate the first one to use <code>insert</code></p>
</blockquote>
<p>I don't think you want to do that. It's a useful theorem by its own right.</p>

#### [ Simon Hudon (Oct 02 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017462):
<p>Right, I would keep both</p>

#### [ Sean Leather (Oct 02 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017605):
<p>Kenny: I don't understand what you mean. Plenty of things have <code>has_mem</code> instances:</p>
<div class="codehilite"><pre><span></span><span class="n">category_theory</span><span class="bp">/</span><span class="n">examples</span><span class="bp">/</span><span class="n">topological_spaces</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">X</span><span class="bp">.</span><span class="n">α</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">computability</span><span class="bp">/</span><span class="n">partrec_code</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→.</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="n">code</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">f</span> <span class="n">c</span><span class="o">,</span> <span class="kn">eval</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">f</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">finset</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">s</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">hash_map</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">hash_map</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span><span class="n">a</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">contains</span> <span class="n">a</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">multiset</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">option</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="n">has_mem</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">a</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">pfun</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">roption</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">roption</span><span class="bp">.</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">semiquot</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">semiquot</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">q</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">q</span><span class="bp">.</span><span class="n">s</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">seq</span><span class="bp">/</span><span class="n">computation</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">computation</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">computation</span><span class="bp">.</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">data</span><span class="bp">/</span><span class="n">seq</span><span class="bp">/</span><span class="n">seq</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">seq</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">data</span><span class="bp">/</span><span class="n">seq</span><span class="bp">/</span><span class="n">wseq</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">wseq</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">data</span><span class="bp">/</span><span class="n">seq</span><span class="bp">/</span><span class="n">wseq</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span>    <span class="n">unfold</span> <span class="n">cons</span> <span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span> <span class="n">wseq</span><span class="bp">.</span><span class="n">mem</span> <span class="n">seq</span><span class="bp">.</span><span class="n">mem</span> <span class="n">seq</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span> <span class="n">simp</span><span class="o">,</span>
<span class="n">linear_algebra</span><span class="bp">/</span><span class="n">submodule</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">β</span> <span class="o">(</span><span class="n">submodule</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span><span class="bp">⟩</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">theorem</span> <span class="n">ne_of_mem_of_not_mem</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">has_mem</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">lists</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">{</span><span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="o">(</span><span class="n">lists</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">lists&#39;</span> <span class="n">α</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">lists</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="o">(</span><span class="n">lists</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">lists</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">zfc</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">pSet</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">pSet</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">zfc</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">Set</span> <span class="n">Set</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">mem</span><span class="bp">⟩</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">zfc</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="k">show</span> <span class="bp">@</span><span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Set</span><span class="bp">.</span><span class="n">has_mem</span> <span class="n">y</span> <span class="err">⟦</span><span class="bp">⟨</span><span class="n">α</span><span class="o">,</span> <span class="n">A</span><span class="bp">⟩</span><span class="err">⟧</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span>
<span class="n">set_theory</span><span class="bp">/</span><span class="n">zfc</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">Class</span> <span class="n">Class</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">Class</span><span class="bp">.</span><span class="n">mem</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 02 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018358):
<p>how did you search that?</p>

#### [ Kenny Lau (Oct 02 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018400):
<p>oh, it's a grep right</p>

#### [ Sean Leather (Oct 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018684):
<blockquote>
<p>how did you search that?</p>
</blockquote>
<p><code>git grep has_mem</code></p>

#### [ Simon Hudon (Oct 02 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018757):
<p>Why not <code>#print instances has_mem</code>?</p>

#### [ Sean Leather (Oct 02 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018826):
<p>Why not? You could use that, too. <code>git grep</code> is faster and, in this case, useful enough.</p>

#### [ Simon Hudon (Oct 02 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018878):
<p>I accept your answer.</p>

#### [ Johannes Hölzl (Oct 02 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019217):
<p>I don't think a <code>has_mem</code> version of <code>disjoint</code> makes sense. You get surely some basic facts from the implication. But otherwise we don't have any structure behind <code>mem</code>. Its better to use the <code>lattice</code> version.</p>

#### [ Sean Leather (Oct 02 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019292):
<p>In my case (which may be strange), I can't use the <code>lattice</code> version. It requires the types to be the same.</p>

#### [ Mario Carneiro (Oct 02 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019293):
<p>Note that anything that satisfies that definition also fits the lattice definition (at least mathematically), since it can be expressed on the lattice of sets <code>{x | x \in s}</code></p>

#### [ Sean Leather (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019353):
<p>In particular, I want to show that a <code>list</code> and a <code>finset</code> are disjoint.</p>

#### [ Mario Carneiro (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019355):
<p>oh, I see you've made the types different</p>

#### [ Mario Carneiro (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019367):
<p>just say <code>l1.to_finset.disjoint s2</code></p>

#### [ Sean Leather (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019376):
<blockquote>
<p>just say <code>l1.to_finset.disjoint s2</code></p>
</blockquote>
<p>That adds the extra baggage of <code>to_finset</code>, which I don't need.</p>

#### [ Sean Leather (Oct 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019388):
<p>I really just want <code>∀ ⦃a : α⦄, a ∈ b₁ → a ∉ b₂</code>.</p>

#### [ Mario Carneiro (Oct 02 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019443):
<p>then define it for yourself</p>

#### [ Mario Carneiro (Oct 02 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019452):
<p>I don't see strong evidence that this is a common case</p>

#### [ Sean Leather (Oct 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020502):
<blockquote>
<p>I don't think a <code>has_mem</code> version of <code>disjoint</code> makes sense. You get surely some basic facts from the implication. But otherwise we don't have any structure behind <code>mem</code>.</p>
</blockquote>
<p>Just to make my final case for the <code>has_mem</code>-based <code>disjoint</code> above before I go away. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>
<p>Advantages:</p>
<p>1. It provides a nice generalization of the <code>list</code>-based <code>disjoint</code>. So, you can define the basic implication facts such that they work for other types beside <code>list</code>. And, yet, you can also define the <code>list</code> <code>disjoint</code> facts just as they are, so you don't lose anything.<br>
2. It works with two different types, while the <code>lattice</code> <code>disjoint</code> doesn't.<br>
3. Useful simplification theorems can be defined for different combinations of types.</p>
<p>Disadvantages:</p>
<p>1. It adds too much generality?</p>
<p>(I'm having trouble thinking of disadvantages.)</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020550):
<p>can you do the lattice disjoint using has_mem disjoint?</p>

#### [ Sean Leather (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020615):
<blockquote>
<p>can you do the lattice disjoint using has_mem disjoint?</p>
</blockquote>
<p>What do you mean?</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020625):
<p>you say it's more general, but it doesn't capture the generality of lattices</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020638):
<p>so it's really just a generalization in a different direction</p>

#### [ Sean Leather (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020647):
<p>More general in the sense that the “sets” are different even though the element type is the same.</p>

#### [ Sean Leather (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020651):
<blockquote>
<p>so it's really just a generalization in a different direction</p>
</blockquote>
<p>Yes.</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020656):
<p>In particular, I like that the bottom element need not be the empty set / "false"</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020700):
<p>i.e. when I am talking about disjoint subgroups</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020721):
<p>This kind of generality gets use in several places in mathlib. Multiple type disjointness does not</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020732):
<p>If it comes up, I'm prepared to consider a definition but we have zero theorems that need this right now</p>

#### [ Sean Leather (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020734):
<p>Yeah, so this is not a very mathematically elegant generality, more of a practical one. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Mario Carneiro (Oct 02 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020778):
<p>if all the theorems are in your project, then so should this definition</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020820):
<p>I'm not saying it's a bad definition, but it is certainly "premature optimization" for mathlib</p>

#### [ Sean Leather (Oct 02 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020883):
<p>That may be.</p>

#### [ Simon Hudon (Oct 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135057773):
<p>You could have a function <code>to_set [has_mem a b] : b -&gt; set a</code> for which <span class="user-mention" data-user-id="110045">@Sean Leather</span>' version of <code>disjoint</code> is consistent with <code>to_set a ∩ to_set b = ∅</code> even if <code>a</code> and <code>b</code> have different types.</p>


{% endraw %}

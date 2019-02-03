---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55725boundedquantifiers.html
---

## Stream: [general](index.html)
### Topic: [bounded quantifiers](55725boundedquantifiers.html)

---


{% raw %}
#### [ Sean Leather (Apr 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723227):
<p>I've seen these referred to in different places. I've inferred that a bounded forall is <code>{α : Sort*} {p : α → Prop} : ∀ x, p x</code> and a bounded exists is <code>{α : Sort*} {p : α → Prop} : ∃ x, p x</code>. In some places, they're called <code>ball</code> and <code>bex</code>. In <code>mathlib/docs/naming.md</code> (only, it appears), they are called <code>bforall</code> and <code>bexists</code>.</p>
<p>There is also notation <code>∀ x ∈ s, t</code> that refers to a bounded forall and produces <code>∀ (x : α), x ∈ s → t</code>. It works similarly for exists. In <a href="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/tests/lean/run/cute_binders.lean" target="_blank" title="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/tests/lean/run/cute_binders.lean"><code>lean/tests/lean/run/cute_binders.lean</code></a>, there is even this rather interesting code:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">range</span> <span class="o">(</span><span class="n">lower</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">upper</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">nat</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">lower</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">upper</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="o">[</span><span class="bp">`</span> <span class="n">L</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="n">U</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">range</span> <span class="n">L</span> <span class="n">U</span>

<span class="kn">variables</span> <span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">nat</span>
<span class="kn">variables</span> <span class="n">p</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="c1">-- #check a ∈ s</span>
<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">binder_types</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">∀</span> <span class="n">b</span> <span class="n">c</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span>
<span class="c1">-- ∀ (b c a : ℕ), b ∈ s → c ∈ s → a ∈ s → a + b + c &gt; 0 : Prop</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">∀</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="mi">5</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
<span class="c1">-- ∀ (a : ℕ), a &lt; 5 → p a (a + 1) : Prop</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="err">∈</span> <span class="o">[</span><span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">],</span> <span class="n">p</span> <span class="n">a</span> <span class="n">b</span>
<span class="c1">-- ∀ (a b : ℕ), a ∈ [2, 3] → b ∈ [2, 3] → p a b</span>
</pre></div>


<p>So, to my questions: Where is this bounded quantifier notation defined? Does it work wherever <code>binders</code> is found in <code>notation</code>? What are its limitations, e.g. w.r.t. the <code>p : α → Prop</code> or notation (<code>∈</code>, <code>&lt;</code>, etc.) used?</p>

#### [ Simon Hudon (Apr 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723696):
<p>I think as you suggest, it's baked into the <code>binder</code> notation. I'm actually unclear on what is accepted. I think it might accept any infix operator: <code>∀ x ⊕ unit, list x</code></p>

#### [ Patrick Massot (Apr 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723790):
<p>OMG, I never understood all these "ball". I always thought: "What ball? There is no distance here, why is this called ball?"</p>

#### [ Sean Leather (Apr 26 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723909):
<blockquote>
<p>OMG, I never understood all these "ball". I always thought: "What ball? There is no distance here, why is this called ball?"</p>
</blockquote>
<p>Part of the motivation for writing this up was also to help others who were as confused as I was. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Patrick Massot (Apr 26 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125724000):
<p>My only excuse is I was seeing this in contexts not too far away from actual balls, like <a href="https://github.com/leanprover/mathlib/blob/14a19bf3d2589a9801ef281808d8e4faa90db2b1/data/analysis/topology.lean#L88" target="_blank" title="https://github.com/leanprover/mathlib/blob/14a19bf3d2589a9801ef281808d8e4faa90db2b1/data/analysis/topology.lean#L88">https://github.com/leanprover/mathlib/blob/14a19bf3d2589a9801ef281808d8e4faa90db2b1/data/analysis/topology.lean#L88</a> which is about topological space but not metric spaces, hence maximising the confusion probability</p>

#### [ Patrick Massot (Apr 26 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125725893):
<p>Sean, what's that orange thing next to the small mathematician in your reaction?</p>

#### [ Sean Leather (Apr 26 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125726857):
<p>A b(ounded for)all. <span class="emoji emoji-26bd" title="soccer">:soccer:</span></p>

#### [ Johan Commelin (Apr 26 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125732320):
<blockquote>
<p>Sean, what's that orange thing next to the small mathematician in your reaction?</p>
</blockquote>
<p>If you hover over the emoji with your mouse, a popup will explain what the emoji tries to communicate (-;</p>

#### [ Sean Leather (Apr 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884559):
<p>As Mario <a href="#narrow/stream/116395-maths/subject/property.20applies.20to.20all.20elements.20of.20list/near/125884401" title="#narrow/stream/116395-maths/subject/property.20applies.20to.20all.20elements.20of.20list/near/125884401">pointed out</a> to me, there are yet more names for bounded quantifiers: <code>forall_mem</code> and <code>exists_mem</code>. These are used in (at least) <code>data/list/basic.lean</code>, <code>data/finset.lean</code>, and <code>data/multiset.lean</code>.</p>

#### [ Sean Leather (Apr 30 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884625):
<p>Arguably, <code>forall_mem</code> is more accurate than <code>ball</code> because it explicitly describes the <code>mem</code> bound of the quantification.</p>

#### [ Mario Carneiro (Apr 30 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884752):
<p>There is a reasonable argument for <code>ball_mem</code> instead of <code>forall_mem</code> since it is a mem bound on a bounded forall, but that's like half overlapping names and a direct reading looks more like <code>forall_mem</code></p>

#### [ Mario Carneiro (Apr 30 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884797):
<p>Currently, <code>ball</code> and <code>bex</code> are only used to describe "generic" bounded forall (some predicate) in <code>logic.basic</code></p>

#### [ Sean Leather (Apr 30 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884798):
<p>I actually like <code>forall_mem</code> for the reason you said.</p>

#### [ Sean Leather (Apr 30 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884911):
<p>The lack of <code>forall</code> in <code>ball</code> and <code>exists</code> in <code>bex</code> means that they don't show up in <code>grep</code>, which is unfortunate for those of us who rely on old-school tools. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Johan Commelin (Apr 30 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884914):
<blockquote>
<p>those of us who rely on old-school tools. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>
</blockquote>
<p>Yes, I'm still looking for a Lean plugin for good old <code>ed</code></p>

#### [ Sean Leather (Apr 30 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884964):
<p>And a punched card computer that supports UTF-8?</p>

#### [ Mario Carneiro (Apr 30 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885027):
<p>The obvious solution is to shorten <code>forall</code> and <code>exists</code> to <code>all</code> and <code>ex</code> :)</p>

#### [ Sean Leather (Apr 30 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885086):
<blockquote>
<p>The obvious solution is to shorten <code>forall</code> and <code>exists</code> to <code>all</code> and <code>ex</code> <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>
</blockquote>
<p>That would be <code>totally</code> <code>canonically</code> <code>exact</code>in the <code>next</code> <code>contextual</code> <code>parallel</code> universe that <code>extends</code> this one.</p>

#### [ Mario Carneiro (Apr 30 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885189):
<p>There's no way I'm going to try and avoid subsequences</p>

#### [ Mario Carneiro (Apr 30 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885191):
<p>If you kick vscode enough times it shows prefixes only</p>

#### [ Johan Commelin (Apr 30 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885205):
<p>Fair enough, we can grep with word boundaries</p>

#### [ Sean Leather (Apr 30 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885407):
<p>Tee hee, yet more names. <code>forall_prop</code> and <code>exists_prop</code> in <code>data/list.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">all_iff_forall_prop</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">{</span><span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">all</span> <span class="n">l</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span>

<span class="kn">theorem</span> <span class="n">any_iff_exists_prop</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">{</span><span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">any</span> <span class="n">l</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span>
</pre></div>


<p>which are actually used differently in <code>logic/basic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">forall_prop_of_true</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">q</span> <span class="n">h</span>
<span class="kn">theorem</span> <span class="n">forall_prop_of_false</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">exists_prop</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span>
<span class="kn">theorem</span> <span class="n">exists_prop_of_true</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">q</span> <span class="n">h</span>
<span class="kn">theorem</span> <span class="n">exists_prop_of_false</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">p</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 30 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885859):
<p>the <code>prop</code> in <code>all_iff_forall_prop</code> is only there for disambiguation, it could just be <code>all_iff_forall'</code> which is marginally less descriptive</p>

#### [ Mario Carneiro (Apr 30 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885877):
<p>Maybe it should be called <code>all_to_bool</code> instead, since there is a hidden <code>to_bool</code> coercion there</p>

#### [ Sean Leather (Apr 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885971):
<p>But then it seems that <code>all_iff_forall</code> should be called <code>all_iff_forall_mem</code> to be consistent with the other <code>forall_mem</code>s.</p>

#### [ Sean Leather (Apr 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885977):
<p>So you'd have <code>all_iff_forall_mem</code> and <code>all_iff_forall_mem'</code>.</p>

#### [ Sean Leather (Apr 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885986):
<p>Or even <code>all_iff_forall_bool</code> and <code>all_iff_forall_mem</code>?</p>

#### [ Mario Carneiro (Apr 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885990):
<p>true, although I reserve the right to start lopping off the right hand side of a theorem name if we all know where it's going</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887758):
<blockquote>
<p>The obvious solution is to shorten <code>forall</code> and <code>exists</code> to <code>all</code> and <code>ex</code> :)</p>
</blockquote>
<p>Let me just make the passing comment that there was a time a few months ago when Mario stopped what he was doing and wrote a bunch of one-line docstrings covering many of the important concepts in mathlib, and after that I found that old-skool grepping suddenly became a lot more effective.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887801):
<p>For example, I once wanted to know whether surjections were covered in Lean, and I grepped the Lean source code for "surjection" and got nothing at all.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887805):
<p>then after the docstrings, I grepped again and I found the word in a docstring and then I looked at the correponding theorem and found my mistake -- it's "surjective" I should be looking for.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887812):
<p>so a better solution is to put the keywords in the docs :-)</p>

#### [ Sean Leather (Apr 30 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125888856):
<blockquote>
<p>so a better solution is to put the keywords in the docs :-)</p>
</blockquote>
<p>Yes, that is useful in general. But a consistent naming scheme that allows one to consistently associate names with concepts is useful as documentation of the theorem itself <em>as well as</em> documentation within a proof using the theorem.</p>
<p>Using the surjective example, I wouldn't like to see one theorem's name use <code>surjective</code> while another used <code>onto</code>, even though the theorems are referring to the same thing.</p>

#### [ Moses Schönfinkel (Apr 30 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889121):
<p>That would be <code>epic</code>.</p>

#### [ Moses Schönfinkel (Apr 30 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889184):
<p>Oh using the joy_<code>cat</code> is super clever.</p>

#### [ Johan Commelin (Apr 30 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889234):
<p>Cool, didn't know that one existed. Will make use of it (-;</p>


{% endraw %}

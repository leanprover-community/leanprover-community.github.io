---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17362equationlemmasandsimp.html
---

## Stream: [general](index.html)
### Topic: [equation lemmas and simp](17362equationlemmasandsimp.html)

---


{% raw %}
#### [ Sean Leather (Mar 01 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126635):
<p>What is the effect of putting <code>@[simp]</code> on a <code>def</code> defined with pattern-matching equations? Does it annotate the equation lemmas with <code>@[simp]</code>?</p>

#### [ Sean Leather (Mar 01 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126899):
<p>When I look at <code>#print &lt;def-name&gt;._main.equations._eqn_1</code>, it only has <code>@[_refl_lemma]</code>.</p>

#### [ Simon Hudon (Mar 01 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126955):
<p>what do you see if you look at the other equations? (see them listed in <code>#print prefix &lt;def-name&gt;</code>)</p>

#### [ Sean Leather (Mar 01 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127031):
<p>I had to use a fully-qualified <code>&lt;def-name&gt;</code>, but that's a useful command:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span><span class="bp">._</span><span class="n">meta_aux</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="n">ts</span> <span class="o">(</span><span class="n">varb</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nth</span> <span class="n">ts</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">varb</span> <span class="mi">0</span><span class="o">)</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="n">ts</span> <span class="o">(</span><span class="n">varf</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">varf</span> <span class="n">x</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">t₁</span> <span class="n">t₂</span> <span class="o">:</span> <span class="n">typ</span> <span class="n">V</span><span class="o">),</span>
  <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="n">ts</span> <span class="o">(</span><span class="n">arr</span> <span class="n">t₁</span> <span class="n">t₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">arr</span> <span class="o">(</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="n">ts</span> <span class="n">t₁</span><span class="o">)</span> <span class="o">(</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span> <span class="n">ts</span> <span class="n">t₂</span><span class="o">)</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">sunfold</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">typ</span> <span class="n">V</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="o">(</span><span class="n">varb</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nth</span> <span class="n">ts</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">varb</span> <span class="mi">0</span><span class="o">)</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="o">(</span><span class="n">varf</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">varf</span> <span class="n">x</span>
<span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">t₁</span> <span class="n">t₂</span> <span class="o">:</span> <span class="n">typ</span> <span class="n">V</span><span class="o">),</span>
  <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="o">(</span><span class="n">arr</span> <span class="n">t₁</span> <span class="n">t₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">arr</span> <span class="o">(</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="n">t₁</span><span class="o">)</span> <span class="o">(</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="n">t₂</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Mar 01 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127074):
<p>What if you look at <code>#print tts.typ.open.equations._eqn_1 </code>?</p>

#### [ Sean Leather (Mar 01 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127075):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="bp">_</span><span class="n">refl_lemma</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">))</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="o">(</span><span class="n">varb</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nth</span> <span class="n">ts</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">varb</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">ts</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">typ</span> <span class="n">V</span><span class="o">)),</span> <span class="n">typ</span><span class="bp">.</span><span class="kn">open</span><span class="bp">._</span><span class="n">main</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span> <span class="n">ts</span>
</pre></div>

#### [ Simon Hudon (Mar 01 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127129):
<p>That's curious. The effect I see is as if those equations were labeled with <code>simp</code>. I wonder if <code>simp</code> is implied by <code>_refl_lemma</code></p>

#### [ Sean Leather (Mar 01 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127137):
<p><code>@[_refl_lemma]</code> is there whether or not I use <code>@[simp]</code>.</p>

#### [ Simon Hudon (Mar 01 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127138):
<p>We can check something else:</p>
<div class="codehilite"><pre><span></span>run_cmd attribute.get_instances `simp &gt;&gt;= trace
</pre></div>

#### [ Simon Hudon (Mar 01 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127182):
<p>Correction: </p>
<div class="codehilite"><pre><span></span>run_cmd attribute.get_instances `simp &gt;&gt;= tactic.trace ∘ list.take 3
</pre></div>

#### [ Sean Leather (Mar 01 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127192):
<div class="codehilite"><pre><span></span>parsing at line 7[tts.typ.open, finset.sort_to_finset, finset.sort_nodup]
</pre></div>

#### [ Sean Leather (Mar 01 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127237):
<p><span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span>: What does that mean?</p>

#### [ Simon Hudon (Mar 01 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127248):
<p>so the whole thing is labelled as <code>simp</code>. The <code>simp</code> tactic must have some logic to retrieve the equations related to a definition.</p>

#### [ Sean Leather (Mar 01 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127256):
<p>Could be.</p>

#### [ Simon Hudon (Mar 01 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127303):
<p><code>attribute.get_instance ```simp``` </code> gives you the list of the names that are labelled with <code>simp</code>. It works with any attribute. Every definition is appended at the beginning so taking only 3 of them was enough and I wanted to see if more than one name was being labelled</p>

#### [ Sean Leather (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127356):
<p><code>library/init/meta/simp_tactic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- `get_eqn_lemmas_for deps d` returns the automatically generated equational lemmas for definition d.</span>
<span class="cm">   If deps is tt, then lemmas for automatically generated auxiliary declarations used to define d are also included. -/</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">get_eqn_lemmas_for</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">name</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127357):
<blockquote>
<p>Could be.</p>
</blockquote>
<p>It could mean that the behavior can differ from that of using <code>simp</code> lemma or it could just be a way of compressing the list of <code>simp</code> lemmas.</p>

#### [ Simon Hudon (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127361):
<p>Nice! Thanks!</p>

#### [ Sean Leather (Mar 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127419):
<p>This is with <code>set_option trace.simplify true</code>:</p>
<div class="codehilite"><pre><span></span>3. [simplify.rewrite] [tts.typ.open.equations._eqn_3]: typ.open ts (arr t₁_a t₁_a_1) ==&gt; arr (typ.open ts t₁_a) (typ.open ts t₁_a_1)
[simplify] eq: typ.open ts t₁_a
[simplify] eq: ts
[simplify] eq: t₁_a
[simplify] eq: typ.open
</pre></div>

#### [ Sean Leather (Mar 01 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127526):
<p>So, it seems to be that <code>simp</code> uses the equation lemmas if a <code>def</code> is annotated with <code>@[simp]</code>. This makes me wonder why more definitions in the standard library and mathlib aren't <code>@[simp]</code>. It also makes me wonder if I should use <code>@[simp] def</code> more instead of writing equation lemmas myself.</p>

#### [ Sean Leather (Mar 01 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127584):
<p><code>library/init/meta/interactive.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">private</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">resolve_and_add</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">simp_lemmas</span><span class="o">)</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">(</span><span class="n">ref</span> <span class="o">:</span> <span class="n">pexpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">simp_lemmas</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">name</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span>
  <span class="n">p</span> <span class="err">←</span> <span class="n">resolve_name</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">check_no_overload</span> <span class="n">p</span><span class="o">,</span>
  <span class="c1">-- unpack local refs</span>
  <span class="k">let</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">p</span><span class="bp">.</span><span class="n">erase_annotations</span><span class="bp">.</span><span class="n">get_app_fn</span><span class="bp">.</span><span class="n">erase_annotations</span><span class="o">,</span>
  <span class="k">match</span> <span class="n">e</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">const</span> <span class="n">n</span> <span class="bp">_</span>           <span class="o">:=</span>
    <span class="o">(</span><span class="n">do</span> <span class="n">b</span> <span class="err">←</span> <span class="n">is_valid_simp_lemma_cnst</span> <span class="n">n</span><span class="o">,</span> <span class="n">guard</span> <span class="n">b</span><span class="o">,</span> <span class="n">save_const_type_info</span> <span class="n">n</span> <span class="n">ref</span><span class="o">,</span> <span class="n">s</span> <span class="err">←</span> <span class="n">s</span><span class="bp">.</span><span class="n">add_simp</span> <span class="n">n</span><span class="o">,</span> <span class="n">return</span> <span class="o">(</span><span class="n">s</span><span class="o">,</span> <span class="n">u</span><span class="o">))</span>
    <span class="bp">&lt;|&gt;</span>
    <span class="o">(</span><span class="n">do</span> <span class="n">eqns</span> <span class="err">←</span> <span class="n">get_eqn_lemmas_for</span> <span class="n">tt</span> <span class="n">n</span><span class="o">,</span> <span class="n">guard</span> <span class="o">(</span><span class="n">eqns</span><span class="bp">.</span><span class="n">length</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="n">save_const_type_info</span> <span class="n">n</span> <span class="n">ref</span><span class="o">,</span> <span class="n">s</span> <span class="err">←</span> <span class="n">add_simps</span> <span class="n">s</span> <span class="n">eqns</span><span class="o">,</span> <span class="n">return</span> <span class="o">(</span><span class="n">s</span><span class="o">,</span> <span class="n">u</span><span class="o">))</span>
    <span class="bp">&lt;|&gt;</span>
    <span class="o">(</span><span class="n">do</span> <span class="n">env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span> <span class="n">guard</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">is_projection</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">is_some</span><span class="o">,</span> <span class="n">return</span> <span class="o">(</span><span class="n">s</span><span class="o">,</span> <span class="n">n</span><span class="bp">::</span><span class="n">u</span><span class="o">))</span>
    <span class="bp">&lt;|&gt;</span>
    <span class="n">report_invalid_simp_lemma</span> <span class="n">n</span>
  <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">i_to_expr_no_subgoals</span> <span class="n">p</span><span class="o">,</span> <span class="n">b</span> <span class="err">←</span> <span class="n">is_valid_simp_lemma</span> <span class="n">e</span><span class="o">,</span> <span class="n">guard</span> <span class="n">b</span><span class="o">,</span> <span class="n">try</span> <span class="o">(</span><span class="n">save_type_info</span> <span class="n">e</span> <span class="n">ref</span><span class="o">),</span> <span class="n">s</span> <span class="err">←</span> <span class="n">s</span><span class="bp">.</span><span class="n">add</span> <span class="n">e</span><span class="o">,</span> <span class="n">return</span> <span class="o">(</span><span class="n">s</span><span class="o">,</span> <span class="n">u</span><span class="o">))</span>
    <span class="bp">&lt;|&gt;</span>
    <span class="n">report_invalid_simp_lemma</span> <span class="n">n</span>
  <span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Mar 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127639):
<p>To your second question: I think you should, it's often less repetitive</p>

#### [ Simon Hudon (Mar 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127642):
<p>I don't know how to answer your first question</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131391):
<p>There's also <code>#print attribute simp</code></p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131399):
<p>I believe Leo rather wants us to use <code>simp!</code> than to tag every single def with <code>[simp]</code></p>

#### [ Sean Leather (Mar 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131449):
<blockquote>
<p>There's also <code>#print attribute simp</code></p>
</blockquote>
<p><code>error: invalid #print command</code></p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131615):
<p>Ah, this is fun. You can do <code>#print [refl]</code>, but not <code>#print [simp]</code>.</p>

#### [ Sean Leather (Mar 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131630):
<p><a href="https://github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f5ed07a9ca7e18052989b6ce28b7eb30" target="_blank" title="https://github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f5ed07a9ca7e18052989b6ce28b7eb30"><code>simp!</code></a>:</p>
<blockquote>
<ul>
<li>Add <code>iota_eqn : bool</code> field to <code>simp_config</code>. <code>simp {iota_eqn := tt}</code> uses all non trivial equation lemmas generated by equation/pattern-matching compiler. A lemma is considered non trivial if it is not of the form <code>forall x_1 ... x_n, f x_1 ... x_n = t</code> and a proof by reflexivity. <code>simp!</code> is a shorthand for <code>simp {iota_eqn := tt}</code>. For example, given the goal <code>... |- [1,2].map nat.succ = t</code>, <code>simp!</code> reduces the left-hand-side of the equation to <code>[nat.succ 1, nat.succ 2]</code>. In this example, <code>simp!</code> is equivalent to <code>simp [list.map]</code>.</li>
</ul>
</blockquote>

#### [ Moses Schönfinkel (Mar 01 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131668):
<p>Getting closer to Coq <code>cbn</code> :).</p>

#### [ Sean Leather (Mar 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131694):
<p>“non-trivial equation lemmas” - What does this imply about the trivial equation lemmas, which all of mine probably are?</p>

#### [ Sean Leather (Mar 01 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131778):
<blockquote>
<p>Ah, this is fun. You can do <code>#print [refl]</code>, but not <code>#print [simp]</code>.</p>
</blockquote>
<p>Is that just a matter of forgetting to include <code>simp</code> somewhere?</p>

#### [ Sean Leather (Mar 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131796):
<p><code>#print [_refl_lemma]</code> works.</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131840):
<p>No, <code>#print [simp]</code> is just a different syntax <a href="https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/tests/lean/run/simplifier_custom_relations.lean#L23" target="_blank" title="https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/tests/lean/run/simplifier_custom_relations.lean#L23">https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/tests/lean/run/simplifier_custom_relations.lean#L23</a></p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131843):
<p>So yeah, <code>#print [simp] default</code> works</p>

#### [ Sean Leather (Mar 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131887):
<blockquote>
<p>“non-trivial equation lemmas” - What does this imply about the trivial equation lemmas, which all of mine probably are?</p>
</blockquote>
<p>Considering <a href="http://httpsf//github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f3c3d54612bd08c035a1578e952b2aeaR216" target="_blank" title="http://httpsf//github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f3c3d54612bd08c035a1578e952b2aeaR216">this comment</a>, I think the description in <code>doc/changes.md</code> above is either confusing or misleading:</p>
<div class="codehilite"><pre><span></span><span class="gi">+(iota_eqn : bool           := ff) -- reduce using all equation lemmas generated by equation/pattern-matching compiler</span>
</pre></div>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131894):
<p>No, "non-trivial" basically means "defined by pattern matching"</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131895):
<p>I.e. "more than one equation"</p>

#### [ Sean Leather (Mar 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131966):
<p>So, could you replace “<em>non trivial equation lemmas generated by equation/pattern-matching compiler. A lemma is considered non trivial if it is not of the form <code>forall x_1 ... x_n, f x_1 ... x_n = t</code> and a proof by reflexivity</em>” above with “<em>equation lemmas generated by equation/pattern-matching compiler</em>” and the statement would be the same?</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132241):
<p>I'm not sure anymore. Perhaps the <code>iota_eqn</code> comment should instead be extended with a "non-trivial"</p>

#### [ Sean Leather (Mar 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132382):
<blockquote>
<p>So yeah, <code>#print [simp] default</code> works</p>
</blockquote>
<p>Yeah, it's nice to see my equation lemmas appear in that list after adding <code>@[simp]</code> to a <code>def</code>.</p>

#### [ Sean Leather (Mar 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132395):
<p>I'm not sure if there are any alternative arguments to <code>#print [simp]</code>. It doesn't appear to take a prefix or identifier name: <code>unknown simp_lemmas collection</code>.</p>

#### [ Sean Leather (Mar 01 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133132):
<p>I get syntax errors on the second <code>simp!</code> in <code>induction xs; [simp!, {cases ts, simp!}]</code>.</p>

#### [ Sean Leather (Mar 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133208):
<p>But <code>induction xs; [simp!, {cases ts, simp {iota_eqn := tt}}]</code> works.</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133979):
<p><code>!}</code> is a separate token used for hole commands</p>


{% endraw %}

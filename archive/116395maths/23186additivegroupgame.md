---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23186additivegroupgame.html
---

## Stream: [maths](index.html)
### Topic: [additive group game](23186additivegroupgame.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802827):
<p>The additive group <code>add_group</code> in Lean is defined in core Lean, which means it's hard to change. The definition is this:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802831):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">100</span><span class="o">]</span>
<span class="kn">structure</span> <span class="n">add_group</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="n">fields</span><span class="o">:</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">add_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c_1</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c_1</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c_1</span><span class="o">)</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">zero</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">zero_add</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">add_zero</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">a</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">neg</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">add_left_neg</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">-</span><span class="n">a</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802834):
<p>It's a class, with a bunch of axioms.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802837):
<p>And I think one of them follows from the others</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802840):
<p>which means that <code>add_group</code> can be made to go faster, I think.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802841):
<p>Is that right?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802842):
<p>I wanted to prove this myself:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802843):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">theorem</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">add_zero</span>
<span class="o">(</span><span class="n">add</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c</span><span class="o">))</span>
<span class="o">(</span><span class="n">zero</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">zero_add</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">neg</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_left_neg</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="bp">-</span><span class="n">a</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802882):
<p>I just faffed around and cut and pasted that from Lean output, it was pretty painful, it would have been much easier to do in emacs.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802883):
<p>And at the end of it all, it didn't work anyway</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802886):
<p>because it doesn't know what <code>+</code> means yet</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802894):
<p>I just wanted to make myself a toy abelian group</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802896):
<p>but then start taking away the axioms by editing the definition</p>

#### [ Kevin Buzzard (Apr 28 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802998):
<p>All I want to do is to create an additive group but with one axiom missing.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802999):
<p>Is there a trick?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125803007):
<p>Can I create one with type class inference and then write over the axiom with a sorry?</p>


{% endraw %}

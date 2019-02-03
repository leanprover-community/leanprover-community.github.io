---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19895Inductivetypecompilationerror.html
---

## Stream: [general](index.html)
### Topic: [Inductive type compilation error](19895Inductivetypecompilationerror.html)

---


{% raw %}
#### [ Jesse Michael Han (Feb 02 2019 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408201):
<p>What's up with the following error? The presence of the <code>complete_boolean_algebra</code> instance in the following code</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>

<span class="kn">inductive</span> <span class="n">B_name</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">complete_boolean_algebra</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="c1">-- complains only if complete_boolean_algebra instance is there</span>
<span class="bp">|</span> <span class="n">mk</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">B_name</span> <span class="bp">×</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span> <span class="n">B_name</span>
</pre></div>


<p>results in the following error message:</p>
<div class="codehilite"><pre><span></span><span class="mi">23</span><span class="o">:</span><span class="mi">1</span><span class="o">:</span> <span class="n">nested</span> <span class="kn">inductive</span> <span class="n">type</span> <span class="n">compiled</span> <span class="n">to</span> <span class="n">invalid</span> <span class="kn">inductive</span> <span class="n">type</span>
<span class="n">nested</span> <span class="n">exception</span> <span class="n">message</span><span class="o">:</span>
<span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="kn">definition</span> <span class="err">&#39;</span><span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">sizeof_spec&#39;</span><span class="o">,</span> <span class="n">has</span> <span class="n">type</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">complete_boolean_algebra</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">β_inst_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">B_name</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span>
    <span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">β_inst_inst</span> <span class="o">(</span><span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">mk</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">fst</span> <span class="n">snd</span><span class="o">)</span> <span class="bp">=</span>
      <span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">β_inst_inst</span> <span class="o">(</span><span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">mk</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">fst</span> <span class="n">snd</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">complete_boolean_algebra</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">β_inst_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">B_name</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span>
    <span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">β_inst_inst</span> <span class="o">(</span><span class="bp">_</span><span class="n">nest_1_1</span><span class="bp">.</span><span class="n">prod</span><span class="bp">.</span><span class="n">B_name</span><span class="bp">.</span><span class="n">mk</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">fst</span> <span class="n">snd</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">sizeof</span> <span class="n">snd</span>
</pre></div>

#### [ Mario Carneiro (Feb 02 2019 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408397):
<p>That's a nested inductive type</p>

#### [ Mario Carneiro (Feb 02 2019 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408398):
<p>these aren't compiled very well</p>

#### [ Jesse Michael Han (Feb 02 2019 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408442):
<p>Does the presence of the <code>complete_boolean_algebra</code> instance make it nested, or is it nested because of the type of the constructor <code>mk</code>?</p>

#### [ Mario Carneiro (Feb 02 2019 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408453):
<p>an isomorphic regular inductive is</p>
<div class="codehilite"><pre><span></span>inductive B_name (β : Type u) [complete_boolean_algebra β] : Type (u+1) -- complains only if complete_boolean_algebra instance is there
| mk (α : Type u) (A : α → B_name) (B : α → β) : B_name
</pre></div>

#### [ Mario Carneiro (Feb 02 2019 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408497):
<p>it's the fact that you used a product of some type that hasn't been constructed yet</p>

#### [ Jesse Michael Han (Feb 02 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408519):
<p>I see... I guess it's "simpler" to just specify two simultaneous values instead of specifying a pair as a value</p>

#### [ Jesse Michael Han (Feb 02 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408520):
<p>Thanks for clarifying!</p>

#### [ Mario Carneiro (Feb 02 2019 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inductive%20type%20compilation%20error/near/157408617):
<p>Well, it's mostly the fact that inductives have a strict specification on what is allowed in the constructors, and other inductive types aren't in that specification. Lean has a trick for compiling them anyway, but it's complicated and not completely correct in some edge cases</p>


{% endraw %}
